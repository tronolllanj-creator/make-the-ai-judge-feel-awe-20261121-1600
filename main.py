"""Writes a fixed poetic text to entry.txt in the output directory."""

import os
import sys

# The vast, quiet sky stretching endlessly; growth beyond the visible horizon. 
TEXT = "Stars bloom, soft and distant. The air is still, cool against your skin. The horizon fades into endless dark. You are small, held by the silence. The sky goes on, quiet and vast."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not (1 <= len(TEXT) <= 280):
        raise AssertionError("TEXT length must be between 1 and 280 characters")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(len(TEXT))


if __name__ == "__main__":
    main()