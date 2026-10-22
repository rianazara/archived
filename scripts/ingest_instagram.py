#!/usr/bin/env python3
"""Normalize an Instagram "Download Your Information" saved-items export.

Captions ship inline in this export, so nothing needs scraping. This builds a
local catalog keyed by your own saved collections — the categories you already
curated — and leaves verbatim captions in inbox/ only: they're other people's
words, and this repo gets pushed.

Usage:
    python3 scripts/ingest_instagram.py inbox/instagram/your_instagram_activity
    python3 scripts/ingest_instagram.py inbox/instagram/export.zip
"""

import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import _queue

OUT = _queue.INBOX / "instagram"
CATALOG = OUT / "catalog"
UNCOLLECTED = "uncollected"


def demojibake(text: str) -> str:
    """Undo the Latin-1/UTF-8 double encoding Instagram applies to captions."""
    if not text:
        return ""
    try:
        return text.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", demojibake(name).lower()).strip("-")
    return slug or "untitled"


def labels(entry: dict) -> dict:
    out = {}
    for pair in entry.get("label_values", []):
        if "label" in pair and "value" in pair:
            out[pair["label"]] = pair["value"]
    return out


def find_posts(node, found: list) -> None:
    """Collect every {URL, Caption} pair anywhere in the structure.

    Collections nest their posts in anonymous {"dict": [...]} wrappers, and the
    shape has changed across export versions, so walk rather than index.
    """
    if isinstance(node, dict):
        if node.get("label") == "URL" and node.get("value"):
            found.append(node)
        for value in node.values():
            find_posts(value, found)
    elif isinstance(node, list):
        for value in node:
            find_posts(value, found)


def posts_in(entry: dict) -> list[dict]:
    """(url, caption) pairs for one collection or saved-post entry."""
    blocks: list[dict] = []
    find_posts(entry, blocks)
    out = []
    for block in blocks:
        parent = block.get("_parent_labels", {})
        out.append({"url": block["value"], "caption": parent.get("Caption", "")})
    return out


def parse_pairs(entry: dict) -> list[dict]:
    """Walk a subtree pairing each URL with the Caption in the same dict list."""
    results = []

    def walk(node):
        if isinstance(node, list):
            url = caption = None
            for item in node:
                if isinstance(item, dict):
                    if item.get("label") == "URL":
                        url = item.get("value")
                    elif item.get("label") == "Caption":
                        caption = item.get("value")
            if url:
                results.append({"url": url, "caption": demojibake(caption or "")})
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            for value in node.values():
                walk(value)

    walk(entry)
    return results


