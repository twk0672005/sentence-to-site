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

### 網站

使用 `workflows/website-workflow.md`：

- 定義目標用戶、第一眼感覺、主要行動；
- 只有頁面／flow／視覺語言未定義時，按需讀 `workflows/refero-inspiration.md`；
- 保留已經成立的版本；
- 只改達成今次結果所需範圍；
- 看 desktop、mobile、console、主要 flow；
- 用清楚停手條件防止自行擴 scope。

### 動畫 / WebGL

使用 `workflows/animation-workflow.md`：

- 動畫必須服務情緒、故事、狀態或注意力；
- 明確 Motion / GSAP / CSS / WebGL ownership；
- 先分類 Micro、Choreographed 或 Cinematic，低層級唔自動升級；
- Choreographed／Cinematic 先做 motion direction、beat sheet、timeline，再分 architecture、scene choreography、timing polish 三層實作；
- 真 Three.js／WebGL 場景先條件式載入 `threejs-cinematic-motion`，由佢負責場景、鏡頭、時間重量、mobile、fallback 同驗證；
- 再按實際問題揀 1–3 個 `threejs-*` 技術參考；禁止全包注入，普通 UI motion 不增加負擔；
- 用短片或時間序列驗證，不靠單張 screenshot；
- desktop 與 mobile 分開看；
- 新版 visibly worse 就保留舊 baseline。

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
