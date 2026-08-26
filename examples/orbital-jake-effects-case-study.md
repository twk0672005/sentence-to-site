# Case Study: ORBITAL + Jake UI Visual Effects

## 原始問題

The brief asked to apply the visual language of the on-screen website in a Jake UI Reel to a planetary site, rather than copying the monitor, desk, or filming setup.

## 精簡後嘅實際跑法

1. 讀現有 ORBITAL 真畫面同 approved baseline。
2. 抽出 reference 入面可見嘅 motion／texture／節奏。
3. 找最弱一刀：普通 progress rail 同場景世界觀割裂。
4. 直接 patch 成 orbital progress device，保留 Earth → solar → deep field journey。
5. 開真頁面睇 desktop／mobile，再用短片確認 motion 唔係只得一張靚圖。

高風險或審美爭議大時，可以加一個獨立 evaluator；今次成功唔係因為有幾個角色，而係因為 critique 指向咗一個可見改動。

## 成功位

- 冇將網站改成 dashboard；
- progress／loading 變成場景一部分；
- 保留原本 journey；
- 短片證明狀態轉場。

## 踩過嘅坑

- 只推 WebGL progress，冇同步 real scroll；
- contact sheet 只抽頭幾秒，差點誤判；
- Headless WebGL 需要適合嘅 Chromium rendering flag。

## 可重用規則

```text
目的 → strongest baseline → 最弱一刀 → 真時間畫面 → 一次可見比較
```
