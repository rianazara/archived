#!/usr/bin/env python3
"""Shared helpers for the ingestion queue under inbox/."""

import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "inbox"
DROP = INBOX / "drop"
QUEUE = INBOX / "queue"
EXTRACT = INBOX / "extract"
PROCESSED = INBOX / "processed"

# Statuses a stub moves through. "pending" items still need their text pulled;
# "extracted" ones are ready for Claude to draft an entry from.
STATUSES = ("pending", "extracted", "needs_dictation", "done", "failed")

# Types Claude resolves with WebFetch during a run, not with extract.py.
FETCH_TYPES = ("url", "instagram")

TYPE_BY_SUFFIX = {
    ".eml": "eml",
    ".mbox": "mbox",
    ".pdf": "pdf",
    ".docx": "docx",
    ".html": "html",
    ".htm": "html",
    ".md": "text",
    ".txt": "text",
    ".zip": "archive",
}


def ensure_dirs() -> None:
    for path in (DROP, QUEUE, EXTRACT, PROCESSED):
        path.mkdir(parents=True, exist_ok=True)


def new_id() -> str:
    return f"{datetime.now().strftime('%Y-%m-%d')}-{secrets.token_hex(2)}"


def now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def rel(path: Path) -> str:
    """Repo-relative string for paths inside the repo, absolute otherwise."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def write_stub(item_type: str, source: str, title: str = "", note: str = "",
               status: str = "pending", item_id: str = "") -> dict:
    ensure_dirs()
    item = {
        "id": item_id or new_id(),
        "type": item_type,
        "source": source,
        "captured_at": now(),
        "status": status,
        "title": title,
        "note": note,
    }
    (QUEUE / f"{item['id']}.json").write_text(json.dumps(item, indent=2) + "\n")
    return item


def read_stubs(status: str = "") -> list[dict]:
    if not QUEUE.exists():
        return []
    items = []
    for path in sorted(QUEUE.glob("*.json")):
        try:
            item = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        if not status or item.get("status") == status:
            items.append(item)
    return items


def update_stub(item_id: str, **fields) -> dict:
    path = QUEUE / f"{item_id}.json"
    item = json.loads(path.read_text())
    item.update(fields)
    path.write_text(json.dumps(item, indent=2) + "\n")
    return item


def queued_sources() -> set[str]:
    """Sources already in the queue, so scans don't double-add a file."""
    return {item.get("source", "") for item in read_stubs()}


def extract_path(item_id: str) -> Path:
    ensure_dirs()
    return EXTRACT / f"{item_id}.txt"
