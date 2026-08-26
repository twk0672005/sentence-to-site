# Website Workflow — Clean Result Core

## 目標

將口頭描述、圖片、混合brief或現有網站，收斂成一個可用、可信、responsive、可驗證的網站成果。流程服務成品，不為完整而加角色、工具、框架或效果。

## 1. 鎖定結果

開始前用最短紀錄鎖定：

```text
Base route: new-site | existing-site
Experience lane: static | ui-motion | cinematic-webgl
Delivery gate: prototype | public
Visual source: direct-build | reference-locked | shared-canvas
Five-second message: <訪客第一眼明白甚麼>
Primary action: <主要行動>
Protected baseline: <不可倒退部分或 n/a>
Required evidence: <固定清單>
Stop condition: <固定條件>
```

有參考圖時，列出必須還原的構圖、層級、物件、材質和禁止漂移項；只有口頭描述亦可直接開始，以明示假設補足可逆細節。

## 2. 概念與視覺方向

當口頭brief嘅視覺、頁面結構或用戶旅程資訊不足，或用戶要求高級／旗艦／公開級成品時，讀 `refero-inspiration.md`，先講清楚未解決的是哪一種問題：

- `Product UI`：參考真實screens／flows，抽取page anatomy、hierarchy、states、feedback和interaction sequence；
- `Refero Styles`：抽取visual premise、palette角色、字體行為、spacing、shape、material、motion與Do／Avoid；
- `mixed`：只在結構與視覺語言同時未定義時使用，仍須指定一個primary source及secondary只填一個named gap。

最多比較三個候選，然後綜合成一套原創design lock再實作。參考圖或現有網站最佳baseline高於Refero；Refero只補空白，不可推翻已接受方向，亦不可複製品牌、文案、圖片、商標、專有字體、完整flow或整份DESIGN.md。

Refero public web UI不可自動scrape／crawl／bulk-download。需要agent自動研究只可使用獲批准的官方MCP／API；安裝、登入、升級、付款、外部上載或付費方案一律先獲批准。未有官方programmatic access時，只用用戶提供的候選連結／截圖或human-led shortlist。

## 3. 讀必要現況

新網站只讀brief、素材和輸出要求。現有網站只讀入口、框架、styles、主要頁面、動畫擁有權、部署方式和最強baseline。不要因為可能有用就掃完整repo或重寫架構。

## 4. 揀最細足夠路線

- `static`：內容、層級、排版及CTA已足夠。
- `ui-motion`：狀態、焦點、轉場或scroll敘事有實際工作。
- `cinematic-webgl`：深度、空間、相機或可環繞場景本身承載故事；唔係因為「高級」兩個字就啟用。

每項額外技術必須回答：如果移除，已鎖定結果會否明顯失效？否則不加。

## 5. 實作次序

1. 先完成五秒訊息、可信度、主要CTA及responsive結構；
2. 做一個完整可見slice；
3. 先修層級、構圖、字體、spacing和內容，再加motion或3D；
4. 只喺有明確素材缺口時用ImageGen；記錄prompt、用途、來源及生成資產，唔准藉生成改寫設計鎖；
5. 保護最強baseline，避免為統一而整頁重寫。

## 6. 真瀏覽器驗證

Build成功、HTTP 200或單張hero圖都唔等於完成。按route驗證：

- desktop與mobile首屏、完整頁面及主要流程；
- CTA、navigation、form、keyboard/focus與相關狀態；
- console、page errors、failed requests及overflow；
- motion要有多狀態或MP4；
- WebGL要驗start／mid／settled或環繞視角、側背面、遮擋、loading、fallback、reduced motion及mobile tier。

## 7. 高級公開級Review：只做一次

當用戶要求「無可挑剔／可以公開發布／旗艦級」，讀 `high-end-public-review.md`，用完整100分制度做一次正式審美與體驗評分：

- Design 40；
- Usability 30；
- Creativity 20；
- Content 10；
- technical、accessibility、rights和WebGL完整性另設不可被總分抵銷的硬閘。

流程固定為：

```text
最強初稿 → fresh browser evidence → 一次完整評分
→ 只修最高影響力的一刀 → 重驗受影響證據 → 停手
→ 詢問用戶是否達到效果
```

不得再review自己嘅review。若用戶答未達到，按最低分維度追問具體落差，並提供最多四個相關選項；收到選擇後先開下一輪。

`public-ready production candidate`需要：冇硬閘失敗、總分至少88、Design至少34/40、Usability至少25/30；「無可挑剔／旗艦」以92分為目標。呢個狀態唔等於獲授權deploy或公開發布。

## 8. 停手與交付

Prototype在證據齊或誠實標記`partial`／`blocked`後停。Public在一次正式Review、一刀修正及重驗後停並詢問效果。唔開無限優化、唔自動加Agent、evaluator或新工具。

交付只講：成果、使用方式、證據、評分、已知限制與需用戶決定事項。公開部署、付款、帳戶操作及對外發布仍須先批准。
