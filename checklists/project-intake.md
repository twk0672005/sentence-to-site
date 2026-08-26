# Project Intake Checklist

開始改網站 / 動畫前，先確認現場，不要靠記憶估。

## 基本身份

- [ ] repo root 已確認
- [ ] 是否 git repo 已確認
- [ ] package manager 已確認：npm / pnpm / yarn / none
- [ ] framework 已確認：Static / React / Vite / Next / Astro / other
- [ ] dev command 已找到
- [ ] build command 已找到
- [ ] preview command 已找到

## 入口與架構

- [ ] main entry 已找到：`index.html` / `src/main.tsx` / `app/page.tsx`
- [ ] route / page structure 已找到
- [ ] content / copy 位置已找到
- [ ] components / sections 位置已找到
- [ ] styling system 已確認：CSS / Tailwind / CSS modules / styled components
- [ ] animation library 已確認：Motion / GSAP / Three.js / CSS only
- [ ] WebGL / canvas scene owner 已找到（如適用）

## 資產與證據

- [ ] images / textures / models / videos 位置已找到
- [ ] reports / screenshots / generated outputs 位置已找到
- [ ] current accepted screenshot / video 已保存或重新產生
- [ ] browser verification 方法已確認

## 安全與邊界

- [ ] `.env` / secrets 沒有被讀出或打包
- [ ] public publishing / payment / domain / deployment 未經批准不碰
- [ ] core config / service / cron 不碰，除非用戶明確要求
- [ ] rollback / backup 方法已確認

## 開工前一句話

```text
Current site is <framework>, entry is <file>, content lives in <folder>, motion owner is <file/folder>, verification will use <command/script>.
```
