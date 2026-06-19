# Resource-Aware Optimization Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    W[Incoming Workload] --> PF[Resource Profiler]
    PF --> PO[Policy Engine: Cost/Latency]
    PO --> SCH[Adaptive Scheduler]
    SCH --> SEL[Model/Tool Selector]
    SEL --> EX[Execution]
    EX --> O[Optimized Result]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
