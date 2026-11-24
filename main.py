"""Status Report Comedy Sprint -- one line, at most 200 characters.

The line: a weekly status report that reports heroic productivity in the
wrong direction -- zero tasks done, fourteen started, inbox zero achieved
by declaring email a legacy system. The blocker is the reporter's own
enthusiasm, which is the joke.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "Weekly status: completed 0 tasks, started 14, renamed the project "
    "twice, and achieved inbox zero by declaring email a legacy system. "
    "Morale: suspiciously high. Blockers: my own enthusiasm."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
