# Inter-Agent Communication (A2A) Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    A1[Agent A] --> BUS[A2A Message Bus]
    A2[Agent B] --> BUS
    A3[Agent C] --> BUS
    BUS --> PRO[Protocol Translator]
    PRO --> ST[Shared Task State]
    ST --> RES[Coordinated Output]
  end
  RES --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
