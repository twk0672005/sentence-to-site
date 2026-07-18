# Project intake

Use this before changing a non-trivial existing site. The goal is to understand the host project, not to force a replacement architecture.

## Capture only what matters

- **Runtime:** framework, package manager, development command, build command, preview command.
- **Entry and routes:** main page entry, route structure, content location, section/component location.
- **Visual system:** token/style source, assets, accepted screenshot or recording, first visible weakness.
- **Motion system:** existing CSS, Motion, GSAP, canvas, or WebGL owner; current cleanup and fallback behavior.
- **Verification:** current test/build commands and the real browser URL or static output directory.
- **Boundaries:** files not to touch, access-controlled areas, release/deployment limits, and rollback point.

## One-sentence readback

Before implementation, be able to say:

```text
This is a <framework> project; <entry> is the entry, <location> owns content,
<location> owns motion, and this change will be verified with <method>.
```

If any part is unknown, inspect it. Do not infer it from the framework name.

## Ownership model

Use ownership when it makes change safer:

```text
content owns meaning
components own layout
motion owns movement
scene owns WebGL/canvas lifecycle
styles own tokens and responsive rules
scripts own verification
reports own generated evidence
```

A small component-local interaction can stay local. Create folders only when they make the next change easier to find.

## Stop signs

Pause before replacing the framework, installing paid services, changing deployment/configuration, exposing a preview publicly, or touching credentials. Preserve the strongest accepted baseline before a meaningful visual change.
