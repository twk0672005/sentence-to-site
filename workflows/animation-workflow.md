# Animation Workflow — Directed Motion + Locked Three.js Router

## 目標

先決定動畫服務甚麼結果，再選最細足夠lane與技術。Three.js係WebGL技術主力；導演判斷、內容層級、accessibility、browser evidence及停手條件仍由workflow負責。

每段動畫至少要做到一項：建立情緒、推進故事、表示狀態、引導注意力或增加可信度。做唔到就刪。

## 1. 揀lane

- **Micro Motion**：hover、focus、press、短feedback。
- **Choreographed Motion**：有開始、發展和結束的編排；再標明子類：
  - `UI Motion`：modal、menu、route、state transition；
  - `Scroll Story`：章節、pin、reveal、視覺敘事。
- **Cinematic WebGL**：相機、深度、空間、粒子、可環繞場景或3D世界本身係主角。

高級感不等於WebGL。CSS／Motion做到就唔升級；只有空間或相機係結果必要部分先用Three.js。

## 2. 場景輸入與鎖定

`Cinematic WebGL`可由三種輸入開始，參考圖並非必需：

```text
Scene input: verbal-brief | image-reference | mixed
Scene lock: <主體／世界、需要展示的視角、相機自由度、材質／光／情緒、必保留／避免、真實度、生成資產許可>
Technical lock: <host stack、three版本、選中skills、ThreeUI元件、source commits、fallback>
```

- **口頭描述**：按已鎖定世界觀、構圖、材質、光線和interaction評估；唔聲稱還原一張不存在嘅圖。
- **參考圖片**：拆解輪廓、尺度、前中後景、遮擋、材質、光向、鏡頭和未知側背面；未知處明示為合理建模假設。
- **混合**：圖片鎖可見事實，文字補充用途、情緒、看不到的空間和互動。

如需要完整可環繞展示，必須建立真3D geometry、camera orbit及側背面；旋轉一張卡、2.5D parallax或只在原視角成立的假景唔算。

## 3. 概念參考與ImageGen

視覺、介面或journey方向未具體，或用戶要求旗艦質感時，可讀 `refero-inspiration.md`。Product UI screens／flows只補UI結構、狀態和interaction；Refero Styles只補排版、palette、spacing、material和motion語言。最多比較三個候選，指定一個primary source，再鎖一套原創方向。參考圖或已接受baseline永遠優先；Refero不可改寫scene silhouette、subject、camera intent或已命名材質。

不可自動scrape／crawl Refero public pages；agent自動研究只走獲批准的官方MCP／API。未批准登入、安裝、付款或外部上載時，使用用戶提供的候選或human-led shortlist。

ImageGen只填已命名的缺口，例如environment plate、天空、貼圖基底、decal、mask、illustration或UI supporting visual。每個生成資產要記錄用途、尺寸、prompt、後處理、來源及權利狀態。生成結果唔可以靜默改寫scene lock；面向鏡頭的單張生成圖亦唔可以冒充完整3D。

## 4. Three.js技術Router

真Three.js工作先讀 `threejs-fundamentals`，再按當前階段加最多1–3個專項；下一階段只有出現新需要先加。禁止一次載入全部skills。

| 實際需要 | 選擇 |
|---|---|
| scene、camera、renderer、resize、render loop | `threejs-fundamentals` |
| silhouette、mesh、BufferGeometry、instancing | `threejs-geometry` |
| PBR、transparency、surface response | `threejs-materials` |
| lights、shadows、HDR environment | `threejs-lighting` |
| image maps、UV、color space、compression | `threejs-textures` |
| keyframes、mixer、skeletal／morph animation | `threejs-animation` |
| GLTF、DRACO、KTX2、external assets | `threejs-loaders` |
| GLSL／自訂視覺計算 | `threejs-shaders` |
| bloom、DOF、grading | `threejs-postprocessing`，只可在構圖／光材質已成立後 |
| raycast、pointer、orbit、touch controls | `threejs-interaction` |
| FPS、draw calls、memory、mobile tier | browser profiling／evidence gate；main冇獨立performance skill |
| WebGPU／TSL／R3F-specific stack | CloudAI-X main冇專項；只有任務明確需要時先查官方stack文件，唔借用open PR skill |

### ThreeUI

