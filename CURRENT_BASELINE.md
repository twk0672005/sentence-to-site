# Afuu Website + Animation Workflow — Current Baseline

**Status:** RELEASE CANDIDATE — local verification complete; not published
**Version:** v1.4.0-truthful-evidence-core
**Previous main:** 9afce9b3ded7b2d2dcf41ade41872ee6ac2c4495

## Product identity

呢個repo係portable reference kit + optional local browser QA utilities。
唔係starter app、installable Agent Skill library、identity/config package或
publishing permission。

Default reading path：

    README.md
    -> choose website-workflow.md OR animation-workflow.md
    -> load one optional reference/specialist only when a named gap requires it

## v1.4 authority

- kit-manifest.json：唯一 version、distribution files、repo-only files authority；
- workflows/evidence-gate.md：唯一 evidence type、coverage、status、terminal
  verdict authority；
- workflows/website-workflow.md：product truth、preservation、responsive、
  browser/review/handoff；
- workflows/animation-workflow.md：motion lane、ownership、official Three.js、
  lifecycle、temporal evidence；
- included-skills/THREEJS_SOURCE_LOCK.json：official source provenance；
- scripts/browser_common.py：target identity、sanitized static root、port／remote
  policy；
- .github/scripts/validate-release.py：repo/distribution/ZIP truth gate。

## Main changes

- 加 Product truth trace、Preservation map、work depth同唯一terminal vocabulary；
- 將Micro／Choreographed／Cinematic evidence比例化；
- Serious／Redesign／Motion使用fresh independent judgement，但仍只做一個
  review batch + 一個bounded repair；
- 加session payload budget，raw media落檔；
- 移除CloudAI-X作runtime authority，改以official mrdoob/three.js host-version
  source/docs為唯一API authority；
- static browser verifier要求identity marker、sanitized entry、strict port；
- progress hook變explicit adapter，唔可以偽造real scroll；
- browser verifier覆蓋desktop／390／320、full-page、keyboard、errors、
  failed requests、overflow、reduced motion；
- motion recorder產生WebM、semantic frames同contact sheet；MP4係optional
  FFmpeg gate；
- release validator建立deterministic ZIP、SHA256SUMS並驗exact byte parity；
- CI恢復unit + real browser dogfood。

## Source snapshot

- Official Three.js source tag：r185
- Tag commit：cb3b077ee63818a8cc1ab273f08704d89b8ac492
- npm observed 2026-08-28：three 0.185.1
- Playwright pin：1.62.0
- ThreeUI Community：@designcodeio/threeui 1.1.0，optional only

## Verification completed — 2026-08-28

- release validator PASS：49 repository files、31 distribution files、32 ZIP
  entries；
- 13 unit tests PASS：occupied port、missing entry、sensitive root、remote URL、
  URL userinfo/redaction、three-state motion、unexpected file、version drift、
  broken file/fragment link、cache同allowed-prefix secret negative cases；
- pinned Playwright 1.62.0 + matching Chromium browser smoke PASS；
- verifier覆蓋desktop 1440×1000、mobile 390×844、narrow 320×800、full-page、
  keyboard、errors、failed requests、overflow、reduced motion；
- motion recorder覆蓋start／mid／settled三個distinct hashes、real scroll、
  WebM、contact sheet、reduced motion；FFmpeg unavailable所以MP4 not-run，
  但今次contract無要求MP4；
- wrong identity marker negative case正確FAIL並保留failure receipt；
- strict UTF-8、secret/private-path/symlink、JSON、Markdown file+fragment links、
  Python compile、git diff check PASS；
- deterministic distribution ZIP兩次byte-identical，SHA256SUMS同entry parity
  PASS；
- 15個引用嘅official Three.js manual URLs回HTTP 200；r185 tag commit核對；
- 11個本機official-source Three.js skills quick validator PASS；
- fresh independent verifier完成兩輪：六個 findings修復後，只餘v1.3文字
  drift，已修正並重驗。

## Publication boundary

呢個狀態代表branch可準備commit／review，唔代表GitHub main、tag、release或
distribution已發布。只有合併後先將main稱為v1.4 canonical；push、PR、tag
同release仍按用戶授權分開處理。
