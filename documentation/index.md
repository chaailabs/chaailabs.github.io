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

<a class="chaai-card" href="chaai/">
  <span class="chaai-card__number">01</span>
  <h3>Chaai</h3>
  <p>Conversational scientific reasoning connected to schedulers, files, structures, simulation codes, and analysis tools.</p>
  <span class="chaai-card__link">Explore the agent →</span>
</a>

<a class="chaai-card" href="hpca/">
  <span class="chaai-card__number">02</span>
  <h3>HPCA engine</h3>
  <p>Deterministic stage contracts, durable state, scheduler reconciliation, validation gates, and provenance.</p>
  <span class="chaai-card__link">Explore the engine →</span>
</a>

<a class="chaai-card" href="workflows/battery-materials/">
  <span class="chaai-card__number">03</span>
  <h3>Scientific workflows</h3>
  <p>Composable workflows for battery materials and machine-learned interatomic-potential lifecycles.</p>
  <span class="chaai-card__link">View workflows →</span>
</a>

</div>

## One system, explicit responsibilities

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

## Choose your path

| If you want to… | Start here |
| --- | --- |
| Understand the complete system | [System overview](getting-started/overview.md) |
| Walk through execution safely | [First workflow](getting-started/first-workflow.md) |
| Understand trust boundaries | [Safety model](getting-started/safety.md) |
| Integrate a scientific backend | [Tools and backends](chaai/tools-and-backends.md) |
| Understand recovery and restart | [HPCA state and recovery](hpca/state-and-recovery.md) |
| Inspect traceability guarantees | [HPCA provenance](hpca/provenance.md) |
