# Learning and Adaptation Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    R[Run Episode] --> FB[Collect Feedback]
    FB --> SC[Performance Scorer]
    SC --> UP[Policy/Prompt Updater]
    UP --> KB[Adaptation Memory]
    KB --> N[Next Episode]
  end
  N --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> MEM[(Memory Store)]
  MEM --> ADAPT[Adapt Trigger]
```
