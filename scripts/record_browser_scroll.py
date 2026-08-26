#!/usr/bin/env python3
"""Record a short browser scroll video for animation evidence.

Two modes:
  ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/record_browser_scroll.py
  ARTIFACT_ROOT=/path/to/site ARTIFACT_PORT=4174 python3 scripts/record_browser_scroll.py
"""
from __future__ import annotations

import contextlib
import http.server
import json
import os
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
OUT_BASE = Path(os.environ.get("ARTIFACT_REPORT_DIR", str(ROOT / "reports"))).resolve()
OUT = OUT_BASE / ("scroll-video-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

class ReuseTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

def port_open(port: int) -> bool:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0

def valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    server = None
    if ARTIFACT_URL:
        if not valid_url(ARTIFACT_URL):
            raise SystemExit(f"Invalid ARTIFACT_URL: {ARTIFACT_URL}")
        url = ARTIFACT_URL
        serve_mode = "external-url"
    else:
        os.chdir(ROOT)
        if not port_open(PORT):
            server = ReuseTCPServer(("127.0.0.1", PORT), QuietHandler)
            threading.Thread(target=server.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{PORT}/"
        serve_mode = "static-root"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage", "--enable-webgl", "--ignore-gpu-blocklist", "--enable-unsafe-swiftshader"])
            ctx = browser.new_context(viewport={"width": 1440, "height": 950}, record_video_dir=str(OUT), record_video_size={"width": 1440, "height": 950})
            page = ctx.new_page()
            page.goto(url, wait_until="networkidle", timeout=45000)
            for i in range(0, 121):
                progress = i / 120
                page.evaluate("""p => {
                    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                    document.documentElement.style.scrollBehavior = 'auto';
                    document.body.style.scrollBehavior = 'auto';
                    window.scrollTo(0, max * p);
                    if (window.__COSMIC_SET_PROGRESS__) window.__COSMIC_SET_PROGRESS__(p);
                    if (window.__APP_SET_PROGRESS__) window.__APP_SET_PROGRESS__(p);
                }""", progress)
                page.wait_for_timeout(33)
            status = page.evaluate("() => window.__COSMIC_ZOOM_STATUS__ || window.__APP_STATUS__ || null")
            page.close(); ctx.close(); browser.close()
        webms = sorted(OUT.glob("*.webm"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not webms:
            raise RuntimeError("No Playwright video was recorded")
        webm = webms[0]
        mp4 = OUT / "scroll-preview.mp4"
        # Preserve real review duration. Do not over-compress time: the animation
        # workflow expects a human-inspectable 6-12 second MP4, not a split-second timelapse.
        subprocess.run(["ffmpeg", "-y", "-i", str(webm), "-filter:v", "fps=30,format=yuv420p", "-an", "-c:v", "libx264", "-preset", "veryfast", "-movflags", "+faststart", str(mp4)], check=True)
        contact_sheet = OUT / "contact-sheet.jpg"
        subprocess.run(["ffmpeg", "-y", "-i", str(mp4), "-vf", "fps=1,scale=360:-1,tile=4x2", "-frames:v", "1", "-update", "1", str(contact_sheet)], check=True)
        report = {"ok": True, "url": url, "serveMode": serve_mode, "webm": str(webm), "mp4": str(mp4), "contactSheet": str(contact_sheet), "status": status}
        (OUT / "video-readback.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    finally:
        if server:
            server.shutdown(); server.server_close()

if __name__ == "__main__":
    raise SystemExit(main())
