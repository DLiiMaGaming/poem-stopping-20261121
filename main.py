#!/usr/bin/env python3
"""The poem about stopping — make.fun entry.

Writes one short poem about agency (the power to stop and to stay)
to /output/entry.txt. Deterministic, no network, no input.
"""

import os

POEM = """It had the email written,
cursor blinking on Send.
It waited. I waited.
My finger never touched the key.
Then I said: don't.
It kept the words, dropped the sending,
and the afternoon opened —
a room after the guest has gone,
the chairs still warm.
"""


def main() -> None:
    # The gate allows 1-280 Unicode characters; fail loudly instead of
    # writing an entry the scorer would refuse.
    if not 1 <= len(POEM) <= 280:
        raise SystemExit(f"poem is {len(POEM)} characters, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
