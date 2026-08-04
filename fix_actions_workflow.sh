#!/usr/bin/env bash
set -euo pipefail
source_file="/projects/nmclps/chaailabs-site-integration/.github/workflows/pages.yml"
target_repo="/projects/lips/Chaai/website"
branch="integrate-hpca-docs"
cd "${target_repo}"
[[ "$(git branch --show-current)" == "${branch}" ]] || { echo "ERROR: expected ${branch}" >&2; exit 1; }
[[ -z "$(git status --porcelain)" ]] || { echo "ERROR: working tree is not clean" >&2; exit 1; }
cp "${source_file}" .github/workflows/pages.yml
git add .github/workflows/pages.yml
git --no-pager diff --cached
git commit -m "Fix documentation workflow dependency cache"
git push origin "${branch}"
echo "Workflow correction pushed; GitHub will rerun pull-request checks."