ThreeUI係可選元件來源，唔係圖片／文字自動變3D世界嘅引擎。只有元件直接符合scene或interface lock時先用：先search，記錄component ID、`sourceCommit`、registry SHA及檔案hash，再以expected commit安裝。冇適合元件就直接建，唔為咗用元件庫而改concept。

### 來源鎖

- Stable technical set：`CloudAI-X/threejs-skills` main commit `b1c623076c661fc9b03dac19292e825a5d106823`。
- Stable API target：official Three.js `r185`／`three@0.185.0`；官方docs和實跑證據高於skill文字。
- Upstream目前冇repo LICENSE檔及GitHub license identification；公開kit只記索引和commit，唔複製其正文。
- PR #13、#14、#15全部不採用；workflow只用已鎖定main，亦唔私下安裝PR新增skill。
- main內兩個已核實無效例子——`ContactShadows.js`及`three/addons/nodes/Nodes.js`——禁止使用；按official r185 docs或可執行證據重建。
- 全部來源禁止自動跟branch更新。轉commit前要重新審核、備份、更新lock及驗證。

詳細機器可讀資料見 `included-skills/THREEJS_SOURCE_LOCK.json`。

## 5. Motion ownership

同一元素同一時間只准一個motion owner：

- CSS：simple hover／focus／tiny transition；
- Motion：component／layout transition；
- GSAP：scroll timeline、長sequence、複雜編排；
- Three.js：scene內物件、camera、shader及spatial interaction。

唔准CSS、Motion、GSAP同時搶同一transform。每段sequence要有trigger、outcome、states、cleanup、mobile alternative及reduced-motion alternative。

## 6. Choreographed／Cinematic 準備與實作層

Micro Motion 只需短行為定義；Choreographed 或 Cinematic 開工前先鎖三樣：

1. **Motion direction**：觀眾要感受到甚麼變化，動畫服務哪個內容結果；
2. **Beat sheet**：每個節點的 trigger、enter、active、exit／settle、mobile alternative、reduced-motion alternative；
3. **Timeline**：用 progress、時間或事件定義每個 beat 的 start／mid／end，避免只靠主觀「大概順」。

實作分三層，按次序向下：

1. **Architecture**：motion owner、state／progress source、listener／render loop、cleanup；
2. **Scene choreography**：文字、主體、相機／構圖和視覺因果的先後；
3. **Timing polish**：duration、easing、stagger、settle與微調。

上層未成立，不可用下層 polish 掩飾。每層只修當前最高影響力問題；唔為完整而循環重做三層。

## 7. Cinematic建造次序

1. silhouette／構圖／主角；
2. camera、world scale及環繞邊界；
3. lighting／materials／textures；
4. 因果主動作；
5. interaction、touch及reset；
6. loading、fallback、mobile quality tier；
7. 最後先post-FX。

先令世界成立，再加氣氛。粒子、bloom、shader或3D唔係高級感保證。

## 8. 真browser驗證

Animation claim需要時間證據，唔係單張截圖：

- start／mid／settled或完整orbit viewpoints；
- desktop／mobile及touch；
- 側背面、occlusion、clipping、near／far、resize；
- loading、fallback、WebGL errors、failed requests；
- reduced motion及弱裝置tier；
- FPS、draw calls、memory或同等performance readback；
- cleanup後冇重複listener、timeline或animation loop。

## 9. 高級公開級Review：只做一次

要求「無可挑剔／公開發布」時，用 `high-end-public-review.md`完整100分制度一次。3D overlay要特別檢查360°完整度、幾何輪廓、材質與光、orbit控制、touch、reset、loading、fallback及穩定性。

流程：最強初稿 → fresh evidence → 一次評分 → 只修最高影響力一刀 → 重驗 → 停手並問用戶效果。唔review自己嘅review；未達標就按低分項提供最多四個選項，收到用戶方向先開下一輪。

`public-ready production candidate`不等於已獲授權部署、公開、付款或對外發布。

## 10. 停手與交付

- Micro／Choreographed prototype：route要求的真時間證據齊，或誠實標記`partial`／`blocked`後停手；
- Public：一次正式Review、最多一刀同路線修正及受影響證據重驗後停手，交回用戶判斷；
- 交付先展示可見artifact，再講lane、motion owner、browser evidence、mobile／reduced-motion狀態及已知限制；
- 唔因為agent自己仍可想到效果，就新增timeline、post-FX、WebGL、evaluator或下一輪。
