#!/usr/bin/env python3
"""Validate the required structure and frontmatter of repository skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return {}, [f"{path}: file is not valid UTF-8"]

    if not lines or lines[0] != "---":
        return {}, [f"{path}: YAML frontmatter must start on the first line"]

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path}: YAML frontmatter has no closing delimiter"]

    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:closing_index]:
        if not line or line[0].isspace() or line.lstrip().startswith("-"):
            if current_key is not None and line.strip():
                fields[current_key] = f"{fields[current_key]} {line.strip()}".strip()
            continue

        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match is None:
            current_key = None
            continue

        current_key = match.group(1)
        value = (match.group(2) or "").strip()
        fields[current_key] = "" if value in {"|", ">"} else value.strip("'\"")

    return fields, errors


def validate_skill(skill_dir: Path) -> tuple[str | None, list[str]]:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return None, [f"{skill_dir}: missing SKILL.md"]

    fields, errors = read_frontmatter(skill_file)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append(f"{skill_file}: frontmatter requires a non-empty name")
    elif name != skill_dir.name:
        errors.append(
            f"{skill_file}: name {name!r} must match directory {skill_dir.name!r}"
        )

    if name and SKILL_NAME_PATTERN.fullmatch(name) is None:
        errors.append(f"{skill_file}: name must use lowercase kebab-case")

    if not description:
        errors.append(f"{skill_file}: frontmatter requires a non-empty description")

    return name or None, errors


def validate_repository(root: Path) -> list[str]:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return [f"{skills_dir}: skills directory does not exist"]

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        return [f"{skills_dir}: no skill directories found"]

    errors: list[str] = []
    names: dict[str, Path] = {}
    for skill_dir in skill_dirs:
        name, skill_errors = validate_skill(skill_dir)
        errors.extend(skill_errors)
        if name is None:
            continue
        if name in names:
            errors.append(
                f"{skill_dir}: duplicate skill name {name!r}; first used by {names[name]}"
            )
        else:
            names[name] = skill_dir

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[4]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    skill_count = sum(1 for path in (root / "skills").iterdir() if path.is_dir())
    print(f"Validated {skill_count} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
