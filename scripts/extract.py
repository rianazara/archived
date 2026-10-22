#!/usr/bin/env python3
"""Pull plain text out of queued local files and YouTube subtitles.

Re-execs itself under .venv/bin/python3 when that exists, so PDF, Word and
YouTube support works whether or not you remember to activate the venv.

Usage:
    python3 scripts/extract.py            # every pending item it can handle
    python3 scripts/extract.py 2026-10-21-a3f9
"""

import email
import email.policy
import json
import mailbox
import os
import re
import subprocess
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

import _queue

VENV_PYTHON = _queue.ROOT / ".venv" / "bin" / "python3"
VENV_YTDLP = _queue.ROOT / ".venv" / "bin" / "yt-dlp"

MISSING_VENV = (
    "needs the venv — run: python3 -m venv .venv && "
    ".venv/bin/python3 -m pip install -U pip yt-dlp pypdf python-docx html2text"
)


class ExtractError(Exception):
    """Raised when an item cannot be turned into text."""


class MissingVenv(ExtractError):
    """The venv isn't built yet. An environment gap, so the item stays pending."""


def reexec_in_venv() -> None:
    """Switch to the venv interpreter once, if one is built and we're outside it."""
    if not VENV_PYTHON.exists():
        return
    if Path(sys.prefix).resolve() == (_queue.ROOT / ".venv").resolve():
        return
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


