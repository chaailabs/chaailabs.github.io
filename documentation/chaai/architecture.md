# Chaai architecture

```mermaid
flowchart TB
  CLI[Terminal or API] --> A[Agent session]
  A --> I[Inference backend]
  A --> R[Tool registry]
  R --> T[Scheduler and scientific tools]
  A --> M[Context and checkpoints]
  T --> E[Controlled execution boundary]
  E --> HPC[HPC resources]
```

The agent owns conversation and planning state. Inference backends provide model responses. Typed tool schemas constrain intended actions. Checkpoints preserve resumability. A production execution boundary must independently enforce permissions; prompt instructions alone are not a security control.

