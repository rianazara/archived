#!/usr/bin/env python3
"""Queue any new files sitting in inbox/drop/. Offline, stdlib only."""

import _queue


def main() -> None:
    _queue.ensure_dirs()
    known = _queue.queued_sources()
    added = 0

    for path in sorted(_queue.DROP.rglob("*")):
        if not path.is_file() or path.name.startswith("."):
            continue
        source = _queue.rel(path)
        if source in known:
            continue
        item_type = _queue.TYPE_BY_SUFFIX.get(path.suffix.lower(), "text")
        item = _queue.write_stub(item_type, source, title=path.name)
        print(f"Queued {item['id']} ({item_type}): {source}")
        added += 1

    pending = len(_queue.read_stubs("pending"))
    print(f"Added {added} item(s). {pending} pending in the queue.")


if __name__ == "__main__":
    main()
