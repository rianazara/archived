---
name: archived
description: Personal knowledge base. Store concepts you learn as plain markdown, browse or search them, revise a topic, or quiz yourself. Use when the user says things like "store this", "what do I have on X", "let's revise X", or "quiz me on X".
---

# archived

A personal knowledge base that lives in this repo as plain markdown. Claude is the
interface for writing and retrieving entries; the files are the source of truth and
stay fully readable without Claude.

## Layout

```
entries/<topic>/<slug>.md   # one concept per file
INDEX.md                    # generated catalog, do not hand-edit
scripts/rebuild_index.py    # regenerates INDEX.md from entries/
scripts/sync.sh             # git add/commit/pull --rebase/push
```

Each entry is a markdown file with YAML frontmatter:

```markdown
---
title: Short title
topic: topic-slug
tags: [tag-one, tag-two]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

Body of the concept in the user's own words. Prefer a few short paragraphs
or a tight bullet list over an exhaustive writeup.
```

`topic` becomes the subfolder under `entries/`. `slug` is a short kebab-case
filename derived from the title, unique within the topic.

## Modes

### STORE — "Store this: …" / "I just learned that …"

1. Read `INDEX.md` and skim existing entries in the likely topic folder for
   overlap. If a close match exists, ask whether to update that entry instead
   of creating a duplicate.
2. Pick or confirm a `topic` (reuse an existing one when it fits).
3. Write the entry file with frontmatter as above. Keep the body faithful to
   what the user actually said — don't pad it with material they didn't
   provide, and don't strip out specifics they gave.
4. Run `python3 scripts/rebuild_index.py`.
5. Confirm what was stored and where, in one line.

### BROWSE — "What do I have on X?" / "Show me my notes on X"

Search `entries/` (filenames, frontmatter tags, and body text) for X. List
matches grouped by topic with a one-line summary each. If nothing matches,
say so plainly rather than guessing.

### REVISE — "Let's revise X" / "Refresh me on X"

Pull every entry under the matching topic (or matching tag if no topic
matches), and walk the user through them as a review: summarize each, then
ask if anything has changed or should be expanded. Offer to update entries
based on what comes up, following the STORE flow.

### QUIZ — "Quiz me on X"

Generate questions from the stored entries under topic/tag X — not from
outside knowledge. Ask one at a time, wait for the answer, then confirm or
correct using the entry as ground truth before moving to the next question.

### SYNC — "Sync my notes" / "Push my changes"

Run `scripts/sync.sh`. Report what was pulled and pushed. If there's a merge
conflict, stop and show it to the user rather than resolving it silently.

## Ground rules

- Never fabricate an entry's content when browsing, revising, or quizzing —
  only use what's actually written in the file.
- Keep `INDEX.md` generated, not hand-maintained — always regenerate via the
  script after any change under `entries/`.
- One concept per file. If a store request bundles several distinct
  concepts, split them into separate entries.
