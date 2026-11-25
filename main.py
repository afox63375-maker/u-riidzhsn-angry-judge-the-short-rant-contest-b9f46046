#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry writer.

Writes one short rant about a small everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Standard library only. Fully deterministic.
"""

import os
import sys

MAX_CHARS = 400

RANT = (
    "My printer has one job. ONE. It sleeps all week doing absolutely "
    "nothing, then the second I need a boarding pass it flashes 'low ink', "
    "jams on page one, and prints a test page in a language I have never "
    "seen. I do not own a printer. I own a small grey hostage negotiator "
    "that charges rent in ink."
)


def validate(rant: str) -> None:
    if not rant or not rant.strip():
        raise ValueError("rant must not be blank")
    if len(rant) > MAX_CHARS:
        raise ValueError(
            f"rant is {len(rant)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(RANT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(RANT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
