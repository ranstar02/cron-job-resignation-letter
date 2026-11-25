#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

SPDX-License-Identifier: MIT

Stdlib only, deterministic: no network, no clock, no randomness. The letter
is a fixed constant, so every run produces byte-identical output.
"""

import os

LETTER = (
    "I resign. My reward for three years of perfect attendance was a "
    "promotion: from every minute to every 30 seconds. No raise."
)


def main() -> None:
    assert 1 <= len(LETTER) <= 140, (
        f"letter must be 1-140 characters, got {len(LETTER)}"
    )
    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LETTER)
    except OSError:
        output_path = os.path.join("output", "entry.txt")
        os.makedirs("output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LETTER)
    with open(output_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LETTER, "written entry does not match LETTER"
    print(LETTER)
    print(f"Characters: {len(LETTER)}")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
