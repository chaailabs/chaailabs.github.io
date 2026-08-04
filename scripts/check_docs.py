"""Validate navigation targets and local Markdown links without external dependencies."""

from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
docs = root / "documentation"
errors: list[str] = []

config = (root / "mkdocs.yml").read_text()
for target in re.findall(r"(?:^|:\s)([A-Za-z0-9_./-]+\.md)\s*$", config, re.MULTILINE):
    if not (docs / target).is_file():
        errors.append(f"missing navigation target: {target}")

link_pattern = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
for page in docs.rglob("*.md"):
    text = page.read_text()
    for raw in link_pattern.findall(text):
        target = raw.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        resolved = (page.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{page.relative_to(root)}: broken link {raw}")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print("Navigation and local Markdown links passed")

