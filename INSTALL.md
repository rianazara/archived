# Install

1. Clone this repo wherever you keep it, e.g.:
   ```
   git clone <remote-url> ~/memory
   ```
2. Symlink the skill into Claude Code's skills directory so it's picked up
   automatically:
   ```
   mkdir -p ~/.claude/skills
   ln -s ~/memory ~/.claude/skills/archived
   ```
3. Open a Claude Code session anywhere and use the phrases from the
   [README](README.md) quick start — Claude will read `SKILL.md` and operate
   on the entries in this repo.

## New machine

Repeat step 1–2 above, then run `Sync my notes` (or `scripts/sync.sh`
directly) to pull the latest entries.

## Requirements

- `git`
- `python3` (used by `scripts/rebuild_index.py`, standard library only — no
  extra packages to install)
