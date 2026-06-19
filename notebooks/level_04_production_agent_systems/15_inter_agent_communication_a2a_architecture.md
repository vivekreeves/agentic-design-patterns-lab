# Inter-Agent Communication (A2A) Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  Q[User Task] --> A[Agent Controller]
  A --> P[Pattern: Inter-Agent Communication (A2A)]
  P --> T[Tools / Data]
  P --> M[Memory / State]
  P --> O[Output + Metrics]
```
