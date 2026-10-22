# archived

My public-ish memory. A personal knowledge base that runs as a Claude Code
skill: I tell Claude what I learned, it writes a markdown file for it, and
everything stays readable and portable as plain text — no database, no
lock-in.

## Quick start

Inside a Claude Code session in this repo:

- `Store this: <concept>` — save a new concept (checked against existing
  entries first, to avoid duplicates)
- `Store this: <link>` — paste an article/Substack URL and Claude fetches
  and summarizes it instead of you typing it out
- `Ingest my inbox` — process everything captured since last time
- `What do I have on <topic>?` — browse/search stored entries
- `Let's revise <topic>` — walk through everything stored on a topic
- `Quiz me on <topic>` — get quizzed using only what's actually stored
- `Sync my notes` — pull/push across devices via git

A scheduled task (`archived-daily-brief`) runs every morning with a digest
of what got stored in the last day plus a quiz question from older entries.

## Capturing from anywhere

Capture is instant and offline — it just queues the thing. Processing
happens later, in bulk.

```bash
python3 scripts/capture.py https://example.com/article   # any public URL
python3 scripts/capture.py https://youtu.be/VIDEOID      # YouTube
python3 scripts/capture.py ~/Downloads/paper.pdf         # a file
```

Or drop files into `inbox/drop/` and let the queue pick them up:

| Source | How it gets in |
|---|---|
| Articles, newsletters on the web | `capture.py <url>` |
| Gmail newsletters | in Gmail, ⋮ → *Download message* → drop the `.eml` in `inbox/drop/` (or a Takeout mbox for bulk) |
| YouTube | `capture.py <url>` — pulls subtitles, no video (see caveat below) |
| Instagram saves | Instagram → *Download Your Information* → drop the zip; only `saved_posts.json` is read |
| PDFs, Word docs, saved pages | drop them in `inbox/drop/` |

Then `python3 scripts/scan_drop.py && python3 scripts/extract.py`, and ask
Claude to `Ingest my inbox`. Anything that can't be read automatically is
flagged for one dictated line rather than guessed at.

**YouTube caveat:** YouTube currently withholds caption tracks from
unauthenticated requests ("PO token required"), so many videos land as
`needs_dictation` even when captions exist. Nothing in this repo works
around that.

## Layout

```
SKILL.md              # the skill definition Claude reads
entries/<topic>/*.md   # one markdown file per concept
INDEX.md              # auto-generated catalog — don't hand-edit
scripts/              # rebuild_index.py, sync.sh
```

See [INSTALL.md](INSTALL.md) for setup on a new machine.
