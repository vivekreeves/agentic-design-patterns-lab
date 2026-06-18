# agentic-design-patterns-lab

"Software patterns organise systems. Agentic patterns organise intelligence."

Traditional software design patterns help engineers structure objects, services, interfaces, and workflows. Agentic AI design patterns help engineers structure reasoning, planning, tool use, memory, collaboration, evaluation, safety, and cost-aware execution.

## Repository Purpose
This repository is an original, level-based lab for learning agentic AI design patterns through:
- Executable Jupyter notebooks
- Matching text study notes
- Lightweight local Python modules for agents, tools, memory, monitoring, evaluation, and FinOps

The project is educational, practical, and production-minded. All examples are designed to run locally without paid APIs.

## What You Will Learn
- Core agentic patterns: prompt chaining, routing, reflection, planning, tool use, and multi-agent orchestration
- Reliability patterns: exception recovery, human-in-the-loop, and guardrails
- Production patterns: observability, evaluation, prioritization, and operational controls
- FinOps patterns: token cost, latency trade-offs, context optimization, and model routing

## Study Roadmap
1. Level 01: Agent foundations
2. Level 02: Memory and adaptation
3. Level 03: Reliability and knowledge
4. Level 04: Production agent systems
5. Level 05: Advanced patterns and engineering
6. Level 06: Agent operations and FinOps

See `docs/learning-roadmap.md` for details.

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name agentic-design-patterns-lab --display-name "Python (Agentic Lab)"
jupyter notebook
```

## Repository Layout
- `docs/`: concept references and structured study support
- `diagrams/`: architecture overviews in Mermaid
- `data/sample/`: local sample data for notebook exercises
- `src/`: reusable Python modules for local experiments
- `notebooks/`: level-based lessons with paired `.ipynb` and `.txt` files

## Local-Only Design
- Uses mock LLM behavior for deterministic local execution
- No mandatory API keys
- Optional extension points are marked in comments for future integration with OpenAI, Gemini, Claude, LangGraph, CrewAI, or MCP-compatible infrastructure

## Contribution
Read `CONTRIBUTING.md` before opening pull requests.

## License
This project is licensed under the MIT License. See `LICENSE`.
