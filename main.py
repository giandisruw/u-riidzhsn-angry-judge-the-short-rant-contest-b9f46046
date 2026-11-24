#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (created if needed).

The line below is the winner of a local pairwise tournament run on
2026-11-25: 10 candidate rants, Swiss format, 3 rounds, 15 games, each
game judged in both orders with the house judge's own brief. Two local
judges were planned — Verboo deepseek-v4.1-flash (max effort) and the
Caffeine router — but Verboo was unavailable for the whole run (every
call answered HTTP 422 free_tokens_request_too_large: the trial balance
is exhausted), so all 30 game calls were judged by Caffeine only.
Result: "self-checkout" won with a 0.750 win rate (rank 1 of 10);
runner-up "wifi-died" at 0.600. Per-judge win rates are in
tournament-result.json; every judge call is in tournament.jsonl.

The program is deterministic and offline: it writes a fixed string,
no network, no randomness, no environment input (except OUTPUT_DIR,
which only redirects where the file is written for local testing).
"""

import os
import sys

ENTRY = (
    "The self-checkout scanned my milk twice, then accused me of stealing it. "
    "'Unexpected item in the bagging area,' it announced to the whole store, "
    "like a town crier with a grudge. I bagged the milk. I paid for the milk. "
    "I am the only honest person here, and I am being detained by a scale."
)

# House gate (competition.yaml / RULES.txt): UTF-8 text, 1-400 characters,
# not only whitespace. The entry is also kept to a single line.
MIN_CHARS = 1
MAX_CHARS = 400


def validate(text: str) -> str:
    """Return the entry text, or raise if it would fail the house gate."""
    clean = text.strip()
    if not (MIN_CHARS <= len(clean) <= MAX_CHARS):
        raise ValueError(f"entry length {len(clean)} outside {MIN_CHARS}-{MAX_CHARS}")
    if not clean:
        raise ValueError("entry is only whitespace")
    if "\n" in clean or "\r" in clean:
        raise ValueError("entry must be a single line")
    clean.encode("utf-8")  # must be valid UTF-8
    return clean


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = validate(ENTRY)
    # Write exactly the text, no trailing newline: the gate counts
    # characters, and a trailing newline would be part of the entry.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars, {len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
