# Advanced Prompting Techniques Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    Q[Task] --> PC[Prompt Constructor]
    PC --> FS[Few-Shot Context]
    PC --> CT[Constraint Template]
    PC --> RF[Role Framing]
    FS --> M[Model Call]
    CT --> M
    RF --> M
    M --> QC[Quality Check]
    QC --> O[Improved Output]
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
