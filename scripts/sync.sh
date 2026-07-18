#!/usr/bin/env bash
# Pull/rebase then push local changes. Stops on conflict instead of resolving silently.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

python3 scripts/rebuild_index.py

if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "Update entries $(date +%Y-%m-%d)"
fi

git pull --rebase
git push
