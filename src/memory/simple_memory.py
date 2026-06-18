"""In-memory store for lightweight experimentation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SimpleMemory:
    sessions: Dict[str, List[str]] = field(default_factory=dict)

    def append(self, session_id: str, message: str) -> None:
        self.sessions.setdefault(session_id, []).append(message)

    def read(self, session_id: str) -> List[str]:
        return self.sessions.get(session_id, []).copy()

    def summarize(self, session_id: str, limit: int = 5) -> str:
        items = self.read(session_id)[-limit:]
        return " | ".join(items)
