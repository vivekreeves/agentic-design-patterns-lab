# Multi-Agent Cost Analysis Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    OR[Orchestrator] --> A1[Agent 1]
    OR --> A2[Agent 2]
    OR --> A3[Agent 3]
    A1 --> TL[Token Logs]
    A2 --> TL
    A3 --> TL
    TL --> CA[Cost Analyzer]
    CA --> RP[Optimization Report]
  end
  RP --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> CDB[(Cost-Latency Dash)]
  CDB --> ACT[FinOps Queue]
```