class _HTMLText(HTMLParser):
    """Stdlib fallback for flattening HTML when html2text isn't installed."""

    SKIP = {"script", "style", "head", "title", "meta", "link"}
    BREAK = {"p", "br", "div", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skipping = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skipping += 1
        elif tag in self.BREAK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skipping:
            self._skipping -= 1
        elif tag in self.BREAK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self._skipping and data.strip():
            self.parts.append(data.strip() + " ")

    def text(self) -> str:
        return collapse_blank_lines("".join(self.parts))


def collapse_blank_lines(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return "\n".join(line.strip() for line in text.splitlines()).strip()


def html_to_text(html: str) -> str:
    try:
        import html2text
    except ImportError:
        parser = _HTMLText()
        parser.feed(html)
        return parser.text()
    converter = html2text.HTML2Text()
    converter.ignore_images = True
    converter.ignore_emphasis = True
    converter.body_width = 0
    return collapse_blank_lines(converter.handle(html))


def message_to_text(message) -> tuple[str, str]:
    """(subject, body) for one parsed email message."""
    subject = str(message.get("Subject", "")).strip()
    sender = str(message.get("From", "")).strip()
    date = str(message.get("Date", "")).strip()

    # Newsletters routinely ship a stub text/plain part ("view in browser") next
    # to the real HTML, so take whichever alternative actually carries content.
    candidates = []
    parts = list(message.walk()) if message.is_multipart() else [message]
    for part in parts:
        if part.get_content_type() not in ("text/plain", "text/html"):
            continue
        raw = part.get_payload(decode=True) or b""
        decoded = raw.decode(part.get_content_charset() or "utf-8", errors="replace")
        text = decoded if part.get_content_type() == "text/plain" else html_to_text(decoded)
        candidates.append(collapse_blank_lines(text))

    body = max(candidates, key=lambda text: len(text.split()), default="")

    header = "\n".join(filter(None, [
        f"Subject: {subject}" if subject else "",
        f"From: {sender}" if sender else "",
        f"Date: {date}" if date else "",
    ]))
    return subject, f"{header}\n\n{body}".strip()


def from_eml(path: Path) -> tuple[str, str]:
    with path.open("rb") as handle:
        message = email.message_from_binary_file(handle, policy=email.policy.default)
    return message_to_text(message)


def from_text(path: Path) -> tuple[str, str]:
    return "", path.read_text(errors="replace").strip()


def from_html(path: Path) -> tuple[str, str]:
    return "", html_to_text(path.read_text(errors="replace"))


def from_pdf(path: Path) -> tuple[str, str]:
    try:
        from pypdf import PdfReader
    except ImportError:
        raise MissingVenv(MISSING_VENV)
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = collapse_blank_lines("\n\n".join(pages))
    if not text:
        raise ExtractError("no extractable text — likely a scanned PDF, needs OCR")
    title = (reader.metadata or {}).get("/Title", "") or ""
    return str(title).strip(), text


def from_docx(path: Path) -> tuple[str, str]:
    try:
        import docx
    except ImportError:
        raise MissingVenv(MISSING_VENV)
    document = docx.Document(str(path))
    body = "\n".join(p.text for p in document.paragraphs)
    return "", collapse_blank_lines(body)


def strip_vtt(vtt: str) -> str:
    """Turn a WebVTT subtitle file into readable prose."""
    lines = []
    for line in vtt.splitlines():
        line = line.strip()
        if not line or "-->" in line or line.startswith(("WEBVTT", "NOTE", "Kind:", "Language:")):
            continue
        if line.isdigit():
            continue
        line = re.sub(r"<[^>]+>", "", line)
        if line and (not lines or lines[-1] != line):
            lines.append(line)
    return collapse_blank_lines(" ".join(lines))


def from_youtube(url: str, item_id: str) -> tuple[str, str]:
    if not VENV_YTDLP.exists():
        raise MissingVenv(MISSING_VENV)
    workdir = _queue.EXTRACT / f"{item_id}-subs"
    workdir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [str(VENV_YTDLP), "--write-auto-subs", "--write-subs",
         "--sub-langs", "en.*,en", "--sub-format", "vtt",
         "--skip-download", "--no-playlist",
         "-o", "%(title)s.%(ext)s", url],
        cwd=str(workdir), capture_output=True, text=True, timeout=180,
    )
    subtitles = sorted(workdir.glob("*.vtt"))
    if not subtitles:
        output = f"{result.stdout}\n{result.stderr}"
        if "PO token" in output:
            raise ExtractError(
                "YouTube withheld the captions (PO token required) — they exist "
                "but need an authenticated request; dictate the takeaway instead"
            )
        raise ExtractError("no captions available — dictate the takeaway instead")
    title = subtitles[0].name.split(".")[0]
    return title, strip_vtt(subtitles[0].read_text(errors="replace"))


def read_archive_member(path: Path, target: Path, wanted: str) -> str:
    """Read one named member out of an untrusted archive.

    Only the member asked for is written to disk: an Instagram export also
    contains messages and profile data, which has no business being unpacked
    just to read a list of saved links.
    """
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path) as archive:
        members = [n for n in archive.namelist() if n.endswith(wanted)]
        if not members:
            names = sorted({Path(n).name for n in archive.namelist()})
            raise ExtractError(
                f"no {wanted} in this archive — not an Instagram export? "
                f"found: {', '.join(names[:6]) or 'nothing'}"
            )
        member = members[0]
        destination = (target / Path(member).name).resolve()
        if not str(destination).startswith(str(target.resolve())):
            raise ExtractError(f"archive tries to escape its directory: {member}")
        with archive.open(member) as source:
            data = source.read()
    destination.write_bytes(data)
    return data.decode("utf-8", errors="replace")


def from_archive(path: Path, item_id: str) -> tuple[str, str]:
    """Instagram 'Download Your Information' export: fan out saved_posts.json."""
    target = _queue.EXTRACT / f"{item_id}-archive"
    raw = read_archive_member(path, target, "saved_posts.json")
    urls = extract_saved_urls(json.loads(raw))
    known = _queue.queued_sources()
    added = 0
    for url, title in urls:
        if url in known:
            continue
        _queue.write_stub("instagram", url, title=title,
                          note=f"from Instagram export {path.name}")
        added += 1
    return "", f"Instagram export: queued {added} saved item(s) of {len(urls)} found."


