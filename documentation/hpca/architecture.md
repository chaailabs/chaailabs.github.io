# HPCA architecture

```mermaid
flowchart LR
  Y[project specification] --> G[schema gate]
  G --> O[orchestrator]
  O --> D[dependency graph]
  D --> J[scheduler adapter]
  J --> X[simulation jobs]
  X --> A[artifact registry]
  A --> Q[scientific validation]
  Q --> O
```

Core invariants are configuration-driven site behavior, explicit stage dependencies, idempotent completion checks, durable state, scheduler reconciliation, immutable provenance records, and no advancement past a failed validation gate.

