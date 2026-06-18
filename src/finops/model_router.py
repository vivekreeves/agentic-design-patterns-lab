"""Choose model tier based on task complexity and budget."""

from __future__ import annotations


def route_model(complexity: str, budget_remaining: float) -> str:
    if budget_remaining < 1.0:
        return "small-local-model"
    if complexity in {"high", "critical"}:
        return "high-capability-model"
    return "balanced-model"
