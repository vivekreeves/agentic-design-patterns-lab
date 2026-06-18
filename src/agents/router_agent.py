"""Route tasks based on simple intent labels."""

from __future__ import annotations

from src.agents.base_agent import AgentContext, BaseAgent


class RouterAgent(BaseAgent):
    name = "router-agent"

    def run(self, prompt: str, context: AgentContext) -> str:
        p = prompt.lower()
        if any(k in p for k in ["cost", "budget", "token"]):
            return "finops"
        if any(k in p for k in ["risk", "control", "regulatory"]):
            return "compliance"
        if any(k in p for k in ["latency", "performance"]):
            return "monitoring"
        return "general"
