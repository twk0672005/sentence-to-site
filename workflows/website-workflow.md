# Website Workflow — Truthful Evidence Core

## 目標

將一句描述、reference、mixed brief 或現有網站，直接收斂成一個可用、
可信、responsive、可驗證嘅網站成果。流程服務成品，唔用角色、框架、
effect、檔案數或 checklist 數量扮進度。

## 1. Result Lock

Tiny 修正可用一行；Normal 以上先記 compact lock：

    Base route: new-site | existing-site
    Work depth: tiny | normal | serious | redesign
    Experience lane: static | ui-motion | cinematic-webgl
    Delivery intent: prototype | public-candidate
    Visual source: direct-build | reference-locked | shared-canvas
    Five-second message:
    Primary action:
    Trust proof:
    Protected baseline:
    Required evidence:
    Stop condition:

- Tiny：一個客觀局部修正，只驗受影響狀態。
- Normal：一頁／component，compact contract + wide/narrow render。
- Serious：公開、賣畀客、跨頁、reference-led 或 trust-sensitive。
- Redesign：Serious + baseline comparison + preservation map。

Public-candidate 唔等於已獲授權 deploy、publish、付款或帳戶操作。

## 2. Authority、現況與保留

新站只讀 brief、素材、輸出格式同真正 command source。現有站先確認：

- current request、最近 project instructions 同 active route；
- browser 實際載入嘅 HTML、styles、scripts、assets；
- framework、entry、content、state、motion owner 同 dependencies；
- project README／package／CI 提供嘅 run、build、test、preview commands；
- desktop/mobile baseline、primary flow 同主要 error/loading/cached/back states。

唔靠檔名估 active page，亦唔因「可能有用」掃完整 repo。

### Product truth trace

每個 visible promise 追到真正結果：

    copy/control -> route -> category/state -> API/data -> engine/decision -> output

Generic label 唔可以靜默行入更窄 domain；fallback 唔可以冒充成功；
live、cached、loading、missing、error 文案必須講真狀態。

### Preservation map

Existing-site／Redesign 寫四欄：

- PRESERVE：route、API、data、event、selector、state、accessibility、SEO、
  privacy、analytics 同已接受 visual behavior；
- EVOLVE：今次真係要改善嘅 owner；
- RETIRE：有證據可以退出嘅舊層；
- DECISION：只有用戶／產品 authority 可以拍板嘅項目。

未完成 preservation map，唔做全頁 reset。

## 3. Concept / Design Lock

只有頁面結構、journey 或視覺語言真係未定義，先讀
[refero-inspiration.md](refero-inspiration.md) 做一次有界研究：

- Product UI：page anatomy、flow、states、feedback；
- Styles：type、palette、spacing、shape、material、motion；
- mixed：兩類 gap 同時存在，但仍指定一個 primary source。

最多三個候選、一個 primary；secondary 只填一個 named gap。Supplied
reference、產品 truth 同 strongest accepted baseline 高於研究來源。
抽規則，唔抄品牌、文案、資產、專有字體、完整 flow 或 trade dress。

Design lock 至少決定：composition thesis、產品專屬 signature、內容層級、
type roles、colour logic、space/shape/material、imagery、desktop/mobile
recomposition、state truth、motion decision 同 Do/Avoid。

ImageGen 只填已命名 asset gap。記錄用途、尺寸、prompt、後處理、來源同
rights；生成資產唔可以靜默改寫 design/scene lock。

## 4. Static-first implementation

1. 先用真內容 graybox 五秒訊息、proof、CTA 同 reading order。
2. 建 semantic HTML、labels、error/help text、loading/empty/success states。
3. 建最少足夠 tokens 同 owner；唔用 tail override 掩住兩套 theme。
4. 完成 keyboard order、visible focus、contrast、target size 同 reflow。
5. 先令 mobile/desktop 各自成立，再加 imagery、motion 或 3D。
6. 保留現有 stack；唔為設計問題換 framework 或加無必要 dependency。

