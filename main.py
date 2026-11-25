#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

Writes the single entry line to /output/entry.txt (no trailing newline),
after validating it: UTF-8, 1-279 chars, single line, no leading/trailing
whitespace. Stdlib only, no network.
"""

import sys
from pathlib import Path

ENTRY = (
    "One star. He waters me once a month, talks to me about his ex, "
    "then acts shocked when I drop a leaf. "
    "I photosynthesize, I don't do therapy."
)


def validate(entry: str) -> None:
    if not entry or entry.strip() != entry:
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not (1 <= len(entry) <= 279):
        raise ValueError(f"entry must be 1-279 chars, got {len(entry)}")
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    validate(ENTRY)
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(ENTRY.encode("utf-8"))
    print(f"wrote {out} ({len(ENTRY)} chars)")
    return 0


def self_test() -> None:
    assert len(ENTRY) == 139, f"expected 139 chars, got {len(ENTRY)}"
    validate(ENTRY)
    for bad in ("", " x", "x ", "a\nb", "x" * 280):
        try:
            validate(bad)
        except ValueError:
            continue
        raise AssertionError(f"validate() accepted invalid entry: {bad!r}")
    print("self-test passed")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        raise SystemExit(main())
