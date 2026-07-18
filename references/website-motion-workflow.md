# Website Motion Workflow

## Scope and boundary

This workflow is for browser-rendered websites, not AI-generated video. UI motion, CSS transitions, Motion, GSAP, WebGL, canvas, and browser-recorded clips used as proof belong here. Generated video, image-to-video, and post-production belong to a separate workflow.

## Choose the smallest honest loop

| Work type | Required loop |
| --- | --- |
| tiny copy/CSS correction | inspect → edit → focused readback/build |
| visible page or section | design read → build → browser readback → desktop view → self-critique |
| public or conversion-sensitive page | visible-page loop + mobile view + console/page errors + primary CTA/flow |
| cinematic, WebGL, or scroll-led page | public-page loop + representative scroll states + motion evidence |

Do not report workflow steps as progress. The loop only counts when it produces a visible artifact, patch, or verified improvement.

## Project intake

Before implementation, inspect the existing framework, package manager, content structure, design tokens, animation owner, and verification scripts. Preserve the current stack unless the task explicitly authorizes a rebuild.

Write a short design read:

> This is a `<page kind>` for `<audience>`; it should feel `<visual language>` and use motion to `<narrative or UX job>`.

Then decide whether meaningful motion is needed. Static clarity is a valid outcome.

## File architecture

For a non-trivial project, keep responsibilities discoverable:

```text
src/
  content/       copy, sections, labels, data
  components/    visual structure and interactions
  motion/        GSAP/Motion setup and teardown
  scene/         WebGL/canvas lifecycle and fallback
  styles/        tokens, layout, responsive rules
  checks/        browser smoke and visual verification
```

The exact folders may follow the host framework. The invariant is that content, structure, motion, scene lifecycle, and verification do not become an uneditable single file.

## Motion ownership and fallback

Assign one transform owner per element:

- CSS: small focus/hover polish;
- Motion: UI state, gesture, layout, and simple scroll rhythm;
- GSAP: pinned, scrubbed, choreographed scroll sequences;
- WebGL/canvas: the main immersive scene.

For each non-trivial sequence, record trigger, intended outcome, enter/active/exit state, cleanup, mobile alternative, and reduced-motion alternative. Use progressive enhancement: an unavailable dependency or weak device must result in a clear static experience, not a broken page.

## Verification and review

Verify the current artifact, not a stale preview:

1. confirm the served page's title and key content;
2. inspect desktop and mobile composition where relevant;
3. inspect scroll/interactions and the final CTA;
4. check console and page errors for serious work;
5. emulate reduced motion for motion-led work;
6. capture MP4/GIF or multiple motion states when the quality of motion is being claimed;
7. critique the visible result and make one targeted improvement.

A build, HTTP 200, or hero screenshot alone is insufficient. If the expected evidence cannot be obtained, report the result as partial rather than claiming completion.

## Stop conditions

Pause before installing paid dependencies, exposing a preview publicly, publishing, changing project configuration, or handling secrets. Do not add animation just to satisfy an animation request when it weakens readability, performance, accessibility, or conversion.
