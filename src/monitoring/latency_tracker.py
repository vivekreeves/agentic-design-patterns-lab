"""Simple latency measurement helpers."""

from __future__ import annotations

import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def timed() -> Iterator[dict]:
    state = {"seconds": 0.0}
    start = time.perf_counter()
    try:
        yield state
    finally:
        state["seconds"] = time.perf_counter() - start
