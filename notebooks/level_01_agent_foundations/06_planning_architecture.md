# Planning Architecture

This diagram is extracted from the notebook so GitHub can render Mermaid reliably.

```mermaid
flowchart LR
  Q[User Task] --> A[Agent Controller]
  A --> P[Pattern: Planning]
  P --> T[Tools / Data]
  P --> M[Memory / State]
  P --> O[Output + Metrics]
```
