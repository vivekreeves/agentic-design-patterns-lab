# Model Context Protocol (MCP) Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  subgraph CoreFlow[Core Pattern Flow]
    A[Agent Runtime] --> C[MCP Client]
    C --> S[MCP Server]
    S --> T1[Tool Endpoint]
    S --> T2[Resource Endpoint]
    T1 --> C
    T2 --> C
    C --> O[Tool-Augmented Output]
  end
  O --> QG{Quality Gate}
  QG -->|Pass| PUB[Publish]
  QG -->|Review| HREV[Human Review]
  HREV --> PUB
  PUB --> OBS[Obs + Cost Metrics]
  OBS --> LOOP[Improvement Loop]
  LOOP --> MEM[(Memory Store)]
  MEM --> ADAPT[Adapt Trigger]
```
