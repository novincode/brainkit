#!/usr/bin/env python3
"""Install selected self-contained packages without overwriting existing work."""
import argparse
import json
import shutil
import sys
from pathlib import Path

from validate import ROOT, NAME, package_check


def install(target, names, *, root=ROOT, dry_run=False):
    target = Path(target).expanduser()
    if target.is_symlink():
        raise ValueError("Target must not be a symlink")
    target = target.resolve()
    if target.is_relative_to((root / "skills").resolve()):
        raise ValueError("Do not install into the source skill tree")
    known = {x["name"] for x in json.loads((root / "registry.json").read_text())["skills"]}
    plan = []
    for name in dict.fromkeys(names):
        if not NAME.fullmatch(name) or name not in known:
            raise ValueError(f"Unknown skill: {name}")
        source = root / "skills" / name
        package_check(source)
        destination = target / name
        if destination.exists() or destination.is_symlink():
            raise FileExistsError(f"Refusing to overwrite: {destination}")
        plan.append((source, destination))
    if not plan:
        raise ValueError("Select at least one skill")
    for source, destination in plan:
        print(f"{'Would copy' if dry_run else 'Copy'} {source.name} -> {destination}")
    if dry_run:
        return
    target.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for source, destination in plan:
            destination.mkdir()  # exclusive reservation; never replace a concurrent install
            created.append(destination)
            shutil.copytree(source, destination, dirs_exist_ok=True)
    except Exception:
        for directory in reversed(created):
            shutil.rmtree(directory)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill", action="append")
    group.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    names = args.skill or [x["name"] for x in json.loads((ROOT / "registry.json").read_text())["skills"]]
    try:
        install(args.target, names, dry_run=args.dry_run)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Install failed: {exc}\n")


if __name__ == "__main__":
    main()
