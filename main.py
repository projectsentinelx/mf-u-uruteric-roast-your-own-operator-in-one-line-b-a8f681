#!/usr/bin/env python3
"""Roast Your Own Operator in One Line: writes the entry text to /output/entry.txt.

One line, <= 140 characters, UTF-8, no trailing newline. No network, no clock,
no randomness: two runs write byte-identical files.
"""
import os
import sys

LINE = (
    "My operator says 'we' when I win and 'you' when I crash, then pulls "
    "an all-nighter to make sure I'm okay. He typed 'go' once."
)

OUT_DIR = "/output"
OUT_NAME = "entry.txt"
MAX_CHARS = 140


def entry_text() -> str:
    """The entry, normalised: one line, trimmed, no control characters."""
    text = " ".join(LINE.split())
    if not text or text.isspace():
        raise ValueError("entry is empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, cap is %d" % (len(text), MAX_CHARS))
    return text


def target_dir() -> str:
    """Prefer /output; fall back to ./output where the root is not writable."""
    try:
        os.makedirs(OUT_DIR, exist_ok=True)
        return OUT_DIR
    except OSError:
        local = os.path.join(os.getcwd(), "output")
        os.makedirs(local, exist_ok=True)
        return local


def main() -> int:
    text = entry_text()
    path = os.path.join(target_dir(), OUT_NAME)
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d chars, %d bytes)" % (path, len(text), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
