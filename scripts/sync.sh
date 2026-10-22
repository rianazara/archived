#!/usr/bin/env bash
# Pull/rebase then push local changes. Stops on conflict instead of resolving silently.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

python3 scripts/rebuild_index.py

# Entries can be derived from personal mail or exports, and this repo is
# pushed, so show what would go up and get a yes first.
if [[ -n "$(git status --porcelain)" ]]; then
  echo "About to commit and push:"
  git status --short
  echo
  if [[ -t 0 ]]; then
    read -r -p "Push these to the remote? [y/N] " reply
    [[ "$reply" == [yY] ]] || { echo "Stopped. Nothing pushed."; exit 1; }
  else
    echo "Not a terminal — refusing to push unreviewed changes." >&2
    exit 1
  fi
  git add -A
  git commit -m "Update entries $(date +%Y-%m-%d)"
fi

git pull --rebase
git push
