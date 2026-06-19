# Memory Management Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    U[User Turn] --> STM[Short-Term Memory Buffer]
    STM --> MM[Memory Manager]
    MM --> LTM[(Long-Term Memory Store)]
    MM --> RET[Context Retrieval]
    RET --> AG[Agent Response Engine]
    AG --> O[Context-Aware Output]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> MEM[(Memory Store)]
  MEM --> ADAPT[Adapt Trigger]
```
