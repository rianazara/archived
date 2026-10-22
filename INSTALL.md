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

## Ingestion toolchain (optional)

Capture, queueing and `.eml`/mbox/text parsing need nothing beyond the
standard library. PDFs, Word documents and YouTube subtitles need a local
venv:

```bash
python3 -m venv .venv
.venv/bin/python3 -m pip install -U pip yt-dlp pypdf python-docx html2text
```

`scripts/extract.py` re-execs itself under `.venv/` when it exists, so you
never have to activate it. Until the venv is built, items needing it stay
`pending` and get picked up automatically afterwards.

## Requirements

- `git`
- `python3` — standard library only for `rebuild_index.py`, `capture.py` and
  `scan_drop.py`
- the venv above, only for PDF / Word / YouTube extraction

Known constraint: `yt-dlp` deprecates Python 3.9 (this machine's system
Python). It installs and runs today, but a newer Python will eventually be
needed for that one adapter.
