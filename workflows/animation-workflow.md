# Animation Workflow — Directed Motion + Official Three.js

## 目標

先講清動畫服務甚麼結果，再揀最細足夠 lane／technology。Library 數量、
shader、particles、bloom、3D 同長 timeline 都唔係品質分數。

每段 motion 至少要服務一項：feedback、orientation、continuity、causality、
hierarchy、progress、story 或 emphasis。冇工作就刪。

## 1. Lane

- Micro Motion：hover、focus、press、短 feedback。維持 Tiny／Normal，
  只需比例化 changed-state、temporal 同 reduced check。
- Choreographed Motion：
  - UI Motion：modal、menu、route、layout/state transition；
  - Scroll Story：章節、pin、reveal、scroll-linked敘事。
- Cinematic WebGL：camera、depth、space、shader、可環繞 object 或 3D world
  本身係結果必要部分。

Choreographed／Scroll Story／Cinematic 使用完整 Motion evidence profile。
高級感唔等於 WebGL；CSS／WAAPI／Motion 做到就唔升級。

## 2. Motion inventory

每段 sequence 記：

    Element/state:
    Job:
    Trigger:
    Start / representative middle / settled or exit:
    Focal point:
    Owner and exact property:
    Interruption / rapid repeat / route change:
    Mobile alternative:
    Reduced-motion alternative:
    Cleanup:
    Required proof:

Delete job 只係「唔好咁靜」「睇落高級」嘅 item。

## 3. Scene / Technical Lock

Cinematic WebGL 先記：

    Scene input: verbal | image | mixed
    Subject/world:
    Required viewpoints:
    Camera freedom, bounds and reset:
    Silhouette/composition:
    Material/light/mood:
    Main spatial interaction:
    Host stack and installed Three.js version:
    Mobile quality tier:
    Loading/fallback/reduced states:
    Generated-asset permission and rights:
    Resource/performance budget:

圖片只鎖可見事實；未知側背面要明示建模假設。聲稱 full orbit／完整 object，
就要真 geometry 同可信 side/back；billboard、旋轉卡、2.5D parallax 或只喺
原角度成立嘅假景唔算。

## 4. Technology and official source

Cost ladder：

| Need | Prefer |
|---|---|
| focus／hover／pressed／短 reveal | CSS |
| 可 reverse／cancel／seek DOM transition | Web Animations API |
| React layout／gesture／state | Motion（如 project 已使用或成本合理） |
| pinned／scrubbed complex DOM story | GSAP + scoped cleanup |
| camera／geometry／material／shader／spatial input | Three.js |
| locked cinematic pixels | native video/image sequence |

Three.js authority：

