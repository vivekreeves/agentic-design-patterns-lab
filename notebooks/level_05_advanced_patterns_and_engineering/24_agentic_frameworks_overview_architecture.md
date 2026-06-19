# Agentic Frameworks Overview Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    APP[Agent Application] --> ADR[Framework Adapter Layer]
    ADR --> FG1[Graph Framework Path]
    ADR --> FG2[Crew Framework Path]
    ADR --> FG3[Custom Runtime Path]
    FG1 --> SH[Shared Tools and Memory]
    FG2 --> SH
    FG3 --> SH
    SH --> O[Comparable Outcomes]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> EXP[Experiment Tracker]
  EXP --> VER[Versioned Prompt]
```
