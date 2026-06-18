"""Estimate workflow-level cost from step token usage."""

from __future__ import annotations

from typing import Iterable


def estimate_workflow_cost(step_tokens: Iterable[int], price_per_1k_tokens: float) -> float:
    total_tokens = sum(step_tokens)
    return round((total_tokens / 1000.0) * price_per_1k_tokens, 6)
