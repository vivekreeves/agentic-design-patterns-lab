# Parallelization Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    T[Task] --> OR[Parallel Orchestrator]
    OR --> W1[Worker 1: Data Pull]
    OR --> W2[Worker 2: Risk Scan]
    OR --> W3[Worker 3: Policy Check]
    W1 --> AG[Aggregator]
    W2 --> AG
    W3 --> AG
    AG --> O[Consolidated Output]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
