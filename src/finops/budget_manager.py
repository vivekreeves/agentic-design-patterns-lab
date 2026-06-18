"""Track spending against a project budget."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BudgetManager:
    total_budget: float
    spent: float = 0.0

    def can_spend(self, amount: float) -> bool:
        return (self.spent + amount) <= self.total_budget

    def register(self, amount: float) -> None:
        if not self.can_spend(amount):
            raise ValueError("Budget exceeded")
        self.spent += amount

    @property
    def remaining(self) -> float:
        return self.total_budget - self.spent
