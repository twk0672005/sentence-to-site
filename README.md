# Afuu Website + Animation Workflow Kit

**Version:** v1.3.3 — Clean Result Core
**Purpose:** 用最少流程做出可見、可驗證、可交付嘅網站／動畫作品。

這是一個 workflow 參考包，不是 starter app、身份檔案或 Hermes 安裝包。

## 先讀這裡

日常任務只需要：

```text
1. README.md
2. workflows/website-workflow.md 或 workflows/animation-workflow.md
3. 真正需要時才讀 specialist reference / included skill
```

不要預設讀完整 file architecture、maintenance map、全部 prompts 或全部 included skills。

## 核心 Workflow

```text
鎖定可見結果
→ 看必要現況與 strongest accepted baseline
→ 只有概念真空白時做一次有界參考研究
→ 選最細足夠 lane
→ 做一個真正有用的 visible slice
→ 在 browser / real media 驗證
→ 同範圍 repair 或停手交付
```

## 兩條 Workflow 點樣配合

網站 Workflow 負責頁面目標、內容層級、視覺方向、主要行動、responsive 結構、browser QA 同交付邊界。動畫 Workflow 只在 movement 真係服務情緒、故事、狀態或注意力時加入，唔會因為「高級」而自動升級。

```text
Website Workflow
├─ static：內容、層級、排版與 CTA 已足夠
├─ ui-motion：按需要進入 Micro 或 Choreographed Motion
│  ├─ UI Motion：modal、menu、route、state transition
│  └─ Scroll Story：章節、pin、reveal、視覺敘事
└─ cinematic-webgl：進入 Cinematic WebGL
```

網站 Workflow 擁有「做甚麼」同「何時算完成」；動畫 Workflow 擁有「點樣郁」同「點樣證明時間體驗成立」。

## 網站 Workflow：流程架構

完整執行規則見 [`workflows/website-workflow.md`](workflows/website-workflow.md)。

### 整體流向

```text
Brief / reference / existing site
→ Result Lock
→ 必要時做一次有界參考研究 → Original Design Lock
→ 讀必要現況與 strongest accepted baseline
→ 選最細足夠 experience lane
→ 建造一個完整 visible slice
→ 真瀏覽器驗證
→ Public／旗艦任務先做一次 bounded review → 最多修一刀
→ Stop / handoff
```

### 開工決策 Contract

| 決策 | 可選值／要回答的問題 |
|---|---|
| Base route | `new-site` 或 `existing-site` |
| Experience lane | `static`、`ui-motion` 或 `cinematic-webgl` |
| Delivery gate | `prototype` 或 `public` |
| Visual source | `direct-build`、`reference-locked` 或 `shared-canvas` |
| Five-second message | 訪客第一眼要明白甚麼？ |
| Primary action | 訪客最重要的下一步係甚麼？ |
| Protected baseline | 邊部分已經成立，絕對唔可以倒退？ |
| Required evidence | 今次完成聲稱需要甚麼真實證據？ |
| Stop condition | 去到邊個可驗證狀態就停手？ |

### 8 個階段

| 階段 | 核心動作 | 可見輸出 |
|---|---|---|
| 1. Result Lock | 鎖定目標用戶、五秒訊息、主要行動、route、lane、證據與停手條件 | 一份短而明確的 execution contract |
| 2. Concept / Design Lock | 只有結構或視覺語言未定義時，最多比較 3 個候選；抽取規則後綜合成原創方向 | Page anatomy、hierarchy、palette、type、spacing、material、motion 的 Do／Avoid |
| 3. Current-state intake | 新站只讀 brief、素材與輸出要求；現有站只讀入口、框架、styles、主要頁面、motion ownership、部署與最佳 baseline | 最少但足夠的 repo／artifact 理解 |
| 4. Route selection | 選 `static`、`ui-motion` 或 `cinematic-webgl`；額外技術必須對已鎖定結果有必要性 | 一條最短可行路線 |
| 5. Visible slice | 先完成訊息、可信度、CTA、responsive 結構，再修層級、構圖、字體、spacing，最後先加 motion／3D | 一段完整、可見、可操作的成品 |
| 6. Browser evidence | 驗 desktop／mobile、CTA、navigation、form、keyboard、console、failed requests、overflow；motion／WebGL 補時間與狀態證據 | Fresh screenshots、readback、keyframes／MP4 與錯誤狀態 |
| 7. Bounded review | 只限 public／旗艦要求：做 1 次完整評分，只修最高影響力 1 刀，再重驗受影響證據 | 一次有界 quality pass，唔進入無限 review loop |
| 8. Stop / handoff | 證據齊就停；未齊則誠實標記 `partial`／`blocked` | Artifact、使用方式、證據、限制與待用戶決定事項 |

## 動畫 Workflow：流程架構

完整執行規則見 [`workflows/animation-workflow.md`](workflows/animation-workflow.md)。

### Lane hierarchy

```text
Motion need
├─ Micro Motion
│  └─ hover、focus、press、短 feedback
├─ Choreographed Motion
│  ├─ UI Motion：modal、menu、route、state transition
│  └─ Scroll Story：章節、pin、reveal、視覺敘事
└─ Cinematic WebGL
   └─ camera、depth、space、particles、orbitable scene／3D world
```

CSS／Motion 做到就唔升級。只有空間、相機或 3D 世界本身承載結果時，先進入 Cinematic WebGL。

### 完整執行鏈

```text
Motion purpose
→ Lane selection
→ Scene / Technical Lock（Cinematic 才需要）
→ Motion direction
→ Beat sheet
→ Deterministic timeline
→ Architecture
→ Scene choreography
→ Timing polish
→ Browser evidence
→ Public 任務：一次 bounded review → 最多修一刀
→ Stop / handoff
```

