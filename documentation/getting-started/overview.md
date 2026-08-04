# System overview

Chaai translates a scientist's goal into explicit tool calls, explanations, and proposed workflow actions. HPCA executes approved computational-materials workflows from a validated specification, records durable state, and produces traceable artifacts.

The separation is intentional:

| Layer | Responsibility |
|---|---|
| Chaai | Interaction, planning, context, tool selection, diagnosis |
| HPCA | Validation, deterministic stages, scheduling, recovery, provenance |
| Simulation codes | Physics calculations and trajectories |
| Scientist | Authorization, scientific judgment, acceptance decisions |

The model proposes; controlled tools mediate; validation gates decide whether execution may proceed.

