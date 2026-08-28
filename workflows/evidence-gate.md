# Evidence Gate — Single Authority

呢份係 kit 唯一 evidence status／coverage authority。README、domain
workflows 同 checklists 只引用，唔重新發明 pass。

## Evidence types

| Primitive | 可以證明 | 唔可以證明 |
|---|---|---|
| Viewport screenshot | 一個 viewport/state/time 嘅 pixels | interaction、semantics、motion、WCAG |
| Full-page screenshot | capture method 產生嘅 layout snapshot | lazy/scroll journey 完整 |
| DOM/computed readback | sampled structure、geometry、declaration | 真 font face、interaction、motion quality |
| Console/page/network trace | 該 route/state 嘅 errors/requests | 其他 route 或整體品質 |
| Interaction record | named control/state 真係行過 | 無關 states 或完整 accessibility |
| Temporal media/frames | 記錄區間內嘅 motion | cleanup、offscreen、所有 reduced states |
| Keyboard/focus/a11y readback | 指定 path/tree/check | 完整 WCAG conformance |
| Performance/resource trace | named device/scenario interval | 其他 device/network/long run |
| Capture receipt | 檔案、時間、hash/bytes | 成品品質或 implementation PASS |

一件 artifact 只在直接證明多個 claim 時先重用；記同一 path，唔複製文字
扮多份 evidence。

## Status vocabulary

Check-level：

- pass：fresh evidence直接證明；
- issues：check跑咗並發現 defect；
- not-applicable：真係不適用，必須有原因；
- opted-out：用戶明確排除，必須有 scope record；
- blocked：缺 authority、tool 或 data；
- not-run：未收 evidence。

Runtime exception、broken required asset、failed critical request、unexpected
WebGL context loss係 issues，唔係 blocked。

Terminal：

    PASS / PARTIAL / FAIL / WAITING_FOR_NOVA

- PASS：全部 required checks pass。
- PARTIAL：有可用 artifact，但任何 required check係 issues／blocked／
  opted-out／not-run，或 judgement 未達 scope。
- FAIL：primary flow／truth／bounded repair 後成果不可接受。
- WAITING_FOR_NOVA：真 authority、rights、secret、account、payment、
  publish/deploy decision。

## Profiles

| Check | Tiny | Normal | Serious / Redesign | Motion |
|---|---|---|---|---|
| Artifact identity | if relevant | required | required | required |
| Protected behavior | if changed | required | required | required |
| Baseline | changed state | existing work | existing/redesign | existing/redesign |
| Desktop render | affected state | required | required | required |
| Mobile render | if changed | required | required | required |
| 320px/zoom-reflow | no | scoped | required | required |
| Primary action | if changed | required | required | required |
| Console/page/network | if changed | required | required | required |
| Overflow/assets | if changed | required | required | required |
| Legibility/contrast | if changed | required | required | required |
| Keyboard/focus/targets | if changed | scoped | required | required |
| State truth | if changed | scoped | required | required |
| Cross-route parity | no | multi-route | journey required | journey required |
| Independent judgement | no | recommended | required | required |
| Reduced motion | if changed | when motion exists | when motion judged | required |
| Temporal evidence | micro changed-state | no | when motion judged | required |
| Interruption/lifecycle | no | no | complex motion | required |
| Performance/resource | no | scoped | heavy surface | heavy motion/WebGL |

Scoped 項目仍要明示 pass/issues/not-applicable/blocked/not-run，唔可以消失。
Redesign要比較 baseline，唔准用 Normal/Tiny 逃避。

## Freshness and identity

每個 batch 綁：

- exact route／artifact path；
- source revision/hash；
- capture timestamp/timezone；
- browser/runner identity；
- viewport/state；
- artifact path、bytes、SHA-256；
- source最大 behavior-changing mtime／revision。

Evidence 必須晚過最後一個相關 source write。未受影響 artifact只有在
owner/hash證明改動不可能影響時先可重用。

## Claim gate

- HTTP 200只證明 response status。
- Build exit 0只證明 build command。
- CSS animation declaration只證明 motion可能存在。
- MP4存在唔證明有轉場、唔黑、唔停 frame。
- webgl canvas存在唔證明 scene完整、touch可用或已cleanup。
- Worker／agent success只係claim。

每個 user-facing completion claim 都要對應 fresh primitive。

## Compact manifest

    artifact: <route/path>
    profile: tiny | normal | serious | redesign | motion
    source: <revision/hash>
    captured_at: <ISO-8601>
    verdict: PASS | PARTIAL | FAIL | WAITING_FOR_NOVA
    checks:
      - id: artifact-identity
        required: true
        status: pass
        evidence: <path/hash/metric>
        note: <what it proves>

Required check唔可以用 N/A／optional消失。Numeric score只可以喺 coverage
完整後發布，否則係假精準。

## Evidence transport

Raw screenshots、video、HTML、JSON、trace落檔。Root conversation用 counts、
paths、top findings、hash/timestamp同 verdict；每輪通常只開兩張代表圖。
Evidence多唔等於品質高，亦唔准因 session budget 刪 required gate。
