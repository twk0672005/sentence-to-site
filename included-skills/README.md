# Optional Skill Index

v1.3.3 不再內嵌完整 Hermes Skill 副本。

原因：完整副本容易過期、重複載入，亦曾將交易／系統個案帶入網站動畫套件。日常 workflow 應直接使用本包核心文件；只有遇到實際需求時，先從當前 agent／Hermes 環境載入對應 Skill。

## 建議路由

- 網站設計：`design-taste-frontend`
- Browser artifact／截圖／影片：`creative-browser-artifacts`
- 可見品質批判：`adversarial-quality-loop`
- Three.js／WebGL cinematic scene（先由 animation workflow 條件式載入）：`threejs-cinematic-motion`
- Three.js 窄技術題目（再按需要揀 1–3 個）：`threejs-fundamentals`、`threejs-geometry`、`threejs-materials`、`threejs-lighting`、`threejs-textures`、`threejs-animation`、`threejs-loaders`、`threejs-shaders`、`threejs-postprocessing`、`threejs-interaction`
- 完成前驗證：`verification-before-completion`
- 前端架構：`frontend-technical-architecture-gate`
- Reel／IG／TikTok reference：`social-reel-agent-system-recon`
- 現有網站 redesign：`redesign-existing-projects`
- 圖像生成：`imagegen-frontend-web`
- Hermes／MCP：`hermes-agent`、`native-mcp`
- 用戶明確要求多代理：`dispatching-parallel-agents` 或 `clawteam`

## 規則

1. 正常任務先讀一個主要 domain skill，唔好全載入。
2. 多代理、MCP、image generation、reel extraction 都係條件式能力。
3. Skill 不存在時，核心 workflow 仍然可獨立使用。
4. 不要從舊 package 盲目覆蓋當前 active skills。
5. CloudAI-X 技術 pack 只供私人本機參考；官方 Three.js r185 文件與實際 browser evidence 優先。

完整 v1.2.6 bundled sources 已保留於舊版及備份，只供 archaeology／rollback，不再作 v1.3 日常內容。
