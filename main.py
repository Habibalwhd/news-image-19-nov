"""Copy the repo-held news image to the output directory."""
import os
import shutil
import sys

MAX_BYTES = 1_048_576  # entry.png must stay at most 1 MiB


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        sys.exit(f"entry.png is {size} bytes, over the 1 MiB limit")
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
