# Guardrails and Safety Patterns Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    IN[User Input] --> IF[Input Policy Filter]
    IF --> PL[Planner]
    PL --> ACT[Action Generator]
    ACT --> AF[Action Guardrail]
    AF --> OS[Output Sanitizer]
    OS --> O[Safe Response]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> SLO[SLO Check]
  SLO --> ORCH[Orchestrator Update]
```
