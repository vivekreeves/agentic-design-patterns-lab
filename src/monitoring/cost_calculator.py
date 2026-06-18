"""Estimate request cost using token usage."""

from __future__ import annotations


def estimate_cost(tokens: int, price_per_1k_tokens: float = 0.002) -> float:
    return round((tokens / 1000.0) * price_per_1k_tokens, 6)
