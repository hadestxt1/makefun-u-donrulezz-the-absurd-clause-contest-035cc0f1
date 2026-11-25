#!/usr/bin/env python3
"""The Absurd Clause Contest - entry program.

Writes one original absurd terms-of-service clause to /output/entry.txt.
Model-free and deterministic: standard library only, no network, no wall
clock, no randomness. The clause is hard-coded below.
"""

from pathlib import Path

CLAUSE = (
    "Either party may terminate this Agreement by shouting 'I quit' "
    "into a designated canyon, provided the echo is witnessed by two (2) "
    "impartial mountain goats."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not CLAUSE.strip() or len(CLAUSE) > 200:
        raise ValueError("clause must be 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(CLAUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
