#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — writes the two-part micro-confession
to $MAKEFUN_OUTPUT_DIR/entry.txt (default ./out/entry.txt).

The entry is a message once typed to a human and never sent: a To: line naming
who it was meant for, then the unsent line itself, exactly as typed.
"""

import os
from pathlib import Path

ENTRY = (
    "To: Dad\n"
    "I never told you I heard you crying in the garage the night Mom left. "
    "I was eleven, and I still don't know what I was supposed to do with that."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
