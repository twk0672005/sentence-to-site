from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
required = [
    root / "README.md",
    root / "LICENSE",
    root / "CONTRIBUTING.md",
    root / "SECURITY.md",
    root / "CODE_OF_CONDUCT.md",
    root / "requirements.txt",
    root / "skills" / "one-sentence-website" / "SKILL.md",
    root / "skills" / "adversarial-quality-loop" / "SKILL.md",
    root / "skills" / "cinematic-web-motion" / "SKILL.md",
    root / "references" / "quality-loop-roles.md",
    root / "references" / "reference-recreation.md",
    root / "references" / "website-motion-workflow.md",
    root / "references" / "project-intake.md",
    root / "references" / "evidence-and-handoff.md",
    root / "references" / "tooling.md",
    root / "scripts" / "verify_browser_artifact.py",
    root / "scripts" / "record_browser_scroll.py",
    root / "evals" / "acceptance-cases.md",
]
missing = [str(path.relative_to(root)) for path in required if not path.is_file() or not path.stat().st_size]
assert not missing, f"missing complete-kit public capabilities: {', '.join(missing)}"

release_files = [
    path for path in root.rglob("*")
    if path.is_file()
    and ".git" not in path.parts
    and "_internal" not in path.parts
    and "tests" not in path.parts
    and ".venv" not in path.parts
    and "__pycache__" not in path.parts
]
public_text = "\n".join(
    path.read_text(encoding="utf-8", errors="ignore")
    for path in release_files
    if path.suffix.lower() in {".md", ".py", ".txt"}
)
for forbidden in (
    "/root/",
    "Afuu",
    "Nova",
    "Hermes",
    "GoldPilot",
    "__COSMIC_",
):
    assert forbidden not in public_text, f"private implementation marker in release payload: {forbidden}"

assert "partial" in (root / "references" / "evidence-and-handoff.md").read_text(encoding="utf-8")
assert "blocked" in (root / "references" / "evidence-and-handoff.md").read_text(encoding="utf-8")
assert "## 6. Evidence verdict" in (root / "evals" / "acceptance-cases.md").read_text(encoding="utf-8")
assert "## 7. Handoff boundary" in (root / "evals" / "acceptance-cases.md").read_text(encoding="utf-8")
assert "prefers-reduced-motion" in (root / "skills" / "motion-choreography" / "SKILL.md").read_text(encoding="utf-8")
print("PASS: complete clean-room public-kit contract and privacy boundary")
