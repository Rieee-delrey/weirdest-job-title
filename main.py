#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes one job title (26 chars, inside the 1-60 gate) to /output/entry.txt,
then reads it back and validates the gate before exiting.
"""

import hashlib
import os
import sys

LINE = "Chief of Staff to a Roomba"
OUT = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 60


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the file must hold exactly the title, one
    # line, UTF-8, non-blank, inside the 1-60 character gate.
    with open(OUT, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} chars, outside 1-60", file=sys.stderr)
        return 1
    if text.count("\n") != 0:
        print("entry is not a single line", file=sys.stderr)
        return 1
    if text != LINE:
        print("entry does not match the title", file=sys.stderr)
        return 1
    print(f"ok: {len(text)} chars sha256={hashlib.sha256(raw).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
