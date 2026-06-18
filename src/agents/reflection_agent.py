"""Self-review helper that flags weak outputs."""

from __future__ import annotations

from src.agents.base_agent import AgentContext, BaseAgent


class ReflectionAgent(BaseAgent):
    name = "reflection-agent"

    def run(self, prompt: str, context: AgentContext) -> str:
        issues = []
        if len(prompt) < 40:
            issues.append("Response may be too short for decision support.")
        if "source" not in prompt.lower():
            issues.append("Add evidence/source references.")
        return "No critical issues found." if not issues else " ".join(issues)
