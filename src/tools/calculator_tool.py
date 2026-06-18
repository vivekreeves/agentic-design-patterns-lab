"""Deterministic math utility for notebook examples."""

from __future__ import annotations


def calculate(expression: str) -> float:
    allowed = set("0123456789+-*/(). ")
    if any(ch not in allowed for ch in expression):
        raise ValueError("Unsupported characters in expression")
    return float(eval(expression, {"__builtins__": {}}, {}))
