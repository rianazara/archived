#!/usr/bin/env bash
# Pull/rebase then push local changes. Stops on conflict instead of resolving
# silently, and confirms before anything leaves the machine.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

confirm() {
  if [[ ! -t 0 ]]; then
    echo "Not a terminal — refusing to proceed unreviewed." >&2
    exit 1
  fi
  local reply
  read -r -p "$1 [y/N] " reply
  [[ "$reply" == [yY] ]] || { echo "Stopped."; exit 1; }
}

python3 scripts/rebuild_index.py

if [[ -n "$(git status --porcelain)" ]]; then
  echo "Uncommitted changes:"
  git status --short
  echo
  confirm "Commit these?"
  git add -A
  git commit -m "Update entries $(date +%Y-%m-%d)"
fi

git pull --rebase

# Entries can be derived from personal mail or exports and this repo is public,
# so review what's actually going out — including commits made earlier, which a
# working-tree check would miss entirely.
upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || true)"
if [[ -z "$upstream" ]]; then
  echo "No upstream set for $(git branch --show-current) — nothing to push against." >&2
  exit 1
fi

if [[ -z "$(git log --oneline "$upstream"..HEAD)" ]]; then
  echo "Already in sync with $upstream. Nothing to push."
  exit 0
fi

echo "About to push to $upstream:"
git log --oneline "$upstream"..HEAD
echo
git diff --stat "$upstream"..HEAD
echo
confirm "Push these?"

git push
