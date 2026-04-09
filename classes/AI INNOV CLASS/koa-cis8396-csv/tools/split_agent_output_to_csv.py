#!/usr/bin/env python3
"""
Split marker-wrapped CSV sections from a full agent output into two .csv files.

Usage:
  python3 split_agent_output_to_csv.py run_output.txt ./out/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from validate_csv_output import _extract_block  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Split dual CSV agent output into files.")
    p.add_argument("input_path", help="Path to full agent output .txt")
    p.add_argument(
        "out_dir",
        nargs="?",
        default=".",
        help="Directory for sentiment_summary.csv and issue_log.csv",
    )
    args = p.parse_args()
    text = Path(args.input_path).read_text(encoding="utf-8", errors="replace")
    try:
        s_block = _extract_block(
            text,
            "===BEGIN_SENTIMENT_SUMMARY_CSV===",
            "===END_SENTIMENT_SUMMARY_CSV===",
        )
        i_block = _extract_block(
            text, "===BEGIN_ISSUE_LOG_CSV===", "===END_ISSUE_LOG_CSV==="
        )
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "sentiment_summary.csv").write_text(s_block.strip() + "\n", encoding="utf-8")
    (out / "issue_log.csv").write_text(i_block.strip() + "\n", encoding="utf-8")
    print(f"Wrote {out / 'sentiment_summary.csv'}")
    print(f"Wrote {out / 'issue_log.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
