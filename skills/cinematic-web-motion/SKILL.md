---
name: cinematic-web-motion
description: Use when a website task involves visual direction, existing-project discovery, animation, browser verification, or a final handoff and it is unclear which specialist skill should lead.
---

# Cinematic Web Motion Router

Choose the smallest specialist skill that owns the decision. Do not load every module for a small CSS or copy correction.

| If the task needs… | Start with… |
| --- | --- |
| a premise, hierarchy, visual critique, or anti-generic direction | `visual-story-direction` |
| an existing repo, unknown files, accepted baseline, or stack read | `website-motion-intake` |
| UI motion, scroll choreography, canvas, WebGL, or reduced motion | `motion-choreography` |
| screenshots, browser readback, console review, recording, or verdict | `browser-evidence` |
| a delivery note, release boundary, or another contributor to continue | `delivery-handoff` |

For a non-trivial website change, the normal sequence is: visual direction → intake → implementation/motion → evidence → handoff. Skip stages that do not affect the claim; never skip browser evidence merely because a build passed.

Read `../../references/website-motion-workflow.md` for the shared operating loop and `../../docs/ARCHITECTURE.md` before adding or changing a module.
