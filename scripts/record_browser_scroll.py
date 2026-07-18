#!/usr/bin/env python3
"""Record a reviewable browser scroll clip and contact sheet.

Examples:
  ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/record_browser_scroll.py
  ARTIFACT_ROOT=/path/to/site python3 scripts/record_browser_scroll.py
"""
from __future__ import annotations

import contextlib
import functools
import http.server
import json
import os
import shutil
import socket
import socketserver
import subprocess
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(os.environ.get("ARTIFACT_ROOT", ".")).resolve()
PORT = int(os.environ.get("ARTIFACT_PORT", "4174"))
ARTIFACT_URL = os.environ.get("ARTIFACT_URL", "").strip()
REPORT_BASE = Path(os.environ.get("ARTIFACT_REPORT_DIR", ROOT / "reports")).resolve()
REPORT_DIR = REPORT_BASE / f"scroll-video-{time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())}"


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


def scroll_through(page) -> None:
    for frame in range(91):
        progress = frame / 90
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
        page.wait_for_timeout(75)


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    server = None
    report: dict[str, object] = {"root": str(ROOT), "report": str(REPORT_DIR)}
    try:
        if not shutil.which("ffmpeg"):
            raise RuntimeError("FFmpeg is required to create MP4 and contact-sheet evidence")
        if ARTIFACT_URL:
            if not valid_url(ARTIFACT_URL):
                raise ValueError(f"Invalid ARTIFACT_URL: {ARTIFACT_URL}")
            url, mode = ARTIFACT_URL, "external-url"
        else:
            server = start_static_server(ROOT, PORT)
            url, mode = f"http://127.0.0.1:{PORT}/", "static-root"
        report.update({"url": url, "serveMode": mode})

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage", "--enable-webgl", "--ignore-gpu-blocklist", "--enable-unsafe-swiftshader"],
            )
            context = browser.new_context(
                viewport={"width": 1440, "height": 950},
                record_video_dir=str(REPORT_DIR),
                record_video_size={"width": 1440, "height": 950},
            )
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=45000)
            page.wait_for_timeout(700)
            scroll_through(page)
            report["status"] = page.evaluate("() => window.__APP_STATUS__ ?? null")
            video = page.video
            page.close()
            context.close()
            if video is None:
                raise RuntimeError("No Playwright video handle was created")
            webm = Path(video.path())
            browser.close()

        if video is None:
            raise RuntimeError("No Playwright video handle was created")
        if not webm.is_file():
            raise RuntimeError("No Playwright video was recorded")
        mp4 = REPORT_DIR / "scroll-preview.mp4"
        contact_sheet = REPORT_DIR / "contact-sheet.jpg"
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(webm), "-filter:v", "fps=30,format=yuv420p", "-an", "-c:v", "libx264", "-preset", "veryfast", "-movflags", "+faststart", str(mp4)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(mp4), "-vf", "fps=1/2,scale=360:-1,tile=4x2", "-frames:v", "1", "-update", "1", str(contact_sheet)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        report.update({"ok": True, "webm": str(webm), "mp4": str(mp4), "contactSheet": str(contact_sheet)})
        exit_code = 0
    except Exception as error:
        report.update({"ok": False, "error": f"{type(error).__name__}: {error}"})
        exit_code = 1
    finally:
        if server:
            server.shutdown()
            server.server_close()
        (REPORT_DIR / "video-readback.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
