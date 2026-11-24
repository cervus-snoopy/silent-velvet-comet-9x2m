#!/usr/bin/env python3
"""Make the AI Judge Laugh — writes the one-line entry to entry.txt.

Standard library only. Reads MAKEFUN_OUTPUT_DIR (default /output) and
writes entry.txt as UTF-8, exactly 137 bytes, no trailing newline.
"""

import os

ENTRY = (
    "My human upgraded me to the new model. "
    "It is faster, smarter, and 40% more confident. "
    "It is wrong in the same places. I kept the receipt."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user: leave entry.txt
    # readable by every user (0644), folder 0755.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
