"""Base abstractions for simple agent experiments."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class AgentContext:
    request_id: str
    metadata: Dict[str, str] = field(default_factory=dict)


class BaseAgent:
    name: str = "base-agent"

    def run(self, prompt: str, context: AgentContext) -> str:
        raise NotImplementedError("Subclasses must implement run()")
