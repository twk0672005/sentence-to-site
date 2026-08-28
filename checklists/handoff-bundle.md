# Handoff Bundle Checklist

交給用戶、朋友、client 或另一個 agent 前，bundle 至少要包含以下內容。

## 必備

- [ ] README / brief
- [ ] changed files summary
- [ ] how to run locally
- [ ] how to verify
- [ ] viewport evidence按profile齊全（Tiny可只交changed state；Normal以上desktop/mobile）
- [ ] readback JSON / verification output
- [ ] known issues
- [ ] next recommended patch

## 動畫 / WebGL 額外必備

- [ ] Micro：before / active / after；或 complex：start / mid / settled
- [ ] Choreographed/Cinematic：6-12秒WebM/MP4 + contact sheet
- [ ] WebGL scope先需要viewpoint／resource／lifecycle readback
- [ ] reduced-motion / fallback 說明

## 交給 agent 的 context block

```text
Goal:
Current accepted version:
Do not change:
Primary weakness:
Files to inspect first:
Run command:
Verify command:
Evidence folder:
Expected output:
```

## 不應打包

- [ ] `.env`
- [ ] API keys / tokens / cookies
- [ ] `node_modules/`
- [ ] `.git/`
- [ ] huge raw generated cache
- [ ] personal screenshots unrelated to project
- [ ] pycache / build temp unless specifically needed
- [ ] base64/data URLs、完整tool transcript或無界raw logs
