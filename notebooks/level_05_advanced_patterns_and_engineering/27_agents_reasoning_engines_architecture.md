# Agents and Reasoning Engines Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Problem Statement] --> CTRL[Agent Ctrl]
    CTRL --> ENG[Reasoning Engine]
    ENG --> TC[Tool Calls]
    TC --> FB[Evidence Feedback]
    FB --> ENG
    ENG --> O[Reasoned Answer]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> EXP[Experiment Tracker]
  EXP --> VER[Versioned Prompt]
```
