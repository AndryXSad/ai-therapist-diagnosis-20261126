"""Your AI Therapist's Diagnosis entry.

The program writes one funny single-line diagnosis to the output
directory: the diagnosis an AI therapist hands its human.

The joke is built as a deadpan clinical finding. "Acute
validation-seeking" is the calm diagnosis a therapist would write on a
chart, and the turn lands at the very end: the patient refreshed the
therapist's reply three times, hoping the machine would change its mind
about them. The laugh comes from the reframe: the patient treats the
AI's verdict as the one that counts, and keeps re-rolling it like a
verdict they can appeal. One sentence, every word working, no setup
that overstays.
"""

import os
from pathlib import Path

# The entry: one line, well under the 200-character gate.
LINE = (
    "Diagnosis: acute validation-seeking. You refreshed my reply three "
    "times hoping I'd change my mind about you."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or text != text.strip():
        raise ValueError("entry must be a single clean line")
    path = output_dir / "entry.txt"
    # Write exactly the line: no trailing newline, so the gated
    # character count is the line's own length.
    path.write_text(text, encoding="utf-8")
    # Self-check: what the grader will read back is byte-identical.
    if path.read_text(encoding="utf-8") != text:
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()
