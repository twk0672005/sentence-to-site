# Troubleshooting

## HTTP 200 但畫面是舊專案

原因：port 被舊 server 佔用。

處理：

1. 檢查 title / H1 / body marker。
2. 換乾淨 port。
3. 重新截圖。
4. 不要只信 HTTP 200。

## Screenshot 是 fallback，不是真 WebGL

處理：

- 檢查 `window.__COSMIC_ZOOM_STATUS__` 或 `window.__APP_STATUS__`。
- 檢查 `webglOk`。
- VPS/headless 可試 SwiftShader。
- 如果 WebGL 不可用，要明確標示 partial / blocked。

## MP4 有檔案但看不到動畫

處理：

- 生成 contact sheet。
- 看 top / mid / final frame。
- 檢查是不是只錄到 loading 或黑畫面。
- 如有 scroll-driven scene，要確保 real scroll 與 animation progress 同步。

## Telegram 看不到中文 Markdown

中文長文要另給：

- PDF
- UTF-8 BOM TXT

Markdown 可以保留，但不要作唯一手機閱讀格式。
