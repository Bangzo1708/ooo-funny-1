#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes a single line of out-of-office auto-reply text to /output/entry.txt.
Deterministic: no network, no randomness, no external files.
"""

import os

ENTRY = (
    "I'm out of the office and my laptop is at home, where it belongs. "
    "Your email will be ignored in the order received."
)


def main() -> None:
    text = ENTRY.strip()

    # Gate checks, mirroring the competition gate:
    # 1-140 characters, not only whitespace, exactly one line.
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 140:
        raise SystemExit("entry is longer than 140 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
