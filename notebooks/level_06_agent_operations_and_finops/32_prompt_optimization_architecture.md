# Prompt Optimization Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    B[Baseline Prompt] --> GEN[Candidate Generator]
    GEN --> AB[A/B Evaluator]
    AB --> WIN[Best Prompt Selector]
    WIN --> DEP[Production Prompt]
    DEP --> MON[Performance Monitor]
  end
  MON --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> CDB[(Cost-Latency Dash)]
  CDB --> ACT[FinOps Queue]
```
