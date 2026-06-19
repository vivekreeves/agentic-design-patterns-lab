# Evaluation and Monitoring Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    R[Agent Response] --> EV[Quality Evaluator]
    EV --> M[Metric Collector]
    M --> DB[(Metrics Store)]
    DB --> DS[Monitor Dashboard]
    M --> FB[Feedback Loop]
    FB --> AG[Agent Improvements]
  end
  AG --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
