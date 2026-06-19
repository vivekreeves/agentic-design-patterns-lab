# Model Routing and Cost Optimization Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    T[Task] --> CX[Complexity Classifier]
    CX -->|Simple| SM[Small Model]
    CX -->|Complex| LM[Large Model]
    SM --> CM[Cost Monitor]
    LM --> CM
    CM --> RT[Routing Policy Tuner]
    RT --> O[Balanced Quality-Cost Output]
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
