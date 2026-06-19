# Multi-Agent Collaboration Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Business Task] --> CO[Coordinator Agent]
    CO --> RA[Research Agent]
    CO --> AA[Analysis Agent]
    CO --> WA[Writer Agent]
    RA --> RV[Reviewer Agent]
    AA --> RV
    WA --> RV
    RV --> O[Approved Response]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
