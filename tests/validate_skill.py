from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
router = root / "skills" / "cinematic-web-motion" / "SKILL.md"
modules = {
    "visual": root / "skills" / "visual-story-direction" / "SKILL.md",
    "intake": root / "skills" / "website-motion-intake" / "SKILL.md",
    "motion": root / "skills" / "motion-choreography" / "SKILL.md",
    "evidence": root / "skills" / "browser-evidence" / "SKILL.md",
    "handoff": root / "skills" / "delivery-handoff" / "SKILL.md",
}
readme = root / "README.md"
license_file = root / "LICENSE"
evals = root / "evals" / "acceptance-cases.md"

for path in (router, *modules.values(), readme, license_file, evals):
    assert path.is_file() and path.stat().st_size > 0, f"missing package file: {path}"

for label, path in {"router": router, **modules}.items():
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"missing YAML frontmatter: {label}"
    frontmatter, body = text.split("---\n", 2)[1:]
    fields = dict(
        line.split(": ", 1)
        for line in frontmatter.strip().splitlines()
        if ": " in line
    )
    assert fields.get("name"), f"missing skill name: {label}"
    description = fields.get("description", "")
    assert description.startswith("Use when"), f"description must be trigger-focused: {label}"
    assert len(frontmatter) <= 1024, f"frontmatter exceeds guidance: {label}"

expected_boundaries = {
    "router": "Do not load every module for a small CSS or copy correction.",
    "visual": "Avoid generic bento layouts",
    "intake": "The existing stack and strongest accepted baseline outrank a preferred architecture.",
    "motion": "Give each node one transform owner.",
    "evidence": "A build, HTTP 200, or one hero screenshot does not prove",
    "handoff": "Exclude credentials, environment files, private assets",
}
for label, phrase in expected_boundaries.items():
    path = router if label == "router" else modules[label]
    assert phrase in path.read_text(encoding="utf-8"), f"missing decision boundary for {label}: {phrase}"

readme_text = readme.read_text(encoding="utf-8")
for phrase in ("skills/catalog.json", "docs/INSTALLATION.md", "docs/ARCHITECTURE.md", "browser-evidence"):
    assert phrase in readme_text, f"README missing library entry: {phrase}"
for heading in ("## 6. Evidence verdict", "## 7. Handoff boundary"):
    assert heading in evals.read_text(encoding="utf-8"), f"missing acceptance case: {heading}"

# Scan intended release text, not local environments, tests, or internal source notes.
release_files = [
    path for path in root.rglob("*")
    if path.is_file()
    and ".git" not in path.parts
    and ".venv" not in path.parts
    and "_internal" not in path.parts
    and "tests" not in path.parts
    and "__pycache__" not in path.parts
    and (path.suffix.lower() in {".md", ".py", ".txt", ".json", ".yml", ".yaml"} or path.name == "LICENSE")
]
public_text = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in release_files)
for pattern, label in (
    (r"(?:sk|ghp|github_pat)_[A-Za-z0-9_\-]{20,}", "secret-like token"),
    (r"(?i)(?:api[_-]?key|bot[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}", "credential assignment"),
):
    assert not re.search(pattern, public_text), f"{label} found"

print("PASS: module boundaries, acceptance cases, and public-boundary scan")