1. 先讀 host project package/lock，確認 exact installed version。
2. API authority 係對應版本嘅官方
   [mrdoob/three.js](https://github.com/mrdoob/three.js) source、manual、
   API docs 同 examples。
3. Audited baseline 係 r185 tag
   cb3b077ee63818a8cc1ab273f08704d89b8ac492；2026-08-28 npm current
   observed 為 three 0.185.1。呢個紀錄唔係強制升級。
4. 如本機有 threejs-cinematic-motion，先用佢做 scene/lifecycle/evidence
   director；再按當前問題讀最多 1–3 個 official-source topic skills：
   threejs-fundamentals、geometry、materials、lighting、textures、animation、
   loaders、shaders、postprocessing、interaction。
5. 唔一次載入全部。官方 source 同 executable evidence 高於任何 Skill。

Machine-readable provenance 見
[THREEJS_SOURCE_LOCK.json](../included-skills/THREEJS_SOURCE_LOCK.json)。

## 5. Ownership

同一 element/property 同一時間只准一個 owner：

- CSS：focus、hover、tiny feedback；
- Motion：component／layout transition；
- GSAP：DOM scroll timeline／long sequence；
- Three.js：scene object、camera、material、shader、spatial interaction。

唔准多套系統搶 transform、opacity、scroll position、camera 或 timeline。
Owner 同時負責 setup、refresh、interrupt、route/unmount cleanup。

## 6. Choreography

Choreographed／Cinematic 開工前鎖：

1. Motion direction：觀眾要理解／感受到嘅改變；
2. Beat sheet：trigger、enter、active、settle/exit、mobile、reduced；
3. Timeline：每個 beat 對 time、progress 或 event 嘅 start/mid/end。

診斷次序：

    ownership/lifecycle -> choreography/causality -> timing polish

冇該層就 skip，唔為「完整」創造三層工作。

## 7. Cinematic build order

1. HTML/content、loading 同 static fallback；
2. silhouette、composition、subject scale；
3. camera/world scale、orbit bounds、reset；
4. geometry completeness；
5. lighting/material/texture causality；
6. primary action、pointer/touch；
7. mobile tier、reduced motion、fallback；
8. post-processing 最後。

先令世界成立，再加氣氛。ImageGen 只填 named gap；記用途、尺寸、prompt、
後處理、provenance、rights，唔可以改寫 scene lock 或冒充 geometry。

## 8. Lifecycle、performance、energy

- Continuous motion 用一個 delta/time source，唔用 high-frequency framework state。
- Cap pixel ratio／drawing buffer；lazy-load heavy scene並預留 layout。
- Scene idle 時 render on demand；hidden tab／offscreen／reduced 狀態停止 work。
- Dispose controls、listeners、observers、RAF、mixer、geometry、materials、
  textures、render targets、decoder/cache ownership。
- Route mount/unmount/return 做 10 cycles（complex runtime），resource count
  唔可以累積。
- Heavy scene 記 delivered JS/model/texture bytes、draw calls、renderer.info、
  long tasks／interaction latency 同 named mobile device/tier。

## 9. Reduced motion

唔係將 duration 變 0.01s：

- 移除 parallax、large translate、zoom、spin、camera flight、ambient loop；
- 保留 state、hierarchy、progress、feedback、focus、result 同 action；
- canvas/video 提供 poster／static scene；
- 驗真 OS/browser preference。

自動 movement 超過五秒且同其他內容同時出現，按適用 accessibility contract
提供 pause/stop/hide；唔超過安全 flash rate。

## 10. Temporal evidence

### Micro

- before／active／after changed-state；
- keyboard/focus/touch state（如適用）；
- reduced alternative；
- console/page errors。

### Choreographed / Scroll

- start／mid／settled，同 reverse/cancel；
- real scroll 同 rendered progress 同步；
- resize、fast scroll、anchor、route re-entry；
- 6–12 秒 WebM/MP4 或等值真時間 record + contact sheet。

### Cinematic WebGL

- start／mid／settled；
- front／side／back／代表 high-low view（full-orbit claim）；
- occlusion、clipping、near/far、reset、pointer/touch；
- loading/error、fallback、reduced、mobile tier；
- renderer/resource before-after cycles 同 performance trace。

Temporal evidence 要證明 start/mid/end visibly distinct、唔黑畫面、唔停喺第一
frame、唔由 fake progress hook 代替 real scroll。Raw media 落檔；root
conversation只開 contact sheet加一張 focal frame。

## 11. Review / verdict

Public／flagship complex motion 用一個 fresh independent evaluation batch，
只修最高影響 root cause，一次 recapture後停。更多主觀迭代需要新 user
direction 或新 objective failure。

Terminal vocabulary：

    PASS / PARTIAL / FAIL / WAITING_FOR_NOVA

Runtime exception、failed required asset、unexpected context loss係 issues，
映射 PARTIAL／FAIL；blocked 唔係 runtime defect 嘅代名詞。

PASS 需要：motion job、single owner、static/reduced、interruption、mobile、
lifecycle、temporal evidence、performance/resource 同 scene/viewpoint claim
全部成立。Build pass、animation-name 或 still screenshot 唔足夠。
