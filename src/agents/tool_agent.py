"""Demonstrates simple tool-selection logic."""

from __future__ import annotations

from src.agents.base_agent import AgentContext, BaseAgent
from src.tools.calculator_tool import calculate


class ToolAgent(BaseAgent):
    name = "tool-agent"

    def run(self, prompt: str, context: AgentContext) -> str:
        if prompt.startswith("calc:"):
            expr = prompt.split("calc:", 1)[1].strip()
            return f"calculated={calculate(expr):.4f}"
        return "No tool invoked. Prefix with 'calc:' to use calculator."
