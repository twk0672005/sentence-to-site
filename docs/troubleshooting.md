# Troubleshooting

## HTTP 200 但畫面是舊專案

原因：用咗外部dev server但identity marker錯，或舊工具曾靜默重用被佔port。

處理：

1. 檢查 title / H1 / body marker。
2. Static mode用`ARTIFACT_PORT=0`；指定port被佔時新版script會fail。
3. 重新截圖。
4. 設`TITLE_CONTAINS`／`H1_CONTAINS`／`BODY_CONTAINS`，不要只信 HTTP 200。

## Static root 被拒絕

原因：ARTIFACT_ROOT係source repo，含`.git`、`.env`、private key或symlink。

處理：先用target project真build command產生sanitized dist／out／build，將
ARTIFACT_ROOT指去該輸出。唔好為通過而關閉安全檢查。

## Screenshot 是 fallback，不是真 WebGL

處理：

- 檢查 `window.__COSMIC_ZOOM_STATUS__` 或 `window.__APP_STATUS__`。
- 檢查 `webglOk`。
- 隔離、可信artifact可明示`ENABLE_SWIFTSHADER=1`；呢個只係software
  renderer evidence，唔係production GPU proof。
- 如果 WebGL 不可用，要明確標示 partial / blocked。

## WebM／MP4 有檔案但看不到動畫

處理：

- 生成 contact sheet。
- 看 top / mid / final frame。
- 檢查是不是只錄到 loading 或黑畫面。
- 如有 scroll-driven scene，要確保 real scroll 與 animation progress 同步。

`PROGRESS_ADAPTER=app/cosmic`只係explicit diagnostic hook；default none。
Hook令畫面郁唔證明real scroll wiring正常。

## 冇 FFmpeg

Motion script仍會交WebM、start/mid/settled同contact sheet。只有交付契約
硬性需要MP4先設`REQUIRE_MP4=1`，再按OS安裝ffmpeg／ffprobe。

## Telegram 看不到中文 Markdown

中文長文要另給：

- PDF
- UTF-8 BOM TXT

Markdown 可以保留，但不要作唯一手機閱讀格式。
