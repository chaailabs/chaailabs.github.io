#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python "${root}/scripts/check_public_content.py"
python "${root}/scripts/check_docs.py"
echo "Public-content validation passed"
