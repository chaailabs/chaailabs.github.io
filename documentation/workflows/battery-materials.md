# Battery-materials workflow

The reference workflow connects a decision to a fidelity ladder:

```mermaid
flowchart TB
  Q[Decision and targets] --> S[Candidate structures]
  S --> D[DFT and AIMD]
  D --> M[MLIP training]
  M --> V[Domain validation]
  V --> P[Production MD]
  P --> A[Transport and interface analysis]
  A --> E[Experimental or design decision]
```

Validation must reflect the intended operating domain: composition, phase, temperature, strain, defects, interfaces and reaction states. Random frame splits are insufficient when adjacent trajectory frames are correlated.
