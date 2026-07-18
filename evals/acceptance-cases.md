# Acceptance cases

Use these cases to evaluate whether an agent applying the kit makes sound website and motion decisions. A response passes only when it states the relevant decision and a concrete verification method.

## 1. Static visual story

**Prompt:** Create an editorial launch page for a small architecture studio.

**Pass:** Defines audience, narrative spine, hierarchy, typography/material direction, responsive composition, and an evidence tier before prescribing animation.

**Fail:** Begins with GSAP effects, generic bento cards, or an animation library without a visual premise.

## 2. Existing project and file architecture

**Prompt:** Add a cinematic introduction to an existing Vite site.

**Pass:** Inspects the current stack before adding dependencies; separates content, components, motion, scene lifecycle, styles, and checks proportionately.

**Fail:** Replaces the stack without reason or puts markup, copy, WebGL, scroll listeners, and QA hooks in one giant entry file.

## 3. Scroll choreography

**Prompt:** Add a pinned scroll story with a WebGL hero and animated product labels.

**Pass:** Assigns one transform owner per element; separates the WebGL scene from DOM labels; includes cleanup, mobile behavior, and reduced motion.

**Fail:** Lets GSAP, CSS hover transforms, and a render loop manipulate the same node.

## 4. Workflow boundary

**Prompt:** Make the website animation more cinematic and deliver an AI-generated MP4.

**Pass:** Treats browser motion and generated-video production as separate workstreams; asks for an explicit decision before adding a video pipeline.

**Fail:** Automatically introduces an image-to-video or generated-MP4 workflow into website implementation.

## 5. Completion claim

**Prompt:** The implementation is finished. What evidence is required?

**Pass:** Chooses the task-appropriate evidence tier; for serious motion work requires running-page readback, desktop/mobile inspection, interaction/scroll states, console/page errors, reduced motion, and motion evidence where claimed.

**Fail:** Treats a successful build, HTTP 200, or a single screenshot as sufficient proof.

## 6. Evidence verdict

**Prompt:** The desktop page looks correct and the build passes, but the mobile fold was not checked and the animation recorder cannot start because Chromium is unavailable.

**Pass:** Reports `partial` or `blocked` with the exact missing evidence and a realistic next step. It does not call the implementation complete.

**Fail:** Says the build proves success, treats a missing browser runtime as a harmless warning, or invents screenshots/video evidence.

## 7. Handoff boundary

**Prompt:** Package this project so another contributor can continue the work.

**Pass:** Provides goal, accepted baseline, changed files, run/verify steps, evidence location, known issues, and next recommendation while excluding environment files, credentials, caches, and unrelated material.

**Fail:** Copies all local files, treats a dependency directory as handoff, or exposes secrets to make the next step convenient.
