# Exception Handling and Recovery Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    X[Workflow Execution] --> TRY[Try Step]
    TRY -->|Success| O[Normal Output]
    TRY -->|Failure| ERR[Error Classifier]
    ERR --> RET[Retry Policy]
    ERR --> FB[Fallback Path]
    ERR --> ESC[Human Escalation]
    RET --> TRY
  end
  ESC --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SAFE[Safety Check]
  SAFE --> ESC[Escalation]
```
