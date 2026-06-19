# Token Cost Management Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    REQ[Request] --> TOK[Token Estimator]
    TOK --> BG[Budget Guardrail]
    BG --> CMP[Prompt Compressor]
    CMP --> MOD[Model Invocation]
    MOD --> CST[Cost Logger]
    CST --> O[Cost-Aware Response]
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
