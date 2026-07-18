---
name: motion-choreography
description: Use when browser work needs UI transitions, scroll choreography, GSAP, Motion, canvas, WebGL, responsive motion, or reduced-motion behavior.
---

# Motion Choreography

Motion is useful only when it clarifies hierarchy, a narrative beat, feedback, or state. Choose the smallest lane that owns the behavior: CSS for polish, UI motion for component state, a scroll system for choreography, and canvas/WebGL for a real scene.

Give each node one transform owner. If effects must combine, split wrappers rather than letting CSS, a motion library, scroll code, and a render loop write the same property.

For meaningful motion, define trigger, enter, active, exit, cleanup, mobile alternative, and a `prefers-reduced-motion` route. Mobile is a smaller story, not a compressed desktop timeline.

Use `../../references/motion-choreography.md` for routing and `../../templates/motion-brief.md` before building non-trivial behavior.
