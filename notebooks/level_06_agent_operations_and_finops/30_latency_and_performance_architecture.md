# Latency and Performance Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    REQ[Request] --> TR[Latency Tracer]
    TR --> BP[Bottleneck Profiler]
    BP --> OPT[Optimization Engine]
    OPT --> EXEC[Optimized Execution]
    EXEC --> O[Low-Latency Output]
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