def extract_saved_urls(data) -> list[tuple[str, str]]:
    """Pull (url, title) pairs out of Instagram's saved_posts.json.

    Instagram has shipped several shapes for this file, so walk the whole
    structure and collect anything that looks like a saved permalink.
    """
    found: list[tuple[str, str]] = []
    seen = set()

    def walk(node, title=""):
        if isinstance(node, dict):
            label = node.get("title") or node.get("value") or title
            href = node.get("href") or node.get("uri") or node.get("url")
            if isinstance(href, str) and "instagram.com" in href and href not in seen:
                seen.add(href)
                found.append((href, label if isinstance(label, str) else ""))
            for value in node.values():
                walk(value, label if isinstance(label, str) else title)
        elif isinstance(node, list):
            for value in node:
                walk(value, title)

    walk(data)
    return found


def extract_item(item: dict) -> tuple[str, str]:
    item_type = item["type"]
    source = item["source"]

    if item_type == "youtube":
        return from_youtube(source, item["id"])

    path = Path(source)
    if not path.is_absolute():
        path = _queue.ROOT / path
    if not path.is_file():
        raise ExtractError(f"file is gone: {source}")

    if item_type == "eml":
        return from_eml(path)
    if item_type == "mbox":
        return from_mbox(path, item["id"])
    if item_type == "pdf":
        return from_pdf(path)
    if item_type == "docx":
        return from_docx(path)
    if item_type == "html":
        return from_html(path)
    if item_type == "archive":
        return from_archive(path, item["id"])
    if item_type == "text":
        return from_text(path)
    raise ExtractError(f"no extractor for type '{item_type}'")


def from_mbox(path: Path, item_id: str) -> tuple[str, str]:
    """Bulk mail export: one queued item per message."""
    known = _queue.queued_sources()
    added = 0
    for index, message in enumerate(mailbox.mbox(str(path))):
        source = f"{_queue.rel(path)}#{index}"
        if source in known:
            continue
        subject, body = message_to_text(message)
        child_id = _queue.new_id()
        _queue.extract_path(child_id).write_text(body + "\n")
        _queue.write_stub("eml", source, title=subject, status="extracted",
                          item_id=child_id, note=f"message {index} of {path.name}")
        added += 1
    return "", f"mbox: queued {added} message(s)."


def main() -> None:
    reexec_in_venv()
    _queue.ensure_dirs()

    wanted = sys.argv[1:]
    items = [i for i in _queue.read_stubs("pending") if not wanted or i["id"] in wanted]
    if not items:
        print("Nothing pending to extract.")
        return

    for item in items:
        if item["type"] in _queue.FETCH_TYPES:
            print(f"- {item['id']} ({item['type']}): left for Claude to fetch")
            continue
        try:
            title, text = extract_item(item)
        except MissingVenv as error:
            # Stays pending so it's picked up automatically once the venv exists.
            _queue.update_stub(item["id"], note=str(error))
            print(f"~ {item['id']} ({item['type']}): {error}")
            continue
        except Exception as error:
            # Inputs are untrusted and third-party parsers raise whatever they
            # like, so one bad file must never abort the rest of the batch.
            status = "needs_dictation" if "dictate" in str(error) else "failed"
            detail = f"{type(error).__name__}: {error}".strip()
            _queue.update_stub(item["id"], status=status, note=detail)
            print(f"! {item['id']} ({item['type']}): {detail}")
            continue

        if item["type"] in ("mbox", "archive"):
            _queue.update_stub(item["id"], status="done", note=text)
            print(f"+ {item['id']} ({item['type']}): {text}")
            continue

        _queue.extract_path(item["id"]).write_text(text + "\n")
        fields = {"status": "extracted"}
        if title and not item.get("title"):
            fields["title"] = title
        _queue.update_stub(item["id"], **fields)
        words = len(text.split())
        print(f"+ {item['id']} ({item['type']}): {words} words -> "
              f"{_queue.rel(_queue.extract_path(item['id']))}")


if __name__ == "__main__":
    main()
