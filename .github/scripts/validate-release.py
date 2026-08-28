#!/usr/bin/env python3
"""Validate and reproducibly package the workflow-kit release contract."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import py_compile
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import unquote


DEFAULT_ROOT = Path(__file__).resolve().parents[2]
ROOT = Path(os.environ.get("WORKFLOW_KIT_ROOT", str(DEFAULT_ROOT))).resolve()
TEXT_SUFFIXES = {".md", ".py", ".json", ".txt", ".yml", ".yaml", ".html"}
IGNORED_PARTS = {
    ".git",
    ".omc",
    ".venv",
    "__pycache__",
    "distribution",
    "node_modules",
    "reports",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(relative: str, issues: list[str]) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        issues.append(f"{relative}: invalid UTF-8 JSON: {exc}")
        return {}


def repository_files() -> set[str]:
    files: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.suffix == ".pyc":
            continue
        files.add(relative.as_posix())
    return files


def sensitive_entries() -> list[str]:
    skip = {".git", ".omc", ".venv", "distribution", "node_modules", "reports"}
    names = {
        ".aws",
        ".env",
        ".netrc",
        ".npmrc",
        ".pypirc",
        ".ssh",
        "credentials.json",
        "id_ed25519",
        "id_rsa",
        "service-account.json",
    }
    suffixes = {".key", ".pem", ".p12", ".pfx"}
    found: list[str] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in skip for part in relative.parts):
            continue
        if path.is_symlink():
            found.append("symlink:" + relative.as_posix())
        if path.name in names or path.name.startswith(".env."):
            found.append(relative.as_posix())
        if path.is_file() and path.suffix.lower() in suffixes:
            found.append(relative.as_posix())
    return sorted(set(found))


def cache_artifacts() -> list[str]:
    found: list[str] = []
    skip = {".git", ".omc", ".venv", "distribution", "node_modules", "reports"}
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in skip for part in relative.parts):
            continue
        if "__pycache__" in relative.parts or (path.is_file() and path.suffix == ".pyc"):
            found.append(relative.as_posix())
    return sorted(found)


def heading_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[\x60*_~]", "", value).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def markdown_anchors(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    anchors = set(re.findall(r"""(?:id|name)=["']([^"']+)["']""", text))
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        slug = heading_slug(match.group(1))
        if not slug:
            continue
        count = counts.get(slug, 0)
        anchors.add(slug if count == 0 else f"{slug}-{count}")
        counts[slug] = count + 1
    return anchors


def markdown_links(relative: str, text: str) -> list[str]:
    missing: list[str] = []
    parent = (ROOT / relative).parent
    for raw in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = raw.strip().strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        path_part, separator, fragment = target.partition("#")
        resolved = (parent / path_part).resolve() if path_part else (ROOT / relative).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            missing.append(f"{relative}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            missing.append(f"{relative}: missing link target: {target}")
            continue
        if separator and fragment and resolved.suffix.lower() == ".md":
            anchor = unquote(fragment)
            if anchor not in markdown_anchors(resolved):
                missing.append(f"{relative}: missing fragment target: {target}")
    return missing


def allowed_repository_path(path: str, allowed: set[str], prefixes: list[str]) -> bool:
    if path in allowed:
        return True
    return any(path.startswith(prefix) for prefix in prefixes)


def deterministic_zip(
    distribution_files: list[str], output_dir: Path | None
) -> tuple[str, int, int, str]:
    with tempfile.TemporaryDirectory() as raw:
        temp = Path(raw)
        package = temp / "sentence-to-site-v1.4.0.zip"
        hashes = {
            relative: sha256((ROOT / relative).read_bytes())
            for relative in distribution_files
        }
        sums = "".join(f"{hashes[path]}  {path}\n" for path in sorted(hashes))
        expected_names = sorted(distribution_files) + ["SHA256SUMS"]

        with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for relative in sorted(distribution_files):
                info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, (ROOT / relative).read_bytes())
            sums_info = zipfile.ZipInfo("SHA256SUMS", date_time=(1980, 1, 1, 0, 0, 0))
            sums_info.compress_type = zipfile.ZIP_DEFLATED
            sums_info.external_attr = 0o100644 << 16
            archive.writestr(sums_info, sums.encode("utf-8"))

        with zipfile.ZipFile(package) as archive:
            names = sorted(archive.namelist())
            if names != sorted(expected_names):
                raise AssertionError(f"ZIP entries differ: {names}")
            if archive.testzip() is not None:
                raise AssertionError(f"ZIP CRC failure: {archive.testzip()}")
            for relative in distribution_files:
                if sha256(archive.read(relative)) != hashes[relative]:
                    raise AssertionError(f"ZIP byte mismatch: {relative}")
            if archive.read("SHA256SUMS").decode("utf-8") != sums:
                raise AssertionError("ZIP SHA256SUMS mismatch")

        package_hash = sha256(package.read_bytes())
        package_bytes = package.stat().st_size
        if output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(package, output_dir / package.name)
            (output_dir / "SHA256SUMS").write_text(sums, encoding="utf-8")
            (output_dir / f"{package.name}.sha256").write_text(
                f"{package_hash}  {package.name}\n", encoding="utf-8"
            )
        return package.name, package_bytes, len(expected_names), package_hash


def validate(output_dir: Path | None = None) -> tuple[list[str], dict[str, object]]:
    issues: list[str] = []
    manifest = read_json("kit-manifest.json", issues)
    distribution = manifest.get("distributionFiles", [])
    repository_only = manifest.get("repositoryOnly", {})
    required_repo = repository_only.get("requiredFiles", []) if isinstance(repository_only, dict) else []
    prefixes = repository_only.get("allowedPrefixes", []) if isinstance(repository_only, dict) else []

    if manifest.get("schemaVersion") != 1:
        issues.append("kit-manifest.json: schemaVersion must be 1")
    if manifest.get("version") != "1.4.0":
        issues.append("kit-manifest.json: version must be 1.4.0")
    if manifest.get("productType") != "reference-kit":
        issues.append("kit-manifest.json: productType must be reference-kit")
    if not isinstance(distribution, list) or not distribution:
        issues.append("kit-manifest.json: distributionFiles must be a non-empty list")
        distribution = []
    if len(distribution) != len(set(distribution)) or distribution != sorted(distribution):
        issues.append("kit-manifest.json: distributionFiles must be unique and sorted")
    if not isinstance(required_repo, list) or not isinstance(prefixes, list):
        issues.append("kit-manifest.json: repositoryOnly contract is malformed")
        required_repo, prefixes = [], []

    required = set(distribution) | set(required_repo)
    current = repository_files()
    missing = sorted(path for path in required if path not in current)
    unexpected = sorted(
        path for path in current if not allowed_repository_path(path, required, prefixes)
    )
    if missing:
        issues.append("missing required files: " + ", ".join(missing))
    if unexpected:
        issues.append("unexpected repository files: " + ", ".join(unexpected))

    texts: dict[str, str] = {}
    for relative in sorted(current):
        path = ROOT / relative
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            texts[relative] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            issues.append(f"{relative}: invalid UTF-8: {exc}")

    corpus = "\n".join(texts.values())
    for pattern, label in (
        (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", "private-key block"),
        (r"(?:ghp|github_pat)_[A-Za-z0-9_-]{20,}", "GitHub token"),
        (r"sk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}", "API key"),
        (
            r"(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*[\"']?"
            r"(?!\[REDACTED\])[A-Za-z0-9_./+\-]{16,}",
            "credential assignment",
        ),
        (r"[A-Za-z]:\\Users\\[^\\\s]+", "absolute Windows user path"),
        (r"(?:^|[\s(])/(?:root|home)/[^\s)]+", "absolute Unix home path"),
    ):
        if re.search(pattern, corpus, flags=re.MULTILINE):
            issues.append(f"tracked text contains {label}")
    if (ROOT / "AGENTS.md").exists() or (ROOT / "CLAUDE.md").exists():
        issues.append("root AGENTS.md/CLAUDE.md would override a recipient project")
    sensitive = sensitive_entries()
    if sensitive:
        issues.append("sensitive or escaping entries found: " + ", ".join(sensitive[:8]))
    caches = cache_artifacts()
    if caches:
        issues.append("cache artifacts found: " + ", ".join(caches[:8]))

    for relative, text in texts.items():
        if relative.endswith(".md"):
            issues.extend(markdown_links(relative, text))

    readme = texts.get("README.md", "")
    baseline = texts.get("CURRENT_BASELINE.md", "")
    skills = read_json("included-skills/SKILLS_MANIFEST.json", issues)
    three_lock = read_json("included-skills/THREEJS_SOURCE_LOCK.json", issues)
    if "v1.4.0" not in readme:
        issues.append("README.md does not declare v1.4.0")
    if "v1.4.0" not in baseline:
        issues.append("CURRENT_BASELINE.md does not declare v1.4.0")
    if skills.get("version") != "1.4.0-truthful-evidence-core":
        issues.append("SKILLS_MANIFEST.json version drift")
    optional = skills.get("optional_skills", [])
    if not isinstance(optional, list) or len(optional) != len(set(optional)):
        issues.append("SKILLS_MANIFEST.json optional_skills must be a unique list")
    if three_lock.get("workflowVersion") != "1.4.0":
        issues.append("THREEJS_SOURCE_LOCK.json workflowVersion drift")

    core_markers = {
        "workflows/website-workflow.md": [
            "Product truth trace",
            "Preservation map",
            "Session budget",
            "PASS / PARTIAL / FAIL / WAITING_FOR_NOVA",
        ],
        "workflows/animation-workflow.md": [
            "Micro Motion",
            "Choreographed Motion",
            "Cinematic WebGL",
            "render on demand",
            "Temporal evidence",
        ],
        "workflows/evidence-gate.md": [
            "Evidence types",
            "Status vocabulary",
            "PASS / PARTIAL / FAIL / WAITING_FOR_NOVA",
        ],
    }
    for relative, markers in core_markers.items():
        text = texts.get(relative, "")
        for marker in markers:
            if marker not in text:
                issues.append(f"{relative}: missing semantic marker {marker!r}")

    with tempfile.TemporaryDirectory() as cache_raw:
        cache = Path(cache_raw)
        for relative in sorted(current):
            if not relative.endswith(".py"):
                continue
            try:
                py_compile.compile(
                    str(ROOT / relative),
                    doraise=True,
                    cfile=str(cache / (relative.replace("/", "__") + "c")),
                )
            except py_compile.PyCompileError as exc:
                issues.append(f"{relative}: Python compile failed: {exc}")

    package_summary: dict[str, object] = {}
    if not issues:
        try:
            name, size, entries, package_hash = deterministic_zip(distribution, output_dir)
            package_summary = {
                "name": name,
                "bytes": size,
                "entries": entries,
                "sha256": package_hash,
            }
        except Exception as exc:
            issues.append(f"distribution package verification failed: {exc}")

    summary = {
        "version": manifest.get("version"),
        "repositoryFiles": len(current),
        "distributionFiles": len(distribution),
        "issues": len(issues),
        "package": package_summary,
    }
    return issues, summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    issues, summary = validate(args.output_dir.resolve() if args.output_dir else None)
    if issues:
        print(json.dumps({"verdict": "FAIL", "summary": summary, "issues": issues}, indent=2))
        return 1
    print(json.dumps({"verdict": "PASS", "summary": summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