一個完整 visible slice 好過五個半完成 section。

## 5. Responsive art direction

對每個 target width 主動決定：

- priority、order、line length、type role、density；
- navigation/control model、touch target；
- table、canvas、instrument 等密集資料點樣分層；
- 邊啲保留、摘要、延後或 progressive disclosure；
- asset、motion 同 resource budget。

Mobile 唔係 desktop 縮細或全部直向堆疊。Essential information 同 action
必須一致，但 composition 可以唔同。

## 6. Motion decision

- static 已經清楚：停喺 static。
- feedback、state、route 或 scroll story 有真工作：進入 ui-motion。
- camera、depth、space 或 explorable world 係結果必要部分：
  先讀 [animation-workflow.md](animation-workflow.md)，再進入 cinematic-webgl。

高級感唔係 WebGL 理由。每項額外技術都要回答：移除後，鎖定結果會否
明顯失效？否則唔加。

## 7. Browser evidence

用 [evidence-gate.md](evidence-gate.md) 揀比例化 coverage，唔用 HTTP 200、
build exit 0 或 screenshot existence 冒充完成。至少按 scope 驗：

- route identity：URL、title、H1、key marker、loaded owner；
- desktop/mobile；Serious/Redesign 再驗 320px／zoom-reflow；
- primary CTA、navigation、form、keyboard/focus 同 state matrix；
- console、page、critical failed request、asset、overflow/clipping；
- visible text、minimum size、contrast、target size；
- reduced motion；有 motion 再加真 temporal evidence；
- cross-route identity、content、navigation 同 state parity。

所有 raw screenshot、video、HTML、JSON 同 trace 落檔，receipt 綁 path、
bytes/hash、viewport/state 同 capture time。

## 8. Session budget

- Root conversation 每個 material repair round 通常只開一張 wide 同一張
  narrow／changed-state 圖；其餘由 path、hash、metrics 同 evaluator receipt
  證明。
- 唔 inline base64、完整 HTML、大型 JSON 或整份 tool transcript。
- Default 最多一批 bounded discovery helpers 同一個 fresh evaluator；
  reuse helper，長 wait 一次，唔密集 polling。
- Existing task 已有兩次 compaction、約 20MB payload 或 16 個 inline image
  results時，完成 atomic stage、寫 compact handoff，轉 fresh task先開始下一個
  evidence-heavy stage。唔改寫／刪 session history。

呢個係 transport budget，唔係降低 QA。

## 9. Review and repair

- Tiny：changed-state readback；唔開 numeric rubric/evaluator。
- Normal：fresh rendered critique，修最高影響 root cause。
- Serious/Redesign：fresh independent evaluator，最多列三個 root causes。
- 明確 high-end／flagship／public-quality：再讀
  [high-end-public-review.md](high-end-public-review.md)。

Default 只有一個 independent evaluation batch 同一個 bounded repair batch。
先修可見影響最大嗰一刀，重驗受影響證據同 regression，然後停。新一輪
主觀方向需要用戶新輸入或新 objective failure，唔 review 自己嘅 review。

## 10. Verdict / handoff

Terminal vocabulary 只有：

    PASS / PARTIAL / FAIL / WAITING_FOR_NOVA

- PASS：scope contract、protected behavior、required evidence 同 judgement 全綠。
- PARTIAL：有可用結果，但 required evidence 或品質仍有 issues/not-run/blocked。
- FAIL：bounded repair 後，primary flow 或成果仍不可接受。
- WAITING_FOR_NOVA：只有 authority、rights、secret、account、payment、
  publish/deploy 等真正 Nova-only 決定。

Runtime exception、broken asset、unexpected WebGL loss 係 issues，最後映射
PARTIAL／FAIL；唔好叫 blocked。

交付只講：可見成果、點用、fresh evidence、changed paths、已知限制、
rollback 同真正需要用戶決定嘅下一步。
