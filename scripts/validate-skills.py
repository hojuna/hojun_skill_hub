#!/usr/bin/env python3
"""Validate basic Agent Skills structure, no third-party dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent / ".agents" / "skills"
errors = []
skills = sorted(p for p in ROOT.iterdir() if p.is_dir()) if ROOT.exists() else []
if not skills:
    errors.append(f"no skills found at {ROOT}")
for folder in skills:
    path = folder / "SKILL.md"
    if not path.is_file():
        errors.append(f"{folder.name}: missing SKILL.md")
        continue
    data = path.read_text(encoding="utf-8")
    if not data.startswith("---\n"):
        errors.append(f"{folder.name}: YAML frontmatter not found")
        continue
    parts = data.split("---\n", 2)
    if len(parts) < 3:
        errors.append(f"{folder.name}: frontmatter closing delimiter missing")
        continue
    header = parts[1]
    match_name = re.search(r"(?m)^name:\s*([^\n]+)$", header)
    match_description = re.search(r"(?m)^description:\s*([^\n]+)$", header)
    name = match_name.group(1).strip() if match_name else ""
    desc = match_description.group(1).strip() if match_description else ""
    if name != folder.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{folder.name}: invalid/mismatched name {name!r}")
    if not desc or len(desc) > 1024:
        errors.append(f"{folder.name}: description missing or too long")
    if not parts[2].strip():
        errors.append(f"{folder.name}: instruction body empty")
if errors:
    for issue in errors:
        print("ERROR:", issue, file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(skills)} Skill manifests have valid basic structure")
