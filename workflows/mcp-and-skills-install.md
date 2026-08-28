# Skills and MCP Routing — Optional, Source-Checked

呢個 kit 本身可獨立使用，冇「必裝 Skills」。先讀 README + 一份 domain
workflow；只有當前問題真係需要先載入一個 specialist。

## Capability routes

| Need | Optional capability |
|---|---|
| Product-specific visual direction | design-taste-frontend |
| Frontend architecture/preservation | frontend-technical-architecture-gate、behavior-preserving-refactor |
| Real browser/evidence | creative-browser-artifacts、playwright-interactive、verification-before-completion |
| High-stakes visible review | adversarial-quality-loop |
| Image-led reference | social-reel-agent-system-recon、imagegen-frontend-web |
| Source/API verification | source-driven-development、context7-mcp |
| Handoff/package | artifact-provenance-and-handoff |
| Long autonomous run | autonomous-work |
| Explicit independent lanes | dispatching-parallel-agents |

Skill唔存在時用 core workflow直接做，唔自動搜尋／安裝另一個同名 package。

## Official Three.js route

Three.js／WebGL 真係必要時：

1. 先讀 host project package/lock，確認 exact installed version；
2. 官方 authority：
   [mrdoob/three.js](https://github.com/mrdoob/three.js) source、manual、API
   docs、examples；
3. 可用 threejs-cinematic-motion 做 scene/lifecycle/evidence director；
4. 當前階段再揀最多 1–3 個：threejs-fundamentals、geometry、materials、
   lighting、textures、animation、loaders、shaders、postprocessing、
   interaction；
5. 唔一次載入全 pack，唔用 popularity 代替 source／license／version audit。

官方 Three.js repo本身係 library，唔包含 Agent Skill SKILL.md。本機 topic
Skills係根據官方 r185 source/docs原創嘅 guidance，不係官方發行物。

## Install gate

外部 Skill／plugin／MCP 安裝前記：

- exact repository/path；
- immutable commit/version；
- maintainer、license、scripts/hooks/allowed-tools；
- network、filesystem、account、credential同付費範圍；
- overlap/conflict同 rollback path；
- targeted validator／forward test。

Mutable branch、npx latest、uvx latest、curl pipe shell 或 README 聲稱 license
唔係可重現安裝 contract。External account、sign-in、token、上載、付款同
machine-wide config仍先獲批准。

## MCP boundary

MCP係外部 capability，唔係人格、審美或產品 authority。先用當前 agent
已提供嘅 connector；唔為一個普通網站任務另裝 server。

- GitHub：repo／issue／PR／CI；
- Figma／Canva：只有用戶提供相應 design authority 時；
- Filesystem：只給明確 root；
- design-research MCP：遵守登入、plan、terms、upload同 privacy gate。

Credential永遠唔寫入呢個 repo、prompt、example或 browser receipt。公開
文件只可用 [REDACTED] placeholder。
