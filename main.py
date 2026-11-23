"""Write the one-line make.fun entry to the output directory."""

import os
import sys
from pathlib import Path

ENTRY = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."


def main() -> None:
    assert 1 <= len(ENTRY) <= 280
    output_dir_name = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    output_dir = Path(output_dir_name)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))
    print(len(ENTRY), file=sys.stderr)


if __name__ == "__main__":
    main()
