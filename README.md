# Afuu Website + Animation Workflow Kit

**Version:** v1.4.0 — Truthful Evidence Core
**Purpose:** 用最短合理流程，將一句描述或現有網站變成可見、可用、可驗證、
可交付嘅網站／動畫成果。

呢個 repo係 reference kit + optional browser QA utilities。佢唔係 starter
app、Agent Skill library、身份檔、MCP installer或部署授權。

## 五分鐘開始

日常任務只讀：

1. 呢份 README；
2. 網站讀 [website-workflow.md](workflows/website-workflow.md)；
3. 動畫／WebGL讀 [animation-workflow.md](workflows/animation-workflow.md)；
4. 真正需要時先讀一份 optional reference／skill。

核心 loop：

    result lock
    -> authority / product truth / protected baseline
    -> smallest useful lane
    -> one complete visible slice
    -> real browser or temporal evidence
    -> one independent review batch when scope requires it
    -> one bounded repair
    -> PASS / PARTIAL / FAIL / WAITING_FOR_NOVA

## Result Lock

Normal以上先記：

| Field | Decision |
|---|---|
| Base route | new-site／existing-site |
| Work depth | tiny／normal／serious／redesign |
| Experience lane | static／ui-motion／cinematic-webgl |
| Delivery intent | prototype／public-candidate |
| Visual source | direct-build／reference-locked／shared-canvas |
| Five-second message | 第一眼明白甚麼？ |
| Primary action | 最重要下一步？ |
| Trust proof | 點解值得相信？ |
| Protected baseline | 邊部分唔可以倒退？ |
| Required evidence | 今次 claim要咩證據？ |
| Stop condition | 去到邊個可驗證狀態停？ |

## Website Workflow

[完整規則](workflows/website-workflow.md)

- 現有站先追 Product truth trace：
  copy/control -> route -> state -> API/data -> engine -> output。
- Redesign先寫 Preservation map：PRESERVE／EVOLVE／RETIRE／DECISION。
- Concept未定先做一次最多三個候選嘅有界 research。
- Static／semantic／responsive先成立，motion／3D後加。
- Mobile係recomposition，唔係desktop縮細。
- Serious／Redesign用fresh independent evaluator；只修最高影響root cause。

## Animation Workflow

[完整規則](workflows/animation-workflow.md)

    Motion need
    ├─ Micro Motion
    ├─ Choreographed Motion
    │  ├─ UI Motion
    │  └─ Scroll Story
    └─ Cinematic WebGL

- 每段motion要有job、single owner、start/mid/settled、interrupt、mobile、
  reduced同cleanup。
- CSS／WAAPI／Motion做到就唔升級；camera／depth／space真係承載結果先用
  Three.js。
- Scene idle時render on demand；hidden/offscreen停止；route/unmount dispose。
- Temporal claim要真record／states，唔係animation declaration或still image。

## Official Three.js

Three.js library/API authority係 host project exact version對應嘅官方
[mrdoob/three.js](https://github.com/mrdoob/three.js) source、manual、API docs
同examples。

Audited baseline係r185 tag
cb3b077ee63818a8cc1ab273f08704d89b8ac492；2026-08-28 npm current
observed為three 0.185.1。呢個唔係強制升級。

官方repo冇Agent Skill SKILL.md。本機可選嘅threejs-cinematic-motion同
threejs-* topics係我哋根據官方source建立嘅guidance，唔係official
Three.js product。見
[THREEJS_SOURCE_LOCK.json](included-skills/THREEJS_SOURCE_LOCK.json)。

## Evidence Authority

[evidence-gate.md](workflows/evidence-gate.md)係唯一evidence type、coverage、
status同terminal verdict authority。

- HTTP 200唔證明畫面；
- build exit 0唔證明runtime；
- screenshot存在唔證明interaction／motion／accessibility；
- MP4/WebM存在唔證明有轉場、唔黑或已cleanup；
- agent success只係claim。

Raw evidence落檔；root conversation每個repair round通常最多睇一張wide
同一張narrow／changed-state圖。

## Browser QA

Python dependency pin：Playwright 1.62.0。Chromium另外安裝。FFmpeg只在
明確要求MP4時需要；motion script本身會產生WebM、start/mid/settled同
contact sheet。

### POSIX

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium

    ARTIFACT_ROOT=/path/to/dist TITLE_CONTAINS="Product" python3 scripts/verify_browser_artifact.py

### Windows PowerShell

    py -m venv .venv
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    .\.venv\Scripts\python.exe -m playwright install chromium

    $env:ARTIFACT_ROOT = "C:\path\to\dist"
    $env:TITLE_CONTAINS = "Product"
    .\.venv\Scripts\python.exe -B scripts\verify_browser_artifact.py

Rules：

- TITLE_CONTAINS／H1_CONTAINS／BODY_CONTAINS至少一個必填；
- static mode預設用OS dynamic port；指定port被佔用會fail，唔重用舊server；
- ARTIFACT_ROOT要係sanitized build/staging，有.env、private key、.git或
  symlink會fail；
- ARTIFACT_URL預設只准loopback；外部URL要明示ALLOW_REMOTE_URL=1；
- project progress hook預設關閉；PROGRESS_ADAPTER=app/cosmic係explicit
  diagnostic，唔代替real scroll。

Motion：

    ARTIFACT_ROOT=/path/to/dist H1_CONTAINS="Product" MOTION_DURATION_SECONDS=8 python3 scripts/record_browser_scroll.py

要MP4時另設REQUIRE_MP4=1並提供ffmpeg／ffprobe。

## Repository Validation

    python3 .github/scripts/validate-release.py
    python3 -m unittest discover -s tests
    python3 .github/scripts/run-browser-smoke.py

Validator會檢 exact repo/distribution contract、strict UTF-8、relative links、
JSON/version parity、secret/private-path patterns、Python compile、deterministic
ZIP、SHA-256同ZIP byte parity。CI會真正安裝browser並dogfood兩個utilities。

## Optional Capabilities

[SKILLS_MANIFEST.json](included-skills/SKILLS_MANIFEST.json)只係index，唔含
Skill body，亦唔自動安裝。Skill/plugin/MCP要先核source、immutable version、
license、scripts/hooks、permissions同rollback。

## Structure

    kit-manifest.json             version + exact distribution authority
    workflows/                    website / animation / evidence / optional references
    scripts/                      fail-closed browser utilities
    checklists/                   optional proportional reminders
    included-skills/              index + source provenance only
    docs/                         setup, troubleshooting, maintenance, history
    tests/                        deterministic unit and browser fixture
    .github/                      CI, release validator, issue/PR templates

## Safety

- 唔包含 credential、identity、memory、cron、service或client material。
- 唔自動install、login、upload、pay、push、deploy或publish。
- Reference／generated asset要有provenance同rights。
- Target project最近instructions、product truth同accepted baseline永遠優先。

版本、distribution file list同repo-only contract嘅machine authority係
[kit-manifest.json](kit-manifest.json)。
