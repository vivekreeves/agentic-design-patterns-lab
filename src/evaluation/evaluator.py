"""Score answer quality using lightweight rubric checks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    score: float
    feedback: str


def evaluate_answer(answer: str) -> EvaluationResult:
    score = 1.0
    feedback = []
    if len(answer) < 80:
        score -= 0.3
        feedback.append("Expand explanation depth.")
    if "risk" not in answer.lower():
        score -= 0.2
        feedback.append("Include explicit risk considerations.")
    if "next" not in answer.lower():
        score -= 0.1
        feedback.append("Add clear next steps.")
    score = max(0.0, round(score, 2))
    return EvaluationResult(score=score, feedback=" ".join(feedback) or "Solid baseline response.")
