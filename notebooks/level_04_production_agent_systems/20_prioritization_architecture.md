# Prioritization Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Task Intake] --> SC[Priority Scorer]
    SC --> HQ[High Priority Queue]
    SC --> MQ[Medium Priority Queue]
    SC --> LQ[Low Priority Queue]
    HQ --> DISP[Dispatcher]
    MQ --> DISP
    LQ --> DISP
    DISP --> O[Execution Order]
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
