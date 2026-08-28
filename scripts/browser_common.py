#!/usr/bin/env python3
"""Shared fail-closed target and receipt helpers for browser evidence scripts."""
from __future__ import annotations

import contextlib
import hashlib
import http.server
import ipaddress
import json
import os
import socketserver
import threading
import time
from dataclasses import dataclass
from functools import partial
from pathlib import Path
from typing import Iterator
from urllib.parse import quote, urlparse


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt: str, *args: object) -> None:
        pass


class ReuseTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


@dataclass
class BrowserTarget:
    url: str
    mode: str
    root: Path | None
    server: ReuseTCPServer | None
    thread: threading.Thread | None


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    normalized = raw.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"{name} must be true/false, got {raw!r}")


def is_loopback_host(hostname: str | None) -> bool:
    if not hostname:
        return False
    if hostname.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(hostname).is_loopback
    except ValueError:
        return False


def validate_external_url(url: str, allow_remote: bool) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"ARTIFACT_URL must be an absolute http(s) URL: {url!r}")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("ARTIFACT_URL must not contain username/password userinfo")
    if not is_loopback_host(parsed.hostname) and not allow_remote:
        raise ValueError(
            "Remote ARTIFACT_URL is disabled by default. Set ALLOW_REMOTE_URL=1 "
            "only when external browsing is in scope."
        )
    return url


def receipt_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed._replace(query="", fragment="").geturl()


def validate_static_root(root: Path, entry_value: str) -> Path:
    entry = Path(entry_value)
    if entry.is_absolute() or ".." in entry.parts:
        raise ValueError(f"ARTIFACT_ENTRY must stay inside ARTIFACT_ROOT: {entry_value!r}")
    entry_path = (root / entry).resolve()
    try:
        entry_path.relative_to(root)
    except ValueError as exc:
        raise ValueError("ARTIFACT_ENTRY escapes ARTIFACT_ROOT") from exc
    if not entry_path.is_file():
        raise ValueError(f"Static entry file does not exist: {entry_path}")

    forbidden_names = {
        ".aws",
        ".env",
        ".git",
        ".netrc",
        ".npmrc",
        ".pypirc",
        ".ssh",
        "credentials.json",
        "id_ed25519",
        "id_rsa",
        "service-account.json",
    }
    forbidden_suffixes = {".key", ".pem", ".p12", ".pfx"}
    unsafe: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if path.is_symlink():
            unsafe.append(f"symlink:{relative.as_posix()}")
        if path.name in forbidden_names or path.name.startswith(".env."):
            unsafe.append(relative.as_posix())
        if path.is_file() and path.suffix.lower() in forbidden_suffixes:
            unsafe.append(relative.as_posix())
        if len(unsafe) >= 8:
            break
    if unsafe:
        raise ValueError(
            "ARTIFACT_ROOT contains sensitive or escaping entries. Serve a sanitized "
            f"build/staging directory instead: {', '.join(unsafe)}"
        )
    return entry


@contextlib.contextmanager
def browser_target() -> Iterator[BrowserTarget]:
    artifact_url = os.environ.get("ARTIFACT_URL", "").strip()
    allow_remote = env_bool("ALLOW_REMOTE_URL", False)
    if artifact_url:
        yield BrowserTarget(
            url=validate_external_url(artifact_url, allow_remote),
            mode="external-url",
            root=None,
            server=None,
            thread=None,
        )
        return

    root = Path(os.environ.get("ARTIFACT_ROOT", ".")).resolve()
    if not root.is_dir():
        raise ValueError(f"ARTIFACT_ROOT is not a directory: {root}")
    entry = validate_static_root(root, os.environ.get("ARTIFACT_ENTRY", "index.html"))
    port = int(os.environ.get("ARTIFACT_PORT", "0"))
    if not 0 <= port <= 65535:
        raise ValueError(f"ARTIFACT_PORT is outside 0..65535: {port}")

    handler = partial(QuietHandler, directory=str(root))
    try:
        server = ReuseTCPServer(("127.0.0.1", port), handler)
    except OSError as exc:
        raise RuntimeError(
            f"Cannot bind static artifact server on 127.0.0.1:{port}; "
            "the port may belong to another project. Choose ARTIFACT_PORT=0 "
            "or a verified free port."
        ) from exc

    assigned_port = int(server.server_address[1])
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    target = BrowserTarget(
        url=f"http://127.0.0.1:{assigned_port}/{quote(entry.as_posix())}",
        mode="static-root",
        root=root,
        server=server,
        thread=thread,
    )
    try:
        yield target
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def output_dir(prefix: str) -> Path:
    base = Path(os.environ.get("ARTIFACT_REPORT_DIR", str(Path.cwd() / "reports"))).resolve()
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    candidate = base / f"{prefix}-{stamp}"
    suffix = 1
    while candidate.exists():
        candidate = base / f"{prefix}-{stamp}-{suffix}"
        suffix += 1
    candidate.mkdir(parents=True)
    return candidate


def file_receipt(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def three_state_receipts_are_distinct(states: list[dict[str, object]]) -> bool:
    if len(states) != 3:
        return False
    names = [str(item.get("name")) for item in states]
    artifacts = [item.get("artifact") for item in states]
    if not all(isinstance(item, dict) for item in artifacts):
        return False
    hashes = [str(item.get("sha256")) for item in artifacts]  # type: ignore[union-attr]
    return names == ["start", "mid", "settled"] and len(set(hashes)) == 3


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def identity_expectations() -> dict[str, str]:
    values = {
        "title": os.environ.get("TITLE_CONTAINS", "").strip(),
        "h1": os.environ.get("H1_CONTAINS", "").strip(),
        "body": os.environ.get("BODY_CONTAINS", "").strip(),
    }
    if not any(values.values()):
        raise ValueError(
            "Set at least one identity marker: TITLE_CONTAINS, H1_CONTAINS, "
            "or BODY_CONTAINS. This prevents a stale server from passing."
        )
    return values


def progress_adapter() -> str:
    adapter = os.environ.get("PROGRESS_ADAPTER", "none").strip().lower()
    if adapter not in {"none", "app", "cosmic"}:
        raise ValueError("PROGRESS_ADAPTER must be none, app, or cosmic")
    return adapter


def set_progress(page: object, progress: float, adapter: str) -> None:
    # Real scrolling always happens. Project hooks are an explicit diagnostic adapter.
    page.evaluate(
        """([p, adapter]) => {
          const max = Math.max(0, document.documentElement.scrollHeight - innerHeight);
          document.documentElement.style.scrollBehavior = 'auto';
          document.body.style.scrollBehavior = 'auto';
          window.scrollTo(0, max * p);
          if (adapter === 'app' && window.__APP_SET_PROGRESS__) window.__APP_SET_PROGRESS__(p);
          if (adapter === 'cosmic' && window.__COSMIC_SET_PROGRESS__) window.__COSMIC_SET_PROGRESS__(p);
        }""",
        [progress, adapter],
    )


def read_status(page: object) -> object:
    return page.evaluate(
        """() => ({
          app: window.__APP_STATUS__ ?? null,
          cosmic: window.__COSMIC_ZOOM_STATUS__ ?? null,
          scrollY: window.scrollY,
          scrollMax: Math.max(0, document.documentElement.scrollHeight - innerHeight),
          runningAnimations: document.getAnimations().filter(a => a.playState === 'running').length
        })"""
    )
