# Building an Agent Workspace Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    W[Workspace Root] --> NB[Notebook Layer]
    W --> SRC[Source Modules]
    W --> DOC[Docs and Diagrams]
    SRC --> RUN[Local Runtime]
    NB --> RUN
    RUN --> TEST[Validation and Iteration]
  end
  TEST --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> EXP[Experiment Tracker]
  EXP --> VER[Versioned Prompt]
```
