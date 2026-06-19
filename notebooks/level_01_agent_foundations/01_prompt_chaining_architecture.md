# Prompt Chaining Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    U[User Prompt] --> C1[Chain Step 1: Extract Intent]
    C1 --> C2[Chain Step 2: Gather Evidence]
    C2 --> C3[Chain Step 3: Draft Response]
    C3 --> V[Validation Check]
    V --> O[Final Output]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> L1[Foundation Loop]
```
