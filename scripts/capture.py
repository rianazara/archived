#!/usr/bin/env python3
"""Queue a URL or file for ingestion. Instant, offline, stdlib only.

Usage:
    python3 scripts/capture.py https://example.com/article
    python3 scripts/capture.py https://youtu.be/VIDEOID --note "watch for the pricing bit"
    python3 scripts/capture.py ~/Downloads/paper.pdf
"""

import argparse
import sys
from pathlib import Path
from urllib.parse import urlparse

import _queue

YOUTUBE_HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "youtu.be"}
INSTAGRAM_HOSTS = {"instagram.com", "www.instagram.com"}


def classify_url(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    if host in YOUTUBE_HOSTS:
        return "youtube"
    if host in INSTAGRAM_HOSTS:
        return "instagram"
    return "url"


def classify_file(path: Path) -> str:
    return _queue.TYPE_BY_SUFFIX.get(path.suffix.lower(), "text")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="URL, or path to a local file")
    parser.add_argument("--type", dest="item_type", default="",
                        help="override the detected type")
    parser.add_argument("--note", default="",
                        help="why this is worth keeping (shown in the daily brief)")
    args = parser.parse_args()

    target = args.target
    if target.startswith(("http://", "https://")):
        item_type = args.item_type or classify_url(target)
        source = target
    else:
        path = Path(target).expanduser()
        if not path.is_file():
            sys.exit(f"Not a URL and not a file: {target}")
        item_type = args.item_type or classify_file(path)
        source = _queue.rel(path)

    item = _queue.write_stub(item_type, source, note=args.note)
    print(f"Queued {item['id']} ({item_type}): {source}")


if __name__ == "__main__":
    main()
