# archived

My public-ish memory. A personal knowledge base that runs as a Claude Code
skill: I tell Claude what I learned, it writes a markdown file for it, and
everything stays readable and portable as plain text — no database, no
lock-in.

## Quick start

Inside a Claude Code session in this repo:

- `Store this: <concept>` — save a new concept (checked against existing
  entries first, to avoid duplicates)
- `What do I have on <topic>?` — browse/search stored entries
- `Let's revise <topic>` — walk through everything stored on a topic
- `Quiz me on <topic>` — get quizzed using only what's actually stored
- `Sync my notes` — pull/push across devices via git

## Layout

```
SKILL.md              # the skill definition Claude reads
entries/<topic>/*.md   # one markdown file per concept
INDEX.md              # auto-generated catalog — don't hand-edit
scripts/              # rebuild_index.py, sync.sh
```

See [INSTALL.md](INSTALL.md) for setup on a new machine.
