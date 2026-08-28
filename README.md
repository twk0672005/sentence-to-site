# Afuu Website + Animation Workflow Kit

[![Version](https://img.shields.io/badge/version-v1.4.0-1f6feb.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-d4a72c.svg)](LICENSE)
[![Workflows](https://img.shields.io/badge/workflows-website%20%2B%20animation-8b5cf6.svg)](#whats-included)
[![Playwright](https://img.shields.io/badge/browser%20QA-Playwright%201.62.0-2eAD33.svg)](requirements.txt)
[![Validate Release](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-release.yml/badge.svg)](https://github.com/twk0672005/sentence-to-site/actions/workflows/validate-release.yml)

> 由一句網站要求，收斂成一個有產品身份、保留真實功能、responsive、
> 可用 browser evidence 驗證嘅網站成果。

**v1.4.0 — Truthful Evidence Core** 係一套畀 coding agent 同人類開發者使用嘅
網站／動畫決策流程，加上一組 fail-closed browser QA utilities。佢專門處理
AI 生成網站最常見嘅問題：畫面似模板、動畫冇目的、mobile 只係縮細 desktop、
功能改壞咗但 screenshot 仍然好睇，以及用 build success 冒充產品完成。

呢個 repository **唔係** component library、starter app、Agent Skill 合集、
MCP installer 或部署授權。佢提供嘅係一套可以套落現有 stack 嘅工作方法：
先理解產品，再設計；先保留行為，再重做表面；最後只講證據真正證明到嘅結果。

---

## Why use this

- **去 AI 味**：由產品內容、工具、數據形狀同文化語境建立視覺語言，唔由
  generic hero、gradient、card grid 開始。
- **保留原本功能**：Redesign 前先寫 `PRESERVE / EVOLVE / RETIRE / DECISION`
  preservation map。
- **按任務比例工作**：小修用 Tiny；一頁用 Normal；公開、高風險或大改版先用
  Serious／Redesign，唔將每個 CSS 改動變成大型儀式。
- **動畫有工作先存在**：feedback、orientation、continuity、hierarchy、progress
  或 emphasis；CSS 做到就唔升級到 WebGL。
- **Mobile 真正重新構圖**：重新決定 priority、order、density、crop、control
  model 同 resource budget，唔係 desktop 縮細。
- **用真證據驗收**：route identity、desktop/mobile、interaction、keyboard、
  console、overflow、reduced motion 同 temporal evidence 分開驗。

## What's included

| Capability | What it does | Entry |
|---|---|---|
| Website Workflow | 新站、現有站、Redesign；產品 truth、視覺 lock、responsive、review | [website-workflow.md](workflows/website-workflow.md) |
| Animation Workflow | Micro、UI choreography、scroll story、cinematic WebGL | [animation-workflow.md](workflows/animation-workflow.md) |
| Evidence Gate | 唯一 evidence coverage、status 同 terminal verdict authority | [evidence-gate.md](workflows/evidence-gate.md) |
| Browser Verifier | desktop/mobile/narrow、focus、overflow、console、reduced motion | [verify_browser_artifact.py](scripts/verify_browser_artifact.py) |
| Motion Recorder | WebM、start/mid/settled、contact sheet、optional MP4 | [record_browser_scroll.py](scripts/record_browser_scroll.py) |
| Skill Routing | design、Three.js、browser、source verification 按需要接入 | [mcp-and-skills-install.md](workflows/mcp-and-skills-install.md) |
| Release Validator | exact files、links、version、secret scan、deterministic ZIP、SHA-256 | [validate-release.py](.github/scripts/validate-release.py) |

## Core workflow

```text
result lock
  -> product truth + protected baseline
  -> smallest useful lane
  -> product-specific design lock
  -> one complete static slice
  -> responsive recomposition
  -> motion only when it earns a job
  -> real browser / temporal evidence
  -> independent review when scope requires it
  -> one bounded repair
  -> PASS / PARTIAL / FAIL / WAITING_FOR_NOVA
```

### Work depth

| Depth | Use when | Minimum route |
|---|---|---|
| Tiny | 一個客觀局部修正 | affected state + narrow verification |
| Normal | 一頁或一個 visible component | compact contract + wide/narrow render |
| Serious | 公開、跨頁、reference-led 或 trust-sensitive | baseline + full contract + independent review |
| Redesign | 現有產品大改版 | Serious + preservation map + baseline comparison |

### Experience lane

```text
static
├─ semantic content, layout, states and responsive composition
ui-motion
├─ micro feedback
├─ choreographed UI
└─ scroll story
cinematic-webgl
└─ camera, depth or explorable space is essential to the result
```

高級感本身唔係使用 Three.js 嘅理由。只有 camera、depth、space 或 spatial
interaction 真係承載產品結果，先進入 cinematic WebGL。

---

## Getting started

### 1. Website work

日常網站任務只需要讀兩份文件：

1. 呢份 `README.md`；
2. [Website Workflow](workflows/website-workflow.md)。

畀 coding agent 嘅最短指令：

```text
Use this workflow kit as reference only. Preserve the target project's own
instructions, product truth, stack and accepted behavior. Choose the smallest
useful work depth, complete one visible slice, verify the real artifact, and
report only what fresh evidence supports.
```

### 2. Animation or WebGL work

只有當 motion 係結果一部分，先再讀
[Animation Workflow](workflows/animation-workflow.md)。Three.js 任務必須先讀
host project package／lock，跟返 exact version 嘅官方
[mrdoob/three.js](https://github.com/mrdoob/three.js) source、manual、API docs 同
examples。

### 3. Working with `design-taste-frontend`

如果 agent 環境已經有 `design-taste-frontend`：

- 普通「建立／修改／重做網站」要求可以由該 Skill 自動接管產品專屬 art
  direction 同視覺判斷；
- 呢個 kit 負責 scope、preservation、implementation sequence、evidence 同
  terminal verdict；
- animation workflow 只喺 motion 真係有工作時條件式加入；
- Tiny 修正唔會被迫執行完整 Serious／Redesign 流程。

本 repository 自身仍然係 reference kit，唔會靜默安裝 Skill、改寫其他專案
instructions 或自動 deploy。

---

## Browser QA

Browser utilities 使用 pinned `playwright==1.62.0`。Chromium 需要另外安裝；
FFmpeg 只喺明確要求 MP4 時需要。

### POSIX

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

ARTIFACT_ROOT=/path/to/dist \
TITLE_CONTAINS="Product" \
python3 scripts/verify_browser_artifact.py
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium

$env:ARTIFACT_ROOT = "C:\path\to\dist"
$env:TITLE_CONTAINS = "Product"
.\.venv\Scripts\python.exe -B scripts\verify_browser_artifact.py
```

至少提供一個 identity marker：`TITLE_CONTAINS`、`H1_CONTAINS` 或
`BODY_CONTAINS`。Static root 含 `.env`、private key、`.git` 或 symlink 會
fail；external URL 預設唔准，避免誤驗舊 server 或錯誤網站。

### Motion evidence

```bash
ARTIFACT_ROOT=/path/to/dist \
H1_CONTAINS="Product" \
MOTION_DURATION_SECONDS=8 \
python3 scripts/record_browser_scroll.py
```

Recorder 會產生 WebM、三個相異嘅 start/mid/settled states 同 contact sheet。
要將 MP4 變成 hard gate，另設 `REQUIRE_MP4=1` 並提供 `ffmpeg`／`ffprobe`。

---

## Evidence model

[evidence-gate.md](workflows/evidence-gate.md) 係唯一 evidence type、coverage、
status 同 terminal verdict authority。

| Evidence | Can prove | Cannot prove alone |
|---|---|---|
| Build exit 0 | source/build command完成 | 真實 runtime、畫面或 journey |
| HTTP 200 | endpoint 有回應 | 回應緊正確網站 |
| Screenshot | 一個 viewport/state 嘅 pixels | interaction、motion、accessibility |
| Video/WebM | 錄製期間嘅時間變化 | cleanup、offscreen lifecycle、全部 states |
| Agent report | agent 聲稱完成 | implementation 或產品 PASS |

Raw screenshot、video、HTML、JSON 同 trace 應該落檔；對話只回傳 path、hash、
viewport/state、關鍵 metrics 同 verdict，避免大型 evidence 拖垮 session。

---

## Repository validation

```bash
python3 .github/scripts/validate-release.py
python3 -m unittest discover -s tests
python3 .github/scripts/run-browser-smoke.py
```

Validation 包括：

- exact repository／distribution allowlist；
- strict UTF-8、relative links 同 version parity；
- secret、credential、private path、sensitive filename 同 symlink checks；
- Python compile；
- positive browser verifier／motion recorder smoke；
- wrong-site marker negative test；
- deterministic ZIP、SHA-256 同 ZIP byte parity。

## Repository map

```text
kit-manifest.json       version + exact distribution authority
workflows/              website, animation, evidence and optional references
scripts/                fail-closed browser QA utilities
checklists/             proportional intake, preflight and delivery reminders
included-skills/        optional capability index + source provenance only
prompts/                visual-reference extraction prompt
docs/                   setup, usage, troubleshooting, maintenance and history
tests/                  deterministic unit tests + browser fixture
.github/                CI, release validation, issue and PR templates
```

## Source and safety boundaries

- Target project 最近嘅 instructions、產品 truth 同 accepted baseline 永遠優先。
- 唔包含 credential、identity、memory、cron、service 或 client material。
- 唔自動 install、login、upload、pay、push、deploy 或 publish。
- Reference／generated asset 要有 provenance 同 rights。
- Optional Skill、plugin 或 MCP 要先核 source、immutable version、license、
  scripts/hooks、permissions 同 rollback。
- `kit-manifest.json` 係 version、distribution file list 同 repo-only contract 嘅
  machine authority。

## Contributing and support

- 使用問題或 bug：開 [GitHub issue](https://github.com/twk0672005/sentence-to-site/issues)。
- 改動前先讀 [CONTRIBUTING.md](CONTRIBUTING.md)。
- Security 問題跟 [SECURITY.md](SECURITY.md) 嘅 private reporting route。
- Release history 見 [CHANGELOG.md](CHANGELOG.md)。

## License

呢個 project 使用 [MIT License](LICENSE)。
