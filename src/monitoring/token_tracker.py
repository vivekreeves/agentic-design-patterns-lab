"""Token accounting utility for local estimation."""

from __future__ import annotations


def estimate_tokens(text: str) -> int:
    # Rough heuristic for educational usage.
    return max(1, len(text.split()) * 2)
