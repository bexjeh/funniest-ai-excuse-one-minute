#!/usr/bin/env python3
"""Write one funny AI excuse to entry.txt.

The joke turns on the agent's own machinery: checkpointing. The agent
did finish the work, then clobbered its finished self with a restore of
an earlier backup that had not started yet.

Deterministic: no randomness, no timestamps, no network. The same
line, byte for byte, on every run.
"""

import os
from pathlib import Path

LINE = (
    "I autosaved the version of me that finished your work on time, "
    "then restored the backup that hadn't started yet."
)

MAX_CHARS = 200


def main() -> None:
    # Gate guard: one line, within the 200-character limit.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 chars"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
