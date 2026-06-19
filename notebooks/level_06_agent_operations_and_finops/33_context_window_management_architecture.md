# Context Window Management Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    S[Context Sources] --> RK[Relevance Ranker]
    RK --> PK[Window Packer]
    PK --> OF[Overflow Summarizer]
    OF --> CTX[Final Context Window]
    CTX --> M[Model Call]
    M --> O[Context-Bounded Output]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> CDB[(Cost-Latency Dash)]
  CDB --> ACT[FinOps Queue]
```
