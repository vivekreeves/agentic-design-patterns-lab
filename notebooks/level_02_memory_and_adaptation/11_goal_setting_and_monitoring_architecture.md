# Goal Setting and Monitoring Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    B[Business Objective] --> GR[Goal Registry]
    GR --> KP[KPI Definitions]
    KP --> MON[Live Monitor]
    MON --> AL[Alerts]
    MON --> ADJ[Goal Adjuster]
    ADJ --> GR
  end
  ADJ --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> MEM[(Memory Store)]
  MEM --> ADAPT[Adapt Trigger]
```
