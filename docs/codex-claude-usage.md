# Codex / Claude Code Usage Guide

這是一份 reference 文件，不是 `AGENTS.md`／`CLAUDE.md`，亦不應覆蓋目標 repo 自己嘅 instructions、memory 或設定。

## 最短使用方法

1. 讀 `README.md`。
2. 網站任務讀 `workflows/website-workflow.md`。
3. 動畫／WebGL 任務讀 `workflows/animation-workflow.md`。
4. 只在大型重構時讀 `workflows/file-architecture-workflow.md`。
5. 直接改一個有用 slice，開真頁面驗證，再交付。

不要先讀完整套件。Tiny／Normal由root直接做；Serious／Redesign／Motion
最多用一批bounded discovery helpers同一個fresh evaluator，唔為角色齊全
開隊。

## 可貼入 coding agent 嘅短指令

```text
Use this workflow kit as reference only. Preserve the target project's own instructions, product truth, and accepted baseline. Read README.md plus the one matching workflow. Make the smallest useful change, keep raw evidence on disk, verify the real artifact, and report only what fresh evidence supports. Use independent review only for Serious, Redesign, Motion, or explicitly high-stakes work.
```

## 工具

最低需要目標專案原本嘅 build/runtime。Browser QA scripts 額外需要 Python、Playwright 同 Chromium；動畫錄製可能需要 FFmpeg。

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

已有 dev server：

```bash
ARTIFACT_URL=http://127.0.0.1:5173 TITLE_CONTAINS=Product python3 scripts/verify_browser_artifact.py
```

Static artifact：

```bash
ARTIFACT_ROOT=/path/to/dist TITLE_CONTAINS=Product python3 scripts/verify_browser_artifact.py
```

只在動畫時間性係 claim 一部分時先錄片：

```bash
ARTIFACT_URL=http://127.0.0.1:5173 H1_CONTAINS=Product python3 scripts/record_browser_scroll.py
```

## Optional skill routing

v1.4 不內嵌 Skill 副本。當前 agent 環境有對應能力先按需載入：

- design：`design-taste-frontend`
- browser artifact：`creative-browser-artifacts`
- 可見品質：`adversarial-quality-loop`
- 完成驗證：`verification-before-completion`
- Official source：`source-driven-development`
- Three.js director：`threejs-cinematic-motion`，再按需最多1–3個
  `threejs-*` topics
- reference extraction：`social-reel-agent-system-recon`
- 明確要求多代理：`dispatching-parallel-agents`／`clawteam`

Skill 不存在時，核心 workflow 仍然可以獨立使用。不要從舊 package 盲目安裝或覆蓋 active skills。
