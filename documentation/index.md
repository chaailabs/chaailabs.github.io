# Chaai Labs documentation

Chaai Labs develops HPC-native systems for computational science. **Chaai** provides the conversational reasoning and scientific-tool interface; **HPCA** provides validated, restartable workflow execution.

```mermaid
flowchart LR
  U[Scientist] --> C[Chaai reasoning and tools]
  C --> P[Validated project specification]
  P --> H[HPCA execution engine]
  H --> S[Scheduler and simulation codes]
  S --> V[Validated artifacts and provenance]
  V --> C
```

!!! note "Current maturity"
    Chaai is a working research prototype deployed on HPC. HPCA is a deterministic workflow engine under active development. Neither label is a substitute for site authorization, scientific review, or validation of a specific result.

Start with the [system overview](getting-started/overview.md) or the [first workflow](getting-started/first-workflow.md).

