"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review, in the dog's voice, to /output/entry.txt.
Deterministic: no network, no randomness, no input — the same line every run.
"""

import os

ENTRY = (
    "He walks up to MY door every day, shoves paper through MY slot, "
    "then RUNS. One star for the trespass, five for the chase. "
    "Same time tomorrow, coward."
)

def main() -> None:
    """Write the review to /output/entry.txt (UTF-8, single line)."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
