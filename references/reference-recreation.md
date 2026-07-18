# Reference-driven recreation

When the brief is "make it look/move like this site or video", extract the *mechanics* of the reference — never its brand, copy, code, or protected assets.

## Pipeline

1. **Verify the source.** Confirm the URL or file actually loads and is the thing the user meant. If the reference is unreachable, say so and ask for a substitute or proceed with a declared approximation — never analyze from imagination while implying you watched it.
2. **Sample real frames.** For motion references, capture frames at meaningful moments (opening state, mid-transition, settled state) and build a contact sheet. Analysis of a video you did not sample is a guess.
3. **Extract mechanics, not identity.**
   - *Learnable*: pacing, easing character, layout rhythm, scroll choreography structure, layering/depth tricks, transition grammar, density of motion.
   - *Do not copy*: logos, brand names, distinctive illustrations, copy text, proprietary code, exact color-and-type identity that makes the reference recognizable as that brand.
4. **Label confidence.** Mark each extracted observation as `observed` (seen in a sampled frame), `inferred` (likely from context), or `assumed` (a default you chose). Downstream decisions should know which is which.
5. **Translate to a build plan.** Map each learnable mechanic to a concrete technique in this kit's lanes (CSS, Motion, GSAP, canvas, WebGL) via `motion-choreography`.

## Honesty rules

- Never claim frame-level analysis without frames on disk.
- If the reference's key effect cannot be reproduced in the chosen stack, say so during planning, not after shipping a lookalike that misses the point.
- The recreation must pass the same browser evidence bar as any other build; "it resembles the reference" is an Evaluator judgement made on screenshots, not a self-declared success.
