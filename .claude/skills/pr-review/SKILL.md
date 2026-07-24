---
name: pr-review
description: Review skill pull requests for repository structure, metadata, safety, scope, and README registration. Use before approving or merging any skill contribution.
license: MIT
metadata:
  version: "1.0.0"
  category: repository-maintenance
---

# Skill Pull Request Review

Review the complete pull request diff and contributor discussion before deciding
whether a skill is ready to merge.

## Required Checks

1. Run `python .claude/skills/pr-review/scripts/validate_skills.py`.
2. Confirm the skill directory and frontmatter `name` match.
3. Confirm the description states when the skill should activate.
4. Check that examples contain no credentials or private data.
5. Verify scripts read secrets from environment variables.
6. Confirm scripts fail with actionable errors and document their dependencies.
7. Confirm English and Chinese README tables register new community skills.
8. Check links, file paths, and commands against the submitted tree.
9. Reject generated files, archives, or data blobs that do not belong in a skill.
10. Confirm the change has one clear purpose and does not duplicate an existing skill.

## Review Output

Report each blocking finding with its file, line, impact, and specific repair.
Separate optional improvements from merge blockers. If all checks pass, state the
commands run and the files reviewed.
