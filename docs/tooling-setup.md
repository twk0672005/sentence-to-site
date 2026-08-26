# Tooling Setup

這包可以放入任何網站 / 動畫專案旁邊使用。以下是常用工具。

## Python browser verification

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

如果不想用 venv：

```bash
pip install playwright
playwright install chromium
```

## FFmpeg

錄影轉 MP4 需要 FFmpeg。

Ubuntu / Debian：

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

macOS：

```bash
brew install ffmpeg
```

## 驗證 static artifact

```bash
ARTIFACT_ROOT=/path/to/site ARTIFACT_PORT=4173 python3 scripts/verify_browser_artifact.py
```

## 驗證已啟動的 dev server

如果 Vite / Next / Astro 已經在跑：

```bash
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/verify_browser_artifact.py
```

## 錄 scroll video

```bash
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/record_browser_scroll.py
```

或者 static serve：

```bash
ARTIFACT_ROOT=/path/to/site ARTIFACT_PORT=4174 python3 scripts/record_browser_scroll.py
```

## Script syntax check

```bash
python3 -m py_compile scripts/verify_browser_artifact.py scripts/record_browser_scroll.py
```

## 常見問題

### Playwright 找不到 Chromium

```bash
playwright install chromium
```

### WebGL 在 VPS / headless 黑畫面

腳本已包含：

```text
--enable-webgl
--ignore-gpu-blocklist
--enable-unsafe-swiftshader
```

如果仍失敗，要把 verdict 降到 partial / blocked，不要假裝 WebGL 已驗證。

### Vite / Next 專案不能用 static serve

不要直接用 Python static server serve source repo。先跑：

```bash
npm run dev
# or
npm run build && npm run preview
```

再用 `ARTIFACT_URL` 指向正在跑的網址。
