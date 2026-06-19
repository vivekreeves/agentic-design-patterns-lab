# AI FinOps Dashboard Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    TM[Token Metrics] --> ETL[FinOps ETL]
    CM[Cost Metrics] --> ETL
    LM[Latency Metrics] --> ETL
    ETL --> WH[(FinOps WH)]
    WH --> PN[Dashboard Views]
    PN --> AN[Anomaly Alerting]
    AN --> ACT[Optimization Queue]
  end
  ACT --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> CDB[(Cost-Latency Dash)]
  CDB --> ACT[FinOps Queue]
```
