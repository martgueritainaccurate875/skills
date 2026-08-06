#!/usr/bin/env python3
"""Tests for the repository skill validator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_skills import validate_repository


class ValidateSkillsTest(unittest.TestCase):
    def write_skill(self, root: Path, directory: str, frontmatter: str) -> None:
        skill_dir = root / "skills" / directory
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(frontmatter, encoding="utf-8")

    def test_valid_scalar_and_block_descriptions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_skill(
                root,
                "alpha-skill",
                "---\nname: alpha-skill\ndescription: Alpha trigger.\n---\n",
            )
            self.write_skill(
                root,
                "beta-skill",
                "---\nname: beta-skill\ndescription: |\n  Beta trigger.\n---\n",
            )

            self.assertEqual(validate_repository(root), [])

    def test_reports_missing_file_and_invalid_frontmatter(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skills" / "missing-skill").mkdir(parents=True)
            self.write_skill(
                root,
                "wrong-directory",
                "---\nname: Wrong_Name\ndescription:\n---\n",
            )

            errors = validate_repository(root)

            self.assertEqual(len(errors), 4)
            self.assertTrue(any("missing SKILL.md" in error for error in errors))
            self.assertTrue(any("must match directory" in error for error in errors))
            self.assertTrue(any("lowercase kebab-case" in error for error in errors))
            self.assertTrue(any("non-empty description" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
