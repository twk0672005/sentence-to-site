# Tooling

The executable scripts are optional. Use them when a claim needs browser-visible proof.

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

Scroll video recording also needs FFmpeg available on `PATH`.

## Browser verification

```bash
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/verify_browser_artifact.py
```

Or, for already-built static files:

```bash
ARTIFACT_ROOT=/path/to/site python3 scripts/verify_browser_artifact.py
```

The script captures desktop/mobile top, middle, and final states, title/H1 readback, browser errors, and failed requests.

## Scroll recording

```bash
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/record_browser_scroll.py
```

It creates a reviewable MP4, contact sheet, and JSON readback. Set `ARTIFACT_REPORT_DIR` to keep generated evidence outside the site tree.

## If tooling cannot run

Do not silently substitute a build result. Mark the result `partial` or `blocked`, state whether Playwright, Chromium, FFmpeg, the server, or the target page is unavailable, and preserve any useful evidence that did succeed.
