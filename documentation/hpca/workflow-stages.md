# Workflow stages

| Stage | Purpose | Representative gate |
|---|---|---|
| Design | Build valid structures and compositions | geometry and composition checks |
| DFT | Relax and characterize electronic structure | convergence and artifact completeness |
| AIMD | Generate high-fidelity dynamic configurations | trajectory integrity and sampling coverage |
| MLIP | Train and evaluate interatomic potentials | held-out errors and domain acceptance |
| MD | Produce statistically useful trajectories | stability, duration and ensemble checks |
| Analysis | Calculate transport and structural observables | fit quality and uncertainty reporting |
| Reporting | Produce traceable figures and summaries | source-data and provenance links |

Stages are contracts, not merely directories: each defines inputs, outputs, completion criteria, failure modes, and recovery behavior.

