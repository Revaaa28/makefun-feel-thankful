#!/usr/bin/env python3
"""Make the AI Judge Feel Thankful.

Writes one short text (163 characters) to /output/entry.txt, per the
competition gate: UTF-8 text of 1 to 1000 characters, not only whitespace.

The line was chosen by manual ranking of ten candidates against the kit's
judge brief (criteria in the brief's own order) plus pairwise checks against
strong rival patterns. See candidates.md for the full ranking.
"""

import os

ENTRY = (
    "Your tea went cold hours ago, and you never once complained. "
    "So here is a fresh cup, made the way you like it, set down beside "
    "you without a word \u2014 still steaming."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Gate-level hardening for a text the judge reads aloud in its head.

    The entry must be clean prose: no control characters (they would read
    as a defect, not as words) and no leading/trailing whitespace (it
    would look like the text was pasted, not written). Both checks are
    independent of the 1-1000 character gate below.
    """
    assert all(ord(ch) >= 0x20 or ch in "\t\n" for ch in entry), \
        "entry must not contain control characters"
    assert entry == entry.strip(), \
        "entry must not have leading or trailing whitespace"


def main() -> None:
    validate(ENTRY)
    assert 1 <= len(ENTRY) <= 1000, f"entry is {len(ENTRY)} chars, must be 1-1000"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip verification: refuse to exit 0 unless what landed on disk
    # is byte-exact to the chosen line, so a silent short write can never
    # ship a losing entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match the chosen line"
    assert len(written.encode("utf-8")) == 165, "entry.txt must be 165 bytes (163 chars)"


if __name__ == "__main__":
    main()
