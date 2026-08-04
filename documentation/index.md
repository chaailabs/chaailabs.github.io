---
hide:
  - toc
---

<div class="chaai-hero" markdown>

<span class="chaai-eyebrow">HPC-native scientific infrastructure</span>

# From scientific intent to validated execution

Chaai Labs connects agentic reasoning, simulation tools, and durable HPC workflows. **Chaai** provides the scientific interface; **HPCA** turns validated specifications into restartable, traceable execution.

[Start with the overview](getting-started/overview.md){ .md-button .md-button--primary }
[Explore HPCA](hpca/index.md){ .md-button }
[← Main Chaai Labs website](https://chaailabs.github.io/){ .md-button }

</div>

<div class="chaai-grid" markdown>

<div class="chaai-card">
  <span class="chaai-card__number">01</span>
  <h3>Chaai</h3>
  <p>Conversational scientific reasoning connected to schedulers, files, structures, simulation codes, and analysis tools.</p>
  <a class="chaai-card__link" href="chaai/">Explore the agent →</a>
</div>

<div class="chaai-card">
  <span class="chaai-card__number">02</span>
  <h3>HPCA engine</h3>
  <p>Deterministic stage contracts, durable state, scheduler reconciliation, validation gates, and provenance.</p>
  <a class="chaai-card__link" href="hpca/">Explore the engine →</a>
</div>

<div class="chaai-card">
  <span class="chaai-card__number">03</span>
  <h3>Scientific workflows</h3>
  <p>Composable workflows for battery materials and machine-learned interatomic-potential lifecycles.</p>
  <a class="chaai-card__link" href="workflows/battery-materials/">View workflows →</a>
</div>

<div class="chaai-card">
  <span class="chaai-card__number">04</span>
  <h3>Operations</h3>
  <p>Observe workflow state, reconcile scheduler jobs, diagnose failures, and recover without losing evidence.</p>
  <a class="chaai-card__link" href="operations/observability/">Open the runbook →</a>
</div>

</div>

## One system, explicit responsibilities

```mermaid
flowchart TB
  U[Scientist] --> C[Chaai reasoning and tools]
  C --> P[Validated project specification]
  P --> H[HPCA execution engine]
  H --> S[Scheduler and simulation codes]
  S --> V[Validated artifacts and provenance]
  V -. evidence and results .-> C
```

!!! note "Current maturity"
    Chaai is a working research prototype deployed on HPC. HPCA is a deterministic workflow engine under active development. Neither label is a substitute for site authorization, scientific review, or validation of a specific result.

## Choose your path

| If you want to… | Start here |
| --- | --- |
| Understand the complete system | [System overview](getting-started/overview.md) |
| Walk through execution safely | [First workflow](getting-started/first-workflow.md) |
| Understand trust boundaries | [Safety model](getting-started/safety.md) |
| Integrate a scientific backend | [Tools and backends](chaai/tools-and-backends.md) |
| Understand recovery and restart | [HPCA state and recovery](hpca/state-and-recovery.md) |
| Inspect traceability guarantees | [HPCA provenance](hpca/provenance.md) |
| Diagnose a stuck or failed run | [Troubleshooting](operations/troubleshooting.md) |
| Understand generated analysis data | [Analysis output reference](reference/analysis-outputs.md) |

<div class="chaai-contact">
  <div>
    <h2>Questions or documentation feedback?</h2>
    <p>Report unclear guidance, request information, or suggest a scientific workflow improvement.</p>
  </div>
  <a class="chaai-contact__button" href="mailto:selvaus10@gmail.com?subject=Chaai%20Labs%20documentation%20feedback">Email Selva</a>
</div>
