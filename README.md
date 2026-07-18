# sentence-to-site

**One sentence in. A verified website out. · 一句話輸入，一個經瀏覽器驗證的網站輸出。**

**[English](#english) · [繁體中文](#繁體中文)**

[![Live showcase — built with this workflow](docs/assets/showcase-orbital.png)](https://twk0672005.github.io/orbital-spatial-intelligence/)

> **Showcase / 範本** — [ORBITAL: From Earth into deep space](https://twk0672005.github.io/orbital-spatial-intelligence/) · a WebGL cinematic journey site produced with this exact workflow: one-sentence brief → visual direction → motion choreography → screenshot-verified delivery.
> 上面就是用這套 workflow 做出來的真實網站：一句話需求 → 視覺方向 → 動畫編排 → 截圖驗證交付。**點圖即看 live。**

---

## English

You have a vague idea — *"a landing page for my coffee cart, warm, not corporate"*. An AI agent loaded with this kit turns that sentence into a finished website: it expands the idea into a design premise, makes the small decisions on your behalf (and tells you which ones, so you can veto them in one line), builds the page, **looks at it in a real browser**, repairs the weakest visible thing, and repeats until the result is honest to show.

This is a **skill library for AI agents** (Claude Code, Codex, and any agent that reads `SKILL.md` files) — not a website builder app, not a giant prompt, not a framework. It encodes the workflow: how to expand a vague sentence without interrogating the user, how to choose a visual direction that isn't generic, how to choreograph motion responsibly, and how to prove — with screenshots and browser readback, never with a build exit code — that the site actually works.

```text
one vague sentence
→ premise + explicit assumptions   (decisions, not a questionnaire)
→ visual direction                 (anti-generic, one visible promise)
→ build + motion                   (framework-neutral: CSS is a valid lane)
→ browser evidence                 (real render, honest verdict)
→ weakest-issue repair loop        (multi-role adversarial loop when available)
→ bounded handoff                  (what was decided for you, and how to veto it)
```

### The skills

The flagship skill is the entry point; the rest are its pipeline. Load one decision-shaped skill at a time — a tiny CSS fix does not need seven modules.

| Skill | Use it for |
| --- | --- |
| [`one-sentence-website`](skills/one-sentence-website/SKILL.md) | **the entry point** — turn one vague sentence into a shipped, verified site |
| [`adversarial-quality-loop`](skills/adversarial-quality-loop/SKILL.md) | a real quality loop — separated Planner / Builder / Evaluator / Evidence Auditor roles, not self-critique |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | route a website task to the right specialist below |
| [`visual-story-direction`](skills/visual-story-direction/SKILL.md) | premise, hierarchy, material direction, and visual critique |
| [`website-motion-intake`](skills/website-motion-intake/SKILL.md) | existing-project stack, ownership, baseline, and verification discovery |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | UI, scroll, canvas, WebGL, mobile, and reduced-motion behavior |
| [`browser-evidence`](skills/browser-evidence/SKILL.md) | screenshots, browser readback, recordings, and honest verdicts |
| [`delivery-handoff`](skills/delivery-handoff/SKILL.md) | bounded delivery, known issues, and privacy-safe continuation |

The machine-readable map is [`skills/catalog.json`](skills/catalog.json). Each skill has its own evaluation fixture; shared guidance has one canonical copy under [`references/`](references/).

### Why this exists

Agents are already good at generating web code. What they get wrong is everything around the code:

- They answer a vague idea with a questionnaire instead of a decision.
- They produce the same generic gradient-and-glass page for every prompt.
- They claim "done" because the build passed, without ever rendering the page.
- They grade their own homework and call the self-review a "quality loop".
- They hand off with no record of what was assumed on the user's behalf.

Each skill in this kit is a countermeasure to one of those failure modes. The core rule everywhere: **completion is a browser verdict, never a build exit code.**

### Install and validate

See [Installation](docs/INSTALLATION.md) for bundle-first installation into your agent's skill directory. Validate the repository before use or release:

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
python3 -m py_compile scripts/*.py
```

Optional executable browser evidence requires Playwright; scroll recordings also require FFmpeg. See [`references/tooling.md`](references/tooling.md).

### Structure and boundaries

Read [Architecture](docs/ARCHITECTURE.md) before adding modules. The kit is deliberately framework-neutral: CSS, a UI motion library, GSAP, canvas, and WebGL are lanes to choose when appropriate, not required dependencies. Static HTML/CSS is a valid and often correct output for a one-sentence site.

The public bundle contains no credentials, client assets, internal runtime configuration, private prompts, or bundled third-party skills. It is a clean-room equivalent core, not a copy of any private operating manual.

---

## 繁體中文

你有一個模糊的想法 —— *「幫我的咖啡車做個 landing page，要溫暖，不要太商業」*。載入這套 kit 的 AI agent 會把這句話變成一個完成的網站：它把想法展開成設計前提，替你做好各項小決定（並明確列出，讓你一句話就能否決），動手建頁，**在真實瀏覽器裡親眼看它**，修復畫面上最弱的一環，如此循環，直到結果誠實可示人為止。

這是一套 **給 AI agent 用的 skill library**（Claude Code、Codex，以及任何讀 `SKILL.md` 的 agent）—— 不是網站生成器 app，不是一條巨型 prompt，也不是框架。它編碼的是 workflow 本身：如何展開一句模糊需求而不逼問使用者、如何選出不落俗套的視覺方向、如何負責任地編排動畫，以及如何證明網站真的能動 —— 憑截圖與瀏覽器 readback，永遠不是憑 build exit code。

```text
一句模糊的話
→ 前提 + 明確假設        （直接做決定，不是問卷）
→ 視覺方向               （反通用感，一個看得見的承諾）
→ 建頁 + 動畫            （框架中立：純 CSS 也是正當路線）
→ 瀏覽器證據             （真實 render，誠實裁決）
→ 最弱一環修復循環        （條件允許時走多角色對抗式 loop）
→ 有邊界的交付           （替你做過哪些決定、如何一句話否決）
```

### Skill 一覽

旗艦 skill 是入口，其餘是它的 pipeline。一次載入一個決策範圍的 skill 即可 —— 改一行 CSS 不需要載入七個模組。

| Skill | 用途 |
| --- | --- |
| [`one-sentence-website`](skills/one-sentence-website/SKILL.md) | **入口** —— 一句模糊的話 → 一個已交付、已驗證的網站 |
| [`adversarial-quality-loop`](skills/adversarial-quality-loop/SKILL.md) | 真正的品質循環 —— Planner / Builder / Evaluator / Evidence Auditor 四角色分離，不是自我批改 |
| [`cinematic-web-motion`](skills/cinematic-web-motion/SKILL.md) | 把網站任務路由到下方最合適的專門 skill |
| [`visual-story-direction`](skills/visual-story-direction/SKILL.md) | 設計前提、視覺層級、材質方向與視覺批判 |
| [`website-motion-intake`](skills/website-motion-intake/SKILL.md) | 既有專案的技術棧、權責、基線與驗證路線盤點 |
| [`motion-choreography`](skills/motion-choreography/SKILL.md) | UI 動畫、scroll、canvas、WebGL、行動端與 reduced-motion |
| [`browser-evidence`](skills/browser-evidence/SKILL.md) | 截圖、瀏覽器 readback、錄影與誠實裁決 |
| [`delivery-handoff`](skills/delivery-handoff/SKILL.md) | 有邊界的交付、已知問題、隱私安全的接手說明 |

機器可讀的總覽在 [`skills/catalog.json`](skills/catalog.json)。每個 skill 都有自己的 eval fixture；共用指引只在 [`references/`](references/) 保留唯一正本。

### 為什麼需要這套 kit

Agent 早就很會寫網頁 code，出錯的是 code 以外的一切：

- 面對模糊需求，回你一份問卷，而不是替你做決定。
- 每條 prompt 都生出同一款「漸層 + 毛玻璃」的通用頁面。
- build 一過就宣稱「完成」，從未真正 render 過那一頁。
- 自己批改自己的作業，還把自我審查叫做「品質循環」。
- 交付時完全不記錄替使用者假設了什麼。

這套 kit 裡的每個 skill 都是針對其中一種失敗模式的對策。貫穿全套的核心規則：**完成與否由瀏覽器裁決，永遠不由 build exit code 裁決。**

### 安裝與驗證

安裝方式見 [Installation](docs/INSTALLATION.md)（bundle 優先，放進你的 agent skill 目錄即可）。使用或發佈前先驗證：

```bash
python3 scripts/validate_skill_package.py
python3 tests/validate_skill.py
python3 tests/validate_skill_library.py
python3 tests/validate_release_contract.py
python3 -m py_compile scripts/*.py
```

可選的可執行瀏覽器證據需要 Playwright；scroll 錄影另需 FFmpeg。詳見 [`references/tooling.md`](references/tooling.md)。

### 結構與邊界

新增模組前先讀 [Architecture](docs/ARCHITECTURE.md)。這套 kit 刻意保持框架中立：CSS、UI 動畫庫、GSAP、canvas、WebGL 都是按需選用的路線，不是必要依賴。對一句話網站而言，靜態 HTML/CSS 往往就是正確答案。

公開 bundle 不含任何 credentials、客戶素材、內部 runtime 設定、私人 prompt 或第三方 skill。它是 clean-room 等價核心，不是任何私人操作手冊的複製品。

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). A new skill must have a distinct trigger, decision boundary, catalog entry, focused eval, and validation result; a differently named duplicate is not a contribution.

## Security

Read [SECURITY.md](SECURITY.md). Do not report credentials or exploit details publicly.

## License

[MIT](LICENSE)
