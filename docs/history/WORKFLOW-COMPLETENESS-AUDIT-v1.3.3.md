# Workflow Completeness Audit

## Current verdict

**v1.3.3 Clean Result Core：PASS for lean, outcome-scaled workflow reference。**

上一版功能完整，但 default reading path 過重：完整 file architecture 手冊、角色 prompts、evidence scoring、maintenance map 與 bundled skills 容易被一口氣載入，令普通任務變成流程儀式。

## v1.3.0 修復

- README 改成一頁核心入口；
- 正常任務只需 README + 一份 domain workflow；
- file architecture 由完整教科書縮成按需決策指南；
- maintenance map 改成套件維護專用；
- Planner / Builder / Evaluator / Evidence Auditor 不再是普通任務預設；
- included skills 明確改為 optional reference library；
- strongest approved visual baseline 優先於技術上較完整但畫面較差的新版本。

## v1.3.1 補強

- Three.js cinematic scene 成為 animation workflow 內的條件式 specialist lane；
- 普通 CSS／Motion／GSAP 任務不載入 Three.js specialist；
- 增加 camera、material causality、delta-time、bloom-off 與 temporal anti-fake gates；
- 保持 README + 一份 domain workflow 的精簡 default reading path。

## v1.3.3 收斂

- website workflow 加入單一 scope lock、最細足夠 lane 與明確停手條件；
- 公開／高價頁只提高證據，不再自動觸發獨立 evaluator；
- animation workflow 分開 Micro、Choreographed、Cinematic，避免小改被升格；
- 高級動畫先做 motion direction、beat sheet、timeline，再行 architecture、scene choreography、timing polish 三層循環；
- 只完成微效果時必須按實際層級交付，不可用工具名或截圖抬高完成度。
- Refero拆成Product UI screens／flows與Refero Styles兩條概念研究lane；最多三個候選、一個primary source，並保持reference／baseline權威。
- Refero public UI禁止自動scrape／crawl／bulk download；官方MCP／API、登入、外部上載及付款仍屬批准邊界。

## 核心保留

- website workflow；
- animation / WebGL workflow；
- desktop / mobile / console / main-flow verification；
- temporal animation evidence；
- executable browser QA scripts；
- 高風險操作與完成前真實驗證。

## Honest boundary

這仍然不是 starter app。它不包含 Vite/Next sample、production CI 或完整產品模板。

套件內仍保留 prompts、checklists、included skills 與歷史 audit 作 optional reference；保留不代表每次都要讀。生產力改善的標準是更快產出更好成品，而不是文件數更多。
