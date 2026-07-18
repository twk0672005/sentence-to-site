#!/usr/bin/env python3
"""Capture browser-visible evidence for a running or static website.

Examples:
  ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/verify_browser_artifact.py
  ARTIFACT_ROOT=/path/to/site python3 scripts/verify_browser_artifact.py
"""
from __future__ import annotations

import contextlib
import functools
import http.server
import json
import os
import socket
import socketserver
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(os.environ.get("ARTIFACT_ROOT", ".")).resolve()
PORT = int(os.environ.get("ARTIFACT_PORT", "4173"))
ARTIFACT_URL = os.environ.get("ARTIFACT_URL", "").strip()
TITLE_CONTAINS = os.environ.get("TITLE_CONTAINS", "")
H1_CONTAINS = os.environ.get("H1_CONTAINS", "")
REPORT_BASE = Path(os.environ.get("ARTIFACT_REPORT_DIR", ROOT / "reports")).resolve()
REPORT_DIR = REPORT_BASE / f"browser-verify-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


class ReusableServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def port_in_use(port: int) -> bool:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as connection:
        connection.settimeout(0.5)
        return connection.connect_ex(("127.0.0.1", port)) == 0


def valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def start_static_server(root: Path, port: int) -> ReusableServer:
    if not root.is_dir():
        raise FileNotFoundError(f"ARTIFACT_ROOT is not a directory: {root}")
    if port_in_use(port):
        raise RuntimeError(
            f"Port {port} is already in use. Set ARTIFACT_URL for that server or choose another ARTIFACT_PORT."
        )
    handler = functools.partial(QuietHandler, directory=str(root))
    server = ReusableServer(("127.0.0.1", port), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


def attach_listeners(page) -> dict[str, list]:
    # Must be attached BEFORE page.goto so load-time errors are captured.
    captured: dict[str, list] = {"console": [], "pageErrors": [], "failedRequests": []}
    page.on(
        "console",
        lambda message: captured["console"].append({"type": message.type, "text": message.text})
        if message.type in {"error", "warning"}
        else None,
    )
    page.on("pageerror", lambda error: captured["pageErrors"].append(str(error)))
    page.on(
        "requestfailed",
        lambda request: captured["failedRequests"].append({"url": request.url, "failure": request.failure}),
    )
    return captured


def capture_view(page, label: str, summary: dict, captured: dict[str, list]) -> None:
    console_messages = captured["console"]
    page_errors = captured["pageErrors"]
    failed_requests = captured["failedRequests"]

    title = page.title()
    h1 = page.locator("h1").first.text_content() if page.locator("h1").count() else ""
    body_sample = page.locator("body").inner_text()[:500]
    for state, progress in (("top", 0), ("mid", 0.55), ("final", 1)):
        page.evaluate(
            """progress => {
                const maximum = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                document.documentElement.style.scrollBehavior = 'auto';
                document.body.style.scrollBehavior = 'auto';
                window.scrollTo(0, maximum * progress);
                if (typeof window.__APP_SET_PROGRESS__ === 'function') {
                    window.__APP_SET_PROGRESS__(progress);
                }
            }""",
            progress,
        )
        page.wait_for_timeout(700)
        page.screenshot(path=str(REPORT_DIR / f"{label}-{state}.png"), full_page=False)

    summary[label] = {
        "title": title,
        "h1": h1,
        "bodySample": body_sample,
        "status": page.evaluate("() => window.__APP_STATUS__ ?? null"),
        "consoleErrors": [item for item in console_messages if item["type"] == "error"],
        "consoleWarnings": [item for item in console_messages if item["type"] == "warning"],
        "pageErrors": page_errors,
        "failedRequests": failed_requests,
    }
    if TITLE_CONTAINS and TITLE_CONTAINS not in title:
        raise AssertionError({"title": title, "expected": TITLE_CONTAINS})
    if H1_CONTAINS and H1_CONTAINS not in h1:
        raise AssertionError({"h1": h1, "expected": H1_CONTAINS})
    if summary[label]["consoleErrors"] or page_errors:
        raise AssertionError({"consoleErrors": summary[label]["consoleErrors"], "pageErrors": page_errors})


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    server = None
    summary: dict[str, object] = {"root": str(ROOT), "report": str(REPORT_DIR)}
    try:
        if ARTIFACT_URL:
            if not valid_url(ARTIFACT_URL):
                raise ValueError(f"Invalid ARTIFACT_URL: {ARTIFACT_URL}")
            url, mode = ARTIFACT_URL, "external-url"
        else:
            server = start_static_server(ROOT, PORT)
            url, mode = f"http://127.0.0.1:{PORT}/", "static-root"
        summary.update({"url": url, "serveMode": mode})

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage", "--enable-webgl", "--ignore-gpu-blocklist", "--enable-unsafe-swiftshader"],
            )
            for label, viewport in (("desktop", {"width": 1440, "height": 950}), ("mobile", {"width": 390, "height": 844})):
                page = browser.new_page(viewport=viewport)
                captured = attach_listeners(page)
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(700)
                capture_view(page, label, summary, captured)
                page.close()
            browser.close()
        summary["ok"] = True
        exit_code = 0
    except Exception as error:
        summary.update({"ok": False, "error": f"{type(error).__name__}: {error}"})
        exit_code = 1
    finally:
        if server:
            server.shutdown()
            server.server_close()
        (REPORT_DIR / "readback.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
