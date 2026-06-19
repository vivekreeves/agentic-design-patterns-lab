# Reflection Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    P[Prompt] --> D[Initial Draft]
    D --> R[Reflection Critic]
    R -->|Needs Improvement| D2[Revised Draft]
    R -->|Acceptable| O[Final Answer]
    D2 --> R
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
