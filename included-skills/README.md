# Optional Skill Index

v1.4.0 保持 index-only，唔內嵌／安裝任何 Skill body。

原因：完整副本會過期、重複載入、失去 source/license/version authority，
亦容易將另一個 project runbook 帶入網站工作。核心 workflow 單獨可用；
當前 agent 環境真有相應能力時先按需載入。

## 路由

- 網站 art direction：design-taste-frontend
- Frontend architecture／preservation：frontend-technical-architecture-gate、
  behavior-preserving-refactor
- Browser／驗證：creative-browser-artifacts、playwright-interactive、
  verification-before-completion
- High-stakes visible review：adversarial-quality-loop
- Reference／ImageGen：social-reel-agent-system-recon、imagegen-frontend-web
- Official source lookup：source-driven-development、context7-mcp
- Handoff：artifact-provenance-and-handoff
- Long run／explicit independent lanes：autonomous-work、
  dispatching-parallel-agents

## Three.js

官方 authority係 host project exact version對應嘅
[mrdoob/three.js](https://github.com/mrdoob/three.js) source、manual、API docs
同 examples。官方 repo冇發行 Agent Skills。

本機如已安裝，可以用 threejs-cinematic-motion 做 director，再揀最多
1–3 個 threejs topic skills。呢啲係我哋根據官方 source寫嘅 local
guidance，唔係 official Three.js product；詳細 source lock見
[THREEJS_SOURCE_LOCK.json](THREEJS_SOURCE_LOCK.json)。

## Rules

1. 正常任務只讀一個主要 domain skill。
2. Skill唔存在時，core workflow照樣執行。
3. External install先核 repository/path、commit/version、license、
   scripts/hooks、permissions同rollback。
4. 唔用mutable branch、popularity或README license claim做authority。
5. 唔從舊 package覆蓋 active skills。
