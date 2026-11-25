#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun bounty entry.

A houseplant's one-star review, written in sap. The entry is a single
139-character line, written byte-for-byte to output/entry.txt with no
trailing newline.

Validation (stdlib only, no network): the entry must be valid UTF-8,
1-279 chars, a single line, and free of leading/trailing whitespace.
Run `python3 main.py --self-test` to exercise the validators and the
output round-trip.
"""

import sys
from pathlib import Path

ENTRY = (
    "One star. He waters me once a month, talks to me about his ex, "
    "then acts shocked when I drop a leaf. "
    "I photosynthesize, I don't do therapy."
)


def validate_utf8(entry: str) -> None:
    entry.encode("utf-8")  # raises if not valid UTF-8-encodable


def validate_length(entry: str) -> None:
    if not (1 <= len(entry) <= 279):
        raise ValueError(f"entry must be 1-279 chars, got {len(entry)}")


def validate_single_line(entry: str) -> None:
    if not entry or entry.strip() != entry:
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def validate(entry: str) -> None:
    """Run every validation step; raises ValueError on the first failure."""
    validate_utf8(entry)
    validate_length(entry)
    validate_single_line(entry)


def main() -> int:
    validate(ENTRY)
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(ENTRY.encode("utf-8"))
    print(f"wrote {out} ({len(ENTRY)} chars)")
    return 0


def self_test() -> None:
    """Exercise the validators and the output round-trip."""
    from pathlib import Path as _Path

    # Entry shape: exact length, single line, no trailing newline.
    assert len(ENTRY) == 139, f"expected 139 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    validate(ENTRY)

    # Each validator rejects what it is responsible for.
    for bad, fn in (
        ("", validate_length),
        ("x" * 280, validate_length),
        (" x", validate_single_line),
        ("x ", validate_single_line),
        ("a\nb", validate_single_line),
        ("a\rb", validate_single_line),
    ):
        try:
            fn(bad)
        except ValueError:
            continue
        raise AssertionError(f"{fn.__name__}() accepted invalid entry: {bad!r}")

    # Deterministic re-run: writing twice yields identical bytes.
    out = _Path(__file__).resolve().parent / "output" / "entry.txt"
    main()
    first = out.read_bytes()
    assert first == ENTRY.encode("utf-8"), "output bytes differ from ENTRY"
    assert not first.endswith(b"\n"), "output must have no trailing newline"
    main()
    second = out.read_bytes()
    assert first == second, "re-run produced different output bytes"
    print("self-test passed")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        raise SystemExit(main())
