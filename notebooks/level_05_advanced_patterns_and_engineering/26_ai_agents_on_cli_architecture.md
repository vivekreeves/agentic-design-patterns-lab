# AI Agents on CLI Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    CMD[CLI Command] --> PARSE[Argument Parser]
    PARSE --> AG[Agent Runtime]
    AG --> TL[Tool Invocation]
    TL --> OUT[Terminal Output]
    OUT --> LOG[Run Log]
  end
  LOG --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> EXP[Experiment Tracker]
  EXP --> VER[Versioned Prompt]
```
