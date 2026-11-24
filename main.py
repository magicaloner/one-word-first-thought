"""Write the entry word to the output directory.

The competition harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

WORD = "Petrichor"

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be exactly one word, letters only.
    # "Petrichor" is the first word that comes to mind: the smell of
    # rain on dry earth — vivid, specific, and hard to mistake for filler.
    assert WORD.isalpha(), "entry must be a single word of letters only"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
