# Evidence Scoring

這份用來判斷一個網站 / 動畫工作流是 `pass`、`partial` 還是 `blocked`。

## Pass

可以講 pass 的條件：

- Desktop screenshot 有正確畫面
- Mobile screenshot 有正確畫面
- title / H1 / key marker 對得上現專案
- console errors = 0
- page errors = 0
- primary CTA / nav / upload / main flow 已測（如適用）
- 如果是動畫：有 MP4 / GIF，並且 contact sheet 顯示確實有轉場
- 如果是 WebGL：`webglOk=true` 或 fallback 有清楚標示且符合任務要求

## Partial

應該講 partial，不要講完成：

- desktop 正常，但 mobile first fold 弱
- 有 screenshot，但未有 animation video
- video 有，但無 contact sheet 或未檢查是否黑畫面
- console warnings 存在但不阻塞，需要列明
- WebGL fallback 可用，但真正 WebGL 未跑起
- flow 能跑，但 proof / trust / CTA 還弱
- script 驗證只覆蓋 static artifact，未覆蓋實際 dev server

## Blocked

應該講 blocked：

- app 開不起
- build / dev server 起不到
- browser 不能打開或一直 timeout，且無替代 Chromium / Playwright 證據
- missing dependency 無法安裝
- 需要 API key / model / data，但目前沒有
- public preview 被 tunnel / login / interstitial 擋住
- ZIP 壞、亂碼、或包含 secret

## Console warnings 怎樣處理

| 情況 | Verdict |
|---|---|
| deprecation warning，不影響畫面 | partial or pass with note |
| failed image / font affecting visual | partial |
| uncaught exception | blocked |
| WebGL context lost | blocked unless fallback is expected and verified |

## Animation evidence 判斷

MP4 存在不等於 animation pass。

要看：

- 開頭是否正確
- 中段是否有狀態變化
- 結尾是否到達目標狀態
- 不是黑畫面
- 不是只有第一 frame
- 不是 query progress 改了但頁面 scroll 沒同步

## 最後一句 verdict 格式

```text
Verdict: pass / partial / blocked
Reason: <一句人話>
Evidence: <screenshots / video / readback path>
Next: <只講下一刀>
```
