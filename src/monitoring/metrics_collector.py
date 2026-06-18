"""Collect quality, cost, and latency metrics."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Metrics:
    quality_score: float
    latency_seconds: float
    token_count: int
    cost_estimate: float
