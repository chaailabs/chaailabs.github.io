#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
rm -rf "${root}/_site" "${root}/build"
mkdir -p "${root}/_site/docs"
cp "${root}/landing/index.html" "${root}/_site/index.html"
cp "${root}/landing/logo.svg" "${root}/landing/logo-icon.svg" "${root}/_site/"
[[ ! -d "${root}/landing/assets" ]] || cp -R "${root}/landing/assets" "${root}/_site/assets"
mkdocs build --strict --config-file "${root}/mkdocs.yml"
cp -R "${root}/build/docs/." "${root}/_site/docs/"
touch "${root}/_site/.nojekyll"
echo "Built ${root}/_site"

