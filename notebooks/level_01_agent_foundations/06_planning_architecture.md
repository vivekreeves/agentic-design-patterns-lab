# Planning Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    G[Goal] --> P[Plan Generator]
    P --> Q[Task Queue]
    Q --> E1[Execute Step 1]
    E1 --> E2[Execute Step 2]
    E2 --> RV[Plan Review]
    RV --> O[Result + Next Steps]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
