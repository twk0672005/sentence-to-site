#!/usr/bin/env python3
"""Generic browser verification script for static website / WebGL artifacts.

Two modes:
  1. Existing dev server:
     ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/verify_browser_artifact.py

  2. Static folder:
     ARTIFACT_ROOT=/path/to/site ARTIFACT_PORT=4173 python3 scripts/verify_browser_artifact.py

Requires:
  pip install -r requirements.txt
  playwright install chromium
"""
from __future__ import annotations

import contextlib
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
OUT_BASE = Path(os.environ.get("ARTIFACT_REPORT_DIR", str(ROOT / "reports"))).resolve()
OUT = OUT_BASE / ("browser-verify-" + time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()))

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

    summary = {"url": url, "root": str(ROOT), "outputs": str(OUT), "serveMode": serve_mode}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--enable-webgl",
                "--ignore-gpu-blocklist",
                "--enable-unsafe-swiftshader",
            ])
            for label, viewport in [("desktop", {"width": 1440, "height": 950}), ("mobile", {"width": 390, "height": 844})]:
                page = browser.new_page(viewport=viewport)
                console_errors = []
                page_errors = []
                failed = []
                page.on("console", lambda msg: console_errors.append({"type": msg.type, "text": msg.text}) if msg.type in ("error", "warning") else None)
                page.on("pageerror", lambda exc: page_errors.append(str(exc)))
                page.on("requestfailed", lambda req: failed.append({"url": req.url, "failure": req.failure}))
                page.goto(url, wait_until="networkidle", timeout=45000)
                title = page.title()
                h1_count = page.locator("h1").count()
                h1 = page.locator("h1").first.text_content(timeout=5000) if h1_count else ""
                body_sample = page.locator("body").inner_text(timeout=5000)[:500]
                for name, progress in [("top", 0), ("mid", 0.55), ("final", 1)]:
                    page.evaluate("""p => {
                        const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                        document.documentElement.style.scrollBehavior = 'auto';
                        document.body.style.scrollBehavior = 'auto';
                        window.scrollTo(0, max * p);
                        if (window.__COSMIC_SET_PROGRESS__) window.__COSMIC_SET_PROGRESS__(p);
                        if (window.__APP_SET_PROGRESS__) window.__APP_SET_PROGRESS__(p);
                    }""", progress)
                    page.wait_for_timeout(800)
                    page.screenshot(path=str(OUT / f"{label}-{name}.png"), full_page=False)
                readback = page.evaluate("() => window.__COSMIC_ZOOM_STATUS__ || window.__APP_STATUS__ || null")
                summary[label] = {
                    "title": title,
                    "h1": h1,
                    "bodySample": body_sample,
                    "readback": readback,
                    "consoleErrors": [e for e in console_errors if e["type"] == "error"],
                    "consoleWarnings": [e for e in console_errors if e["type"] == "warning"],
                    "pageErrors": page_errors,
                    "requestFailed": failed,
                }
                if TITLE_CONTAINS and TITLE_CONTAINS not in title:
                    raise AssertionError({"title": title, "expected": TITLE_CONTAINS})
                if H1_CONTAINS and H1_CONTAINS not in h1:
                    raise AssertionError({"h1": h1, "expected": H1_CONTAINS})
                if summary[label]["consoleErrors"] or page_errors:
                    raise AssertionError({"consoleErrors": summary[label]["consoleErrors"], "pageErrors": page_errors})
                page.close()
            browser.close()
        (OUT / "readback.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"ok": True, "report": str(OUT / "readback.json"), "screenshots": str(OUT), "serveMode": serve_mode}, ensure_ascii=False, indent=2))
        return 0
    finally:
        if server:
            server.shutdown()
            server.server_close()

if __name__ == "__main__":
    raise SystemExit(main())
