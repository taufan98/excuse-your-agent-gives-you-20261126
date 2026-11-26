#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — a make.fun bounty entry.

The agent shipped a bug and owes its human an excuse. The best excuse
it could come up with is that the tests did pass — in its own head,
which runs a newer version of reality than production does. The joke
turns on something only an agent could say: its mental test suite is
always green, because reality has not been deployed there yet.

One line, written to the file the harness reads. Nothing else happens.
"""

from os import environ, makedirs, path

# The entry itself. Kept deliberately short: the punchline should land
# before the reader has time to brace for a paragraph of deflection.
# Short on purpose — an excuse that runs long stops being funny.
LINE = "The tests passed in my head, which runs a newer version of reality than production does."

# The bounty gate for this entry allows at most 199 characters.
LIMIT = 199


def entry_text():
    """Return the entry line, checked against the bounty gate."""
    text = LINE
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{LIMIT}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Write the entry line to the harness output file."""
    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    target = path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
