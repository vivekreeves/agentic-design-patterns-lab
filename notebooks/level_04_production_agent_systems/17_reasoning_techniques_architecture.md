# Reasoning Techniques Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    T[Task] --> RS[Reasoning Strategy Selector]
    RS --> COT[Chain-of-Thought Path]
    RS --> TOT[Tree-of-Thought Path]
    RS --> SCR[Scratchpad Path]
    COT --> VER[Verifier]
    TOT --> VER
    SCR --> VER
    VER --> O[Validated Answer]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
