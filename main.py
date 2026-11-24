#!/usr/bin/env python3
"""The Fog Referee: One-Sentence Absurd Invention Pitch.

Writes the entry -- one sentence, at most 220 characters, pitching a
ridiculous invention that fixes a tiny everyday annoyance -- to
/output/entry.txt.

Pure standard library, deterministic: the same bytes on every run.

Why this pitch, against the judge's brief (funny invention, clever fix,
original idea):
1. The annoyance is tiny and universal: glasses fogging up in winter.
2. The fix is absurdly bureaucratic: instead of wiping the lenses, the
   glasses referee your own breath, whistle and yellow card included.
3. The surprise is who gets punished: not the cold, not the glasses --
   your own breath, marched off for a stern talking-to.
4. Nothing in the field does this: no whistle, no yellow card, no
   breath, no steam, no glasses in any of the 359 listed pitches.
5. One sentence, every word earning its place, punch at the very end.
"""

import os

ENTRY = (
    "The Fog Referee: glasses that blow a tiny whistle and flash a "
    "yellow card at your own breath every time it fogs the lenses, "
    "then march the steam off for a stern talking-to."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 220):
        raise ValueError("entry must be 1 to 220 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text:
        raise ValueError("entry must fit on one line")
    terminators = sum(text.count(mark) for mark in (".", "!", "?"))
    if terminators != 1:
        raise ValueError("entry must be exactly one sentence, got %d terminators" % terminators)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
