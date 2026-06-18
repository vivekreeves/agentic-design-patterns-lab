"""Create an ordered plan from a high-level objective."""

from __future__ import annotations

from src.agents.base_agent import AgentContext, BaseAgent


class PlannerAgent(BaseAgent):
    name = "planner-agent"

    def run(self, prompt: str, context: AgentContext) -> str:
        steps = [
            "Clarify objective and constraints",
            "Gather required data and tools",
            "Generate candidate response",
            "Validate against policy and quality checks",
            "Return answer with confidence and next actions",
        ]
        return "\n".join(f"{idx}. {step}" for idx, step in enumerate(steps, 1))
