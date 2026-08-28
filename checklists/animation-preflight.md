# Animation Preflight Checklist

- [ ] 動畫有敘事工作，不只是好看
- [ ] Lane 已標明：Micro / Choreographed UI / Scroll Story / Cinematic WebGL
- [ ] Motion ownership 清楚：Motion / GSAP / Three.js / CSS 不打架
- [ ] 有 reduced-motion fallback 或合理降級
- [ ] Micro有 before / active / after；complex有 start / mid / settled
- [ ] Choreographed/Cinematic有6–12秒WebM/MP4或等值真時間record + contact sheet
- [ ] Temporal frames visibly distinct，唔黑、唔停第一frame、real scroll同步
- [ ] WebGL先需要viewpoints、loading/fallback、renderer/resource readback
- [ ] Mobile 動畫不遮字、不爆版
- [ ] Route/unmount/hidden/offscreen後冇orphan loop/listener/timeline
