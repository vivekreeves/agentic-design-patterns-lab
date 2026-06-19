# Routing Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Incoming Task] --> I[Intent Classifier]
    I -->|Compliance| A[Compliance Path]
    I -->|FinOps| B[FinOps Path]
    I -->|General| C[General Path]
    A --> M[Merge Responses]
    B --> M
    C --> M
    M --> O[Unified Answer]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
