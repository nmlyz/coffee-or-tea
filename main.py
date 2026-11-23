#!/usr/bin/env python3
import os
import sys

CHOICE = "A"


def main() -> int:
    if CHOICE not in ("A", "B") or len(CHOICE) != 1:
        print("invalid choice", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(CHOICE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "rb") as f:
        data = f.read()
    if data != CHOICE.encode("ascii") or len(data) != 1 or data != b"A":
        print(f"verification failed: {data!r}", file=sys.stderr)
        return 1
    print(f"wrote {path}: {data!r} ({len(data)} byte)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
