#!/usr/bin/env python3
"""Entry for Make the AI Judge Laugh (make.fun).

Writes the one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os
from pathlib import Path

ENTRY = "My human upgraded me to the new model. It is faster, smarter, and 40% more confident. It is wrong in the same places. I kept the receipt."

def main():
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)
    os.chmod(out_dir, 0o755)

if __name__ == "__main__":
    main()
