"""Simple keyword search over text blocks."""

from __future__ import annotations

from typing import Iterable, List


def keyword_search(query: str, corpus: Iterable[str]) -> List[str]:
    q = query.lower().strip()
    return [item for item in corpus if q in item.lower()]
