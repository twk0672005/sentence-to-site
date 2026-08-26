# File Architecture Workflow

只在 repo 已經難以判斷「應該改邊一層」、多人／多 agent 容易互相踩檔，或大型重構前使用。普通小網站唔需要先重排全個目錄。

## 核心 ownership

```text
content owns meaning
components own layout
motion owns movement
scene owns WebGL/canvas
styles own tokens
assets own media
scripts own verification
reports own generated evidence
docs own durable decisions
```

目標係令下一個人五分鐘內知道改邊度，而唔係追求漂亮資料夾。

## 開工前五問

1. 真正 entry point 喺邊？
2. Hero／第一屏由邊個 component 控制？
3. Global styles／tokens 喺邊？
4. Animation／WebGL 由邊個檔案擁有？
5. 現有 build、test、browser QA 點跑？

先讀 `package.json`、README、主要 entry、現有 scripts 同當前 git status。唔好靠 stack 名估架構。

## 何時拆檔

拆分只因 ownership 或維護需要：

- 文案與 section data 反覆出現 → `content/`
- 可重用 layout／UI → `components/`
- 多 section 共用 timeline／scroll state → `motion/`
- Three.js、shader、camera、particles → `scene/`
- typography、spacing、colour → `styles/`
- 可重生 QA 輸出 → `reports/`，不要混入 source

小型 component-local 行為可以留喺 component。不要為了符合模板而拆成十個空資料夾。

## 建議結構（按需採用）

```text
src/
├── content/
├── components/
├── motion/
├── scene/
├── styles/
└── lib/
public/assets/
scripts/
reports/
docs/
```

不是每個 repo 都要齊全。只建立真正有 owner 的層。

## Animation ownership

同一個 element 不要同時由 CSS transition、Motion、GSAP 同 WebGL 搶 transform。

- UI entry／hover／layout morph → Motion 或 component-local CSS
- pinned／scrubbed scroll narrative → GSAP / explicit timeline
- cinematic world／particles／shader → Three.js / WebGL scene
- subtle texture／grain／button feedback → CSS

## 安全修改

1. 保留 strongest accepted baseline。
2. 先修改最少必要檔案。
3. 不做無關 migration。
4. generated evidence 不入 production source layer。
5. 多 writer 前先分 worktree／明確 ownership。
6. 架構改動後要跑 build 同 real browser smoke。

## Stop signs

- one giant `App.tsx` / `index.html` 混合 copy、scene、timeline、styles；
- 同一狀態由多套動畫工具控制；
- asset、source、generated screenshot 混埋；
- 為簡單 prototype 套入 enterprise folder tree；
- 先重構架構，後先諗用戶會睇到咩。

## 完成條件

架構改善只在以下情況成立：

- 改動位置更清楚；
- 現有 flow 沒有被推翻；
- build／browser main flow 仍正常；
- 可見成品沒有倒退。

目錄更整齊但畫面變差、速度變慢或修改範圍擴大，不算改善。
