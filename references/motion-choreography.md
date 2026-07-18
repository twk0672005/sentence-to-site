# Motion choreography

## Route the motion

- Use CSS for small polish and state that naturally belongs to the component.
- Use a UI motion library for entry, exit, layout, hover, focus, and gesture state.
- Use a scroll system for pinned or scrubbed narrative progression.
- Use canvas or WebGL only when a scene, depth, or simulation is itself part of the experience.

## One transform owner

A node gets one transform writer. If scroll, hover, and scene movement must coexist, split wrappers so each owner controls a different node. Avoid competing `transform`, `opacity`, or scroll listeners.

## Define the complete behavior

For meaningful motion, specify trigger, enter, active, exit, cleanup, mobile alternative, and reduced-motion alternative. Scroll choreography needs clear start/end boundaries and cleanup on unmount or route change.

## Mobile is not a shrunken desktop timeline

Keep the narrative beat, but shorten, stack, simplify, or make static any choreography that harms reading, performance, or touch interaction. `prefers-reduced-motion` should preserve meaning rather than merely disabling code.
