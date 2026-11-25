"""Weirdest Job Title entry.

Writes a single job title -- the weirdest one we could think of, in
60 characters or fewer and nothing else -- to /output/entry.txt.

The title is a module-level constant so the program's output is fully
determined by this file alone. Standard library only.
"""

import os

# The entry: one job title, 60 characters or fewer, nothing else.
TITLE = "Chief Negotiator for Haunted Vending Machines"

# Kit cap, confirmed from the competition kit's RULES.txt / gate:
# /output/entry.txt must be UTF-8 text of 1 to 60 characters.
MAX_CHARS = 60

# Word count of the chosen title, kept as a constant for the guard below.
WORD_COUNT = 6


def check_title(title):
    """Verify the title obeys the kit's gate before anything is written.

    Returns a list of problems (empty when the title is valid).
    """
    problems = []
    if not title:
        problems.append("title is empty")
    if title != title.strip():
        problems.append("title has leading or trailing whitespace")
    if "\n" in title or "\r" in title:
        problems.append("title must be a single line")
    if len(title) > MAX_CHARS:
        problems.append(
            "title is %d chars, over the %d-char cap" % (len(title), MAX_CHARS)
        )
    if len(title.split()) != WORD_COUNT:
        problems.append(
            "word count is %d, expected %d" % (len(title.split()), WORD_COUNT)
        )
    return problems


def verify_written(out_path):
    """Read the file back and confirm it is byte-identical to TITLE."""
    with open(out_path, "rb") as f:
        raw = f.read()
    expected = TITLE.encode("utf-8")
    if raw != expected:
        raise ValueError(
            "read-back mismatch: file is %d bytes, expected %d bytes"
            % (len(raw), len(expected))
        )
    text = raw.decode("utf-8")
    if len(text) != len(TITLE) or text.count("\n") != 0:
        raise ValueError("read-back text does not match TITLE exactly")
    return len(raw)


def main():
    """Write TITLE to /output/entry.txt, creating the directory if needed."""
    problems = check_title(TITLE)
    if problems:
        raise ValueError("invalid title: " + "; ".join(problems))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TITLE)
    n_bytes = verify_written(out_path)
    print("wrote %d bytes to %s: %r" % (n_bytes, out_path, TITLE))


if __name__ == "__main__":
    main()
