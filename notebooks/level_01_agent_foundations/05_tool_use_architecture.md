# Tool Use Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Query] --> PL[Tool Planner]
    PL --> TS[Tool Selector]
    TS --> CALC[Calculator Tool]
    TS --> SRCH[Search Tool]
    TS --> DB[Mock Database]
    CALC --> SYN[Synthesis Layer]
    SRCH --> SYN
    DB --> SYN
    SYN --> O[Grounded Response]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
