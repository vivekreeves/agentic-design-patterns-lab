# Human in the Loop Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[High-Impact Request] --> D[Agent Draft]
    D --> RG[Risk Gate]
    RG --> H[Human Reviewer]
    H -->|Approve| P[Publish Result]
    H -->|Revise| D
  end
  P --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SAFE[Safety Check]
  SAFE --> ESC[Escalation]
```
