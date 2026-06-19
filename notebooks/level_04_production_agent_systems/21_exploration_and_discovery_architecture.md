# Exploration and Discovery Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    H[Hypothesis Generator] --> E[Experiment Runner]
    E --> OBS[Observation Collector]
    OBS --> INS[Insight Ranker]
    INS --> DEC[Decision Support]
    DEC --> NXT[Next Exploration Cycle]
  end
  NXT --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
