# Contributing Guide

## Principles
- Keep content original and educational.
- Prefer local, deterministic examples over paid API dependencies.
- Maintain consistency between notebook and matching study note.

## Development Workflow
1. Create a branch from `main`.
2. Make focused commits with clear messages.
3. Validate notebooks open correctly and run cells top-to-bottom.
4. Open a pull request with:
   - What changed
   - Why it changed
   - How it was validated

## Notebook Standards
Each notebook should include:
1. Title
2. Learning objectives
3. Concept explanation
4. Architecture diagram
5. Python implementation
6. Mock LLM or mock agent example
7. Banking/regulatory example when relevant
8. Logging or monitoring example when relevant
9. Exercises
10. Final summary

## Study Note Standards
Each `.txt` file must include all 17 required sections in order.

## Code Style
- Python 3.10+
- Keep modules lightweight and testable
- Use clear logging and explicit data models where useful
