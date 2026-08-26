# Handoff Bundle Checklist

交給用戶、朋友、client 或另一個 agent 前，bundle 至少要包含以下內容。

## 必備

- [ ] README / brief
- [ ] changed files summary
- [ ] how to run locally
- [ ] how to verify
- [ ] desktop screenshot
- [ ] mobile screenshot
- [ ] readback JSON / verification output
- [ ] known issues
- [ ] next recommended patch

## 動畫 / WebGL 額外必備

- [ ] top / mid / final screenshots
- [ ] 6-12 秒 MP4 / GIF
- [ ] contact sheet
- [ ] WebGL status readback
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