def load(export: Path) -> tuple[list, list]:
    """Read saved_posts.json and saved_collections.json from a dir or zip."""
    if export.is_dir():
        def read(name):
            hits = sorted(export.rglob(name))
            return json.loads(hits[0].read_text()) if hits else []
        return read("saved_posts.json"), read("saved_collections.json")

    with zipfile.ZipFile(export) as archive:
        def read(name):
            hits = [n for n in archive.namelist() if n.endswith(name)]
            if not hits:
                return []
            with archive.open(hits[0]) as handle:
                return json.loads(handle.read().decode("utf-8", errors="replace"))
        return read("saved_posts.json"), read("saved_collections.json")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    export = Path(sys.argv[1]).expanduser()
    if not export.exists():
        sys.exit(f"No such export: {export}")

    posts_raw, collections_raw = load(export)
    if not posts_raw and not collections_raw:
        sys.exit("Found neither saved_posts.json nor saved_collections.json.")

    # url -> record. Saved posts give the baseline; collections add membership.
    records: dict[str, dict] = {}
    for entry in posts_raw:
        fields = labels(entry)
        url = fields.get("URL")
        if not url:
            continue
        records[url] = {
            "url": url,
            "caption": demojibake(fields.get("Caption", "")),
            "saved_at": entry.get("timestamp"),
            "collections": [],
        }

    collections: dict[str, dict] = {}
    for entry in collections_raw:
        fields = labels(entry)
        name = demojibake(fields.get("Name", "")).strip()
        if not name:
            continue
        key = name.casefold()
        meta = collections.setdefault(key, {"name": name, "urls": [], "aliases": set()})
        meta["aliases"].add(name)
        for pair in parse_pairs(entry):
            url = pair["url"]
            record = records.setdefault(url, {
                "url": url, "caption": pair["caption"],
                "saved_at": None, "collections": [],
            })
            if not record["caption"]:
                record["caption"] = pair["caption"]
            if meta["name"] not in record["collections"]:
                record["collections"].append(meta["name"])
            if url not in meta["urls"]:
                meta["urls"].append(url)

    CATALOG.mkdir(parents=True, exist_ok=True)
    index = {
        "generated_at": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "source": str(export),
        "collections": {m["name"]: m["urls"] for m in collections.values()},
        "posts": records,
    }
    (OUT / "index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False))

    for meta in collections.values():
        write_catalog(meta["name"], [records[u] for u in meta["urls"] if u in records])

    loose = [r for r in records.values() if not r["collections"]]
    write_catalog(UNCOLLECTED, loose)

    write_review_list(collections, records)

    print(f"posts: {len(records)}  collections: {len(collections)}  "
          f"uncollected: {len(loose)}")
    print(f"index:   {_queue.rel(OUT / 'index.json')}")
    print(f"catalog: {_queue.rel(CATALOG)}/  ({len(collections) + 1} files)")
    print(f"review:  {_queue.rel(OUT / 'needs-review.md')}")

    merged = [sorted(m["aliases"]) for m in collections.values() if len(m["aliases"]) > 1]
    for aliases in merged:
        print(f"merged duplicate collection names: {aliases}")


BAIT = re.compile(
    r"comment\s+[\"“']?\w+|i'?ll\s+dm|dm\s+you|link\s+in\s+bio|swipe|carousel",
    re.I,
)


def substantive(caption: str) -> bool:
    """True when the caption itself carries the content, hashtags excluded."""
    return len(re.sub(r"#\w+", "", caption).strip()) >= 400


def write_review_list(collections: dict, records: dict) -> None:
    """Items whose substance isn't in the text: carousels, reels, comment-gated DMs.

    Instagram exports carry captions only, so for these the knowledge is still
    on Instagram. Listed per collection so they can be reopened deliberately.
    """
    lines = [
        "# Needs review",
        "",
        "Saved items whose content isn't recoverable from the export: no caption,",
        "or the caption only teases a carousel/reel/DM. Open these on Instagram if",
        "they still matter. Regenerated by scripts/ingest_instagram.py.",
        "",
    ]
    for meta in sorted(collections.values(), key=lambda m: m["name"].casefold()):
        items = [records[u] for u in meta["urls"] if u in records]
        stuck = [i for i in items
                 if not substantive(i["caption"]) or BAIT.search(i["caption"] or "")]
        if not stuck:
            continue
        lines.append(f"## {meta['name']} — {len(stuck)} of {len(items)}")
        lines.append("")
        for item in stuck:
            caption = " ".join(item["caption"].split())
            why = "no caption" if not caption else (
                "teaser only" if BAIT.search(caption) else "too short")
            lines.append(f"- {item['url']} — _{why}_"
                         + (f"  \n  {caption[:110]}…" if caption else ""))
        lines.append("")
    (OUT / "needs-review.md").write_text("\n".join(lines))


def write_catalog(name: str, items: list[dict]) -> None:
    """Local reference file: verbatim captions stay out of entries/ and out of git."""
    lines = [
        f"# {name}",
        "",
        f"{len(items)} saved item(s). Local reference only — verbatim captions,",
        "not for committing. Generated by scripts/ingest_instagram.py.",
        "",
    ]
    for item in sorted(items, key=lambda r: r.get("saved_at") or 0, reverse=True):
        saved = item.get("saved_at")
        when = (datetime.fromtimestamp(saved).strftime("%Y-%m-%d") if saved else "unknown")
        lines.append(f"## {when} — {item['url']}")
        also = [c for c in item["collections"] if c != name]
        if also:
            lines.append(f"_also in: {', '.join(also)}_")
        lines.append("")
        lines.append(item["caption"].strip() or "_(no caption)_")
        lines.append("")
    (CATALOG / f"{slugify(name)}.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