### 10 個階段

| 階段 | 核心動作 | 主要輸出 |
|---|---|---|
| 1. Purpose / lane | 每段動畫至少服務情緒、故事、狀態、注意力或可信度其中一項，再選 Micro、Choreographed 或 Cinematic | 明確 motion job；冇工作就刪 |
| 2. Scene / Technical Lock | Cinematic 任務鎖主體、世界、視角、相機自由度、材質、光、情緒、真實度、host stack、Three.js 版本與 fallback | Scene lock + technical lock |
| 3. Reference / ImageGen | 只在已命名缺口使用 Refero／ImageGen；參考補空白，生成資產唔可以改寫 scene lock | 原創視覺方向或有來源紀錄的 supporting asset |
| 4. Technical router | 真 Three.js 工作先讀 fundamentals，再按當前問題揀最多 1–3 個專項；唔全包注入 | 最細足夠的技術組合 |
| 5. Motion ownership | 同一元素同一時間只准一個 owner：CSS、Motion、GSAP 或 Three.js | 無 transform ownership 衝突的 architecture |
| 6. Pre-production | Choreographed／Cinematic 先寫 motion direction、beat sheet、timeline；定義 trigger、enter、active、exit／settle、mobile 與 reduced-motion alternative | 可執行而非「大概順」的時間設計 |
| 7. Implementation layers | 依次完成 Architecture → Scene choreography → Timing polish；上層未成立，不用 polish 掩飾 | 穩定 lifecycle、清楚視覺因果、最後先微調 easing／stagger |
| 8. Cinematic build | 依次做 silhouette／composition → camera／world scale → light／material／texture → main action → interaction → loading／fallback／mobile tier → post-FX | 先成立的 3D 世界，再加氣氛 |
| 9. Time-based evidence | 驗 start／mid／settled、desktop／mobile、touch、occlusion、resize、loading、fallback、reduced motion、performance 與 cleanup | MP4、contact sheet、semantic keyframes 或 scroll-state evidence |
| 10. Review / stop | Public 任務只做 1 次正式 review、最多 1 刀同路線修正；重驗後停手，交回用戶判斷 | 可見 artifact、lane、owner、證據、fallback 與已知限制 |

### Motion ownership

| Owner | 適合負責 |
|---|---|
| CSS | hover、focus、tiny transition、細微 texture |
| Motion | component、layout、route 與 state transition |
| GSAP | scroll timeline、長 sequence、pin／scrub 編排 |
| Three.js | scene 物件、camera、shader 與 spatial interaction |

同一個 transform 唔可以同時由多套工具控制。每段 sequence 都要有 trigger、outcome、states、cleanup、mobile alternative 同 reduced-motion alternative。

## 何時加額外流程

只按觸發條件加：

- **大型 repo 或架構混亂** → `workflows/file-architecture-workflow.md`
- **公開／賣畀客／高風險視覺作品** → 提高 browser／interaction／handoff 證據；獨立 evaluator 仍只在用戶明確要求時加入
- **時間性動畫／VFX** → MP4、contact sheet 或 deterministic frames
- **用戶明確要求小隊／多條獨立研究線** → subagents / ClawTeam
- **需要配置 Hermes／MCP** → 對應 included skill
- **普通內部修改** → 不開角色小隊、不做 evidence scoring 儀式

## 最低驗證

### 靜態／網站

- 一個主要 viewport 真畫面
- Title／H1／主要 CTA readback
- Console／page 無阻斷錯誤
- 主流程可用
- 今次涉及 responsive 先補另一 viewport
- 一句人話質量判斷

### 動畫

以上再加其中一項：

- 6–12 秒 MP4；或
- contact sheet / semantic keyframes；或
- mid-transition / scroll-state evidence。

技術通過不等於畫面好。最終判斷以可見成品為準。

## 工具

已有 dev server：

```bash
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/verify_browser_artifact.py
ARTIFACT_URL=http://127.0.0.1:5173 python3 scripts/record_browser_scroll.py
```

靜態 artifact：

```bash
ARTIFACT_ROOT=/path/to/site python3 scripts/verify_browser_artifact.py
ARTIFACT_ROOT=/path/to/site python3 scripts/record_browser_scroll.py
```

## Optional skill index

`included-skills/` 只保存**按需 Skill 路由索引**，不再內嵌完整 Skill 副本。

正常網站任務最多先讀一個主要 design skill；只有遇到實際問題先加 architecture、reel、MCP、image generation、multi-agent 或 handoff skill。

不要一次載入全部 skills。不要將 skills file count 當成套件品質。

## 生產力規則

- 一個可見 artifact 同一時間只准一個 writer。
- 一個線性修改唔需要四個角色。
- 一次 iteration 必須有 visible/testable delta。
- scheduling、報告、checklist 唔等於進度。
- 不為了「完整」而建立新文件、Prompt、Gate 或版本。
- 公開或高價值唔等於自動多 agent、多 evaluator 或重做 design system。
- strongest approved baseline 永遠優先於 technically cleaner but visibly weaker candidate。

## Optional / archive-style references

以下保留作按需查閱，不進入正常 reading path：

- `docs/workflow-kit-maintenance-map.md`
- `WORKFLOW_COMPLETENESS_AUDIT.md`
- `PACKAGING_AUDIT.md`
- `prompts/`
- `checklists/`
- `included-skills/`
- 深度 architecture / MCP / handoff 文件

## 安全

不包含 API key、token、memory、cron、config、service 或身份檔。任何 credential 只可顯示為 `[REDACTED]`。
