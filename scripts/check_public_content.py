"""Fail when public content contains common credentials or internal infrastructure."""

from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
targets = [root / "documentation", root / "landing", root / "README.md"]
rules = {
    "credential-like value": re.compile(r"ghp_|github_pat_|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
    "internal absolute path": re.compile(r"/kfs2/|/projects/(?:nmclps|lips)/|/home/[A-Za-z0-9._-]+/"),
    "cluster account": re.compile(r"--account[= ][A-Za-z0-9._-]+|default_account:\s*(?:nmclps|lips)"),
    "private host": re.compile(r"[A-Za-z0-9._-]+\.hpc\.(?:nlr|nrel)\.gov|\bkl[0-9]+\b"),
}
errors: list[str] = []
files: list[Path] = []
for target in targets:
    files.extend(target.rglob("*")) if target.is_dir() else files.append(target)
for path in files:
    if not path.is_file() or path.suffix.lower() == ".svg":
        continue
    try:
        lines = path.read_text().splitlines()
    except UnicodeDecodeError:
        continue
    for number, line in enumerate(lines, 1):
        for label, pattern in rules.items():
            if pattern.search(line):
                errors.append(f"{path.relative_to(root)}:{number}: {label}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Credential and internal-infrastructure scan passed")

