#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entry program.

Writes exactly one emoji to /output/entry.txt: Mount Fuji.

Why this emoji, against the judge's brief (most important first):
1. Exactly one emoji, and it lands on a dream vacation — the brief names
   "a mountain" outright among dream vacations, and Fuji is the mountain
   every traveller pictures.
2. A postcard at a glance — snow-capped Fuji against the sky is one of the
   most photographed views on earth; a stranger sees the trip before
   reading a word.
3. Personal and specific — not "any holiday", but one particular dream:
   Japan, a dawn climb, Fuji itself.
4. A spark of surprise — while the field sends beaches and sunsets, a
   mountain is the fresh pick.
5. Reads instantly at any size, in any culture — a single iconic peak.

Deterministic: the same single code point is written on every run.
Standard library only. No network, no input files, no dependence on the
working directory — the output path is absolute.
"""

import os

EMOJI = "\U0001F5FB"  # MOUNT FUJI — one code point, four UTF-8 bytes.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check against the competition's gate: UTF-8 text of 1 to 8
    # characters, not only white space. Fail loudly rather than submit
    # an invalid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 8, "entry must be 1 to 8 characters"
    assert text.strip(), "entry must not be only white space"


if __name__ == "__main__":
    main()
