#!/usr/bin/env python3
"""Dependency-free project checks; not a full YAML/spec or behavioral validator."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP = {".git", "local", "dist", "work", "outputs", "__pycache__", ".venv", "node_modules"}


def public_files(root):
    return [p for p in root.rglob("*") if p.is_file() and not (set(p.relative_to(root).parts) & SKIP)]


def metadata(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"Missing frontmatter: {path}")
    header, body = text[4:].split("\n---\n", 1)
    fields = {}
    for line in header.splitlines():
        key, sep, value = line.partition(":")
        if not sep or key not in {"name", "description"} or key in fields:
            raise ValueError(f"Unsupported project metadata: {path}: {line}")
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        fields[key] = value
    if set(fields) != {"name", "description"}:
        raise ValueError(f"Expected name and description: {path}")
    if not NAME.fullmatch(fields["name"]) or len(fields["name"]) > 64:
        raise ValueError(f"Invalid name: {path}")
    if fields["name"] != path.parent.name:
        raise ValueError(f"Name/directory mismatch: {path}")
    if not 1 <= len(fields["description"]) <= 1024:
        raise ValueError(f"Invalid description length: {path}")
    if len(body.split()) > 900:
        raise ValueError(f"Entry exceeds 900-word project budget: {path}")
    if "[TODO:" in text:
        raise ValueError(f"Unfinished initializer: {path}")
    return fields, body


def package_check(directory):
    if directory.is_symlink():
        raise ValueError(f"Skill directory is a symlink: {directory}")
    fields, body = metadata(directory / "SKILL.md")
    for p in directory.rglob("*"):
        if p.is_symlink():
            raise ValueError(f"Symlink not allowed in package: {p}")
        if p.is_file() and p.suffix == ".md":
            for raw in LINK.findall(p.read_text(encoding="utf-8")):
                if "://" in raw or raw.startswith("#"):
                    continue
                target = (p.parent / raw.split("#")[0]).resolve()
                if not target.is_relative_to(directory.resolve()):
                    raise ValueError(f"Link escapes installed package: {p}: {raw}")
                if not target.is_file():
                    raise ValueError(f"Broken package link: {p}: {raw}")
    for ref in (directory / "references").glob("*.md"):
        if f"references/{ref.name}" not in body:
            raise ValueError(f"Reference not directly discoverable from entry: {ref}")
    return fields


def validate(root=ROOT):
    errors = []
    registry = json.loads((root / "registry.json").read_text())
    names = [item["name"] for item in registry["skills"]]
    if any(not name.startswith("brainkit-") for name in names):
        errors.append("All package names must use the brainkit- namespace")
    if len(names) != len(set(names)):
        errors.append("Duplicate registry name")
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if set(names) != actual:
        errors.append("Registry/skill coverage mismatch")
    for item in registry["skills"]:
        try:
            if item["entry"] != f"skills/{item['name']}/SKILL.md":
                raise ValueError(f"Invalid registry entry: {item['name']}")
            package_check(root / "skills" / item["name"])
        except (ValueError, OSError) as exc:
            errors.append(str(exc))
    files = public_files(root)
    for p in files:
        if p.suffix == ".json":
            try:
                json.loads(p.read_text())
            except (ValueError, OSError) as exc:
                errors.append(f"Invalid JSON {p}: {exc}")
        if p.suffix == ".md":
            for raw in LINK.findall(p.read_text()):
                if "://" in raw or raw.startswith("#"):
                    continue
                if not (p.parent / raw.split("#")[0]).is_file():
                    errors.append(f"Broken relative link {p}: {raw}")
    cases = json.loads((root / "evals/cases.json").read_text())["cases"]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate evaluation ID")
    for name in names:
        kinds = {case["kind"] for case in cases if case.get("skill") == name}
        if not {"positive", "negative"} <= kinds:
            errors.append(f"Missing positive/negative evaluations: {name}")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"PASS: {len(names)} packages, {len(files)} public files, {len(cases)} behavioral case definitions (not executed)")
    for name in names:
        _, body = metadata(root / "skills" / name / "SKILL.md")
        print(f"  {name}: {len(body.split())} entry words")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
