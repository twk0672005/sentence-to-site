# Evidence Reference — Conditional

本文件只在交付風險較高、互動較多、動畫時間性明顯，或需要正式 handoff 時按需使用。普通小改動唔需要跑晒全部項目。

## 比例化證據

| 任務 | 建議最低證據 |
|---|---|
| 普通 landing page 小改 | 一個主要 viewport 真畫面 + title/H1/CTA + 無阻斷錯誤 |
| Responsive／互動改動 | desktop + mobile + 主流程 smoke |
| WebGL／重動畫 | 關鍵時間格 + 短片 + console/WebGL readback |
| Reference recreation | reference 與新 artifact 對照 + 一句差距判斷 |
| ZIP／handoff | ZIP integrity + README／入口 readback |

只檢查與今次 claim 有關嘅層。HTTP 200 唔證明畫面、build 唔證明 runtime、檔案存在唔證明交付。

## 狀態用語

- `pass`：今次承諾嘅範圍有新鮮證據支持；
- `partial`：有可用結果，但明確缺一層；
- `blocked`：缺工具、資料、權限或真實 runtime；
- `next batch`：今批完成，下一層係新 scope，唔假扮同一批未完。

禁止用「應該 OK」或「我覺得完成」代替證據。證據只係支援判斷，唔係越多越高質。
