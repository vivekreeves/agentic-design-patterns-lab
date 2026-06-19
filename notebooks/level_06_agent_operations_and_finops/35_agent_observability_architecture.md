# Agent Observability Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    AG[Agent Runtime] --> EV[Event Stream]
    EV --> MC[Metrics Collector]
    MC --> ST[(Observability Store)]
    ST --> DB[Operations Dashboard]
    ST --> AL[Alert Rules]
    AL --> OPS[On-Call Actions]
  end
  OPS --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> CDB[(Cost-Latency Dash)]
  CDB --> ACT[FinOps Queue]
```
