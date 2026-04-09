#!/usr/bin/env python3
"""
Validate PART 2 of a combined agent response: two marker-wrapped CSV blocks.
Ignores any prose (e.g. PDF-style PART 1) before ===BEGIN_SENTIMENT_SUMMARY_CSV===.

Usage:
  python3 validate_csv_output.py path/to/full_output.txt
  python3 validate_csv_output.py   # reads stdin
"""

from __future__ import annotations

import csv
import io
import sys
from pathlib import Path
from typing import List, Tuple

SENTIMENT_HEADER = (
    "campground_id,campground_name,avg_sentiment_score,total_reviews,"
    "top_issue_theme,severity_level,recommended_action"
)
ISSUE_HEADER = (
    "issue_id,campground_id,issue_description,severity,root_cause_hypothesis,"
    "recommended_action,assigned_to,due_date,status"
)


def _read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    return sys.stdin.read()


def _extract_block(text: str, begin: str, end: str) -> str:
    i = text.find(begin)
    if i < 0:
        raise ValueError(f"Missing marker: {begin!r}")
    j = text.find(end, i + len(begin))
    if j < 0:
        raise ValueError(f"Missing marker: {end!r}")
    inner = text[i + len(begin) : j]
    return inner.strip("\n")


def _check_fences(text: str) -> None:
    if "```" in text:
        raise ValueError(
            "Found markdown code fences (```) in output; remove them for reliable CSV extract."
        )


def _parse_csv_block(name: str, block: str, expected_header: str) -> List[List[str]]:
    lines = [ln for ln in block.splitlines() if ln.strip()]
    if not lines:
        raise ValueError(f"{name}: empty CSV block")
    header_row = next(csv.reader([lines[0]]))
    expected_cols = next(csv.reader(io.StringIO(expected_header)))
    if header_row != expected_cols:
        raise ValueError(
            f"{name}: header mismatch.\n  got:      {header_row}\n  expected: {expected_cols}"
        )
    rows: List[List[str]] = []
    for line in lines[1:]:
        rows.append(next(csv.reader([line])))
    return rows


def validate(text: str) -> Tuple[List[List[str]], List[List[str]]]:
    _check_fences(text)

    s_block = _extract_block(
        text, "===BEGIN_SENTIMENT_SUMMARY_CSV===", "===END_SENTIMENT_SUMMARY_CSV==="
    )
    i_block = _extract_block(
        text, "===BEGIN_ISSUE_LOG_CSV===", "===END_ISSUE_LOG_CSV==="
    )

    end_s = text.find("===END_SENTIMENT_SUMMARY_CSV===")
    begin_i = text.find("===BEGIN_ISSUE_LOG_CSV===")
    if begin_i >= 0 and end_s > begin_i:
        raise ValueError("Issue Log CSV appears before Sentiment Summary ends; check order.")

    sentiment_rows = _parse_csv_block("Sentiment Summary", s_block, SENTIMENT_HEADER)
    issue_rows = _parse_csv_block("Issue Log", i_block, ISSUE_HEADER)

    if not sentiment_rows:
        raise ValueError("Sentiment Summary: no data rows after header")
    if not issue_rows:
        raise ValueError("Issue Log: no data rows after header")

    return sentiment_rows, issue_rows


def main() -> int:
    argv = [a for a in sys.argv[1:] if a not in ("-h", "--help")]
    path = argv[0] if argv else None
    try:
        text = _read_text(path)
    except OSError as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        return 2
    if not text.strip():
        print("Empty input.", file=sys.stderr)
        return 2
    try:
        s_rows, i_rows = validate(text)
    except ValueError as e:
        print(f"VALIDATION FAILED: {e}", file=sys.stderr)
        return 1
    print("OK: PART 2 CSV blocks parse.")
    print(f"  Sentiment Summary rows: {len(s_rows)}")
    print(f"  Issue Log rows:         {len(i_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
