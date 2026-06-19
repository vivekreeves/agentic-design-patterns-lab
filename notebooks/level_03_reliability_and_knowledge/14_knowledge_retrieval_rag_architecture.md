# Knowledge Retrieval (RAG) Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[User Query] --> RET[Retriever]
    RET --> VS[(Knowledge Index)]
    VS --> CTX[Context Builder]
    CTX --> GEN[Answer Generator]
    GEN --> CIT[Citation Check]
    CIT --> O[Grounded Response]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SAFE[Safety Check]
  SAFE --> ESC[Escalation]
```
