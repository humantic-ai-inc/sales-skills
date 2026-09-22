#!/usr/bin/env python3
"""Check every skill has valid frontmatter and the sections every skill must carry."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "skills"
REQUIRED = ["## What you need", "## Steps", "## If Humantic is not connected",
            "## Humantic tools this skill uses", "## Rules"]
errors = []
for skill in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    f = skill / "SKILL.md"
    if not f.exists():
        errors.append(f"{skill.name}: missing SKILL.md"); continue
    text = f.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{skill.name}: no frontmatter"); continue
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    name = fm.get("name", "").strip(); desc = fm.get("description", "").strip()
    if name != skill.name: errors.append(f"{skill.name}: name '{name}' does not match folder")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name): errors.append(f"{skill.name}: invalid name")
    if not desc or len(desc) > 1024: errors.append(f"{skill.name}: description empty or over 1024 chars")
    if "<" in desc or ">" in desc: errors.append(f"{skill.name}: angle brackets in description")
    for s in REQUIRED:
        if s not in text: errors.append(f"{skill.name}: missing section '{s}'")
    if not (skill / "README.md").exists(): errors.append(f"{skill.name}: missing README.md")
    print(f"ok  {skill.name}  ({len(desc)} char description)")
if errors:
    print("\n".join(errors)); sys.exit(1)
print("All skills valid.")
