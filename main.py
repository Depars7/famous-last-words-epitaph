#!/usr/bin/env python3
"""Write the chosen epitaph entry to /output/entry.txt.

Deterministic, stdlib only: the exact entry text, no trailing newline,
file mode 0644. /output is created if needed; the directory itself is
never chmodded.
"""

import os

ENTRY = "I died doing what I loved: ignoring the terms and conditions."

# Gate: 1-150 characters, not whitespace-only.
if not 1 <= len(ENTRY) <= 150 or not ENTRY.strip():
    raise ValueError("ENTRY must be 1-150 non-whitespace characters")


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    # Binary write: no newline translation on any platform, no trailing newline.
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))
    os.chmod(path, 0o644)
    # Verify: what landed on disk must be byte-identical to ENTRY.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise RuntimeError("entry.txt does not match ENTRY byte-for-byte")
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
