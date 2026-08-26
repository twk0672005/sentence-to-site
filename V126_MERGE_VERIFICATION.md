# V1.2.6 Merge Verification

## Source

Base package:

```text
afuu_website_animation_workflow_kit_v1_2_4_readme_inheritance.zip
```

This v1.2.6 package keeps the v1.2.4 full-source package as the base.

## What changed

Added / strengthened:

```text
workflows/file-architecture-workflow.md
docs/workflow-kit-maintenance-map.md
README.md
WORKFLOW_COMPLETENESS_AUDIT.md
```

## Main merge decision

The complete file architecture workflow was merged into:

```text
workflows/file-architecture-workflow.md
```

The wider maintenance map / integration workflow was preserved as:

```text
docs/workflow-kit-maintenance-map.md
```

## Verification performed

Fresh verification was run after packaging.

Results:

```text
required_missing: []
forbidden_files: []
root_forbidden_zip_members: []
decode_bad: []
secret_like_hit_count: 0
zip_integrity_error: null
```

Browser workflow smoke test:

```text
script: scripts/verify_browser_artifact.py
target: dummy static site
result: ok true
serveMode: static-root
```

File architecture markers verified:

```text
ownership_model: true
recommended_full_structure: true
safe_migration: true
bad_architectures: true
evidence_linked: true
```

## Website + animation workflow smoke update

Additional workflow smoke testing was run after the file-architecture merge.

Website workflow smoke:

```text
workflow: workflows/website-workflow.md
result: PASS
method: build small static landing page -> browser evidence -> screenshot evaluator -> patch one visible weakness -> final evidence
```

Animation workflow smoke:

```text
workflow: workflows/animation-workflow.md
result: PASS after script fix
method: add scroll progress hook -> screenshots -> MP4 recording -> contact sheet -> readback
```

Script fix made during the animation smoke:

```text
scripts/record_browser_scroll.py
```

Reason:

```text
The original ffmpeg filter over-compressed the recorded video into a split-second timelapse. The script now preserves human-reviewable duration and generates contact-sheet.jpg automatically.
```

Verified final animation evidence shape:

```text
mp4 duration: about 6.9 seconds
contact sheet: generated
readback progress: 1
console/browser evidence: clean in smoke test
```

## Boundary

This is still a workflow inheritance kit, not a starter app.

It intentionally keeps the v1.2.4 full-source raw included skills. For Telegram/iPhone-safe external delivery, generate a separate ASCII-safe handoff edition.
