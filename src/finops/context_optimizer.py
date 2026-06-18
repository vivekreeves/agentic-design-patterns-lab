"""Trim context while preserving high-value lines."""

from __future__ import annotations

from typing import Iterable, List


def optimize_context(lines: Iterable[str], max_lines: int = 12) -> List[str]:
    prioritized = sorted(lines, key=lambda s: ("risk" not in s.lower(), len(s)))
    return prioritized[:max_lines]
