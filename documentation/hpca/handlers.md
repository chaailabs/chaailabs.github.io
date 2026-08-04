# Handler reference

This page documents each HPCA handler family. Enabled handlers and dependencies vary with the project category and validated specification.

## Common handler contract

```mermaid
flowchart TB
  A[Check dependencies] --> B{Inputs ready?}
  B -->|no| W[Remain pending]
  B -->|yes| C{Complete and fresh?}
  C -->|yes| K[Reuse result]
  C -->|no| D[Prepare inputs]
  D --> E[Execute locally or submit job]
  E --> F[Reconcile runtime state]
  F --> G{Output gate passes?}
  G -->|yes| H[Record artifacts and COMPLETE]
  G -->|retryable| D
  G -->|terminal| I[Record failure context]
```

This separation between a handler and a handler run follows a common orchestration pattern: states belong to a particular execution, while the definition remains reusable. Comparable systems also expose retries, cached results, state histories, and persisted outputs; see [Prefect states](https://docs.prefect.io/v3/concepts/states) and [result persistence](https://docs.prefect.io/v3/advanced/results).

## h00 — Materials design

```mermaid
flowchart TB
  S[Project specification] --> C{Material category}
  C -->|crystal| X[Build or load crystal]
  C -->|polymer| P[Build repeat units and chain]
  C -->|liquid| L[Resolve molecules and pack cell]
  X --> V[Validate composition and geometry]
  P --> V
  L --> V
  V --> O[Write structures and metadata]
```

**Gate:** required species, composition, periodic cell, and usable geometry are present. **Outputs:** designed structures and downstream-ready structural inputs.

## h01 — DFT

```mermaid
flowchart TB
  I[Designed structure] --> R[Optional AIMD pre-relaxation]
  R --> V[Variable-cell relaxation]
  V --> O[Ionic optimization]
  O --> B[Bader]
  O --> S[Static]
  O --> D[DOS SCF]
  D --> N[DOS non-SCF]
  O --> E[Electrochemical static]
  B --> G[Convergence and artifact gates]
  S --> G
  N --> G
  E --> G
```

Each enabled subtask must produce its expected converged artifacts. Subtasks are independently tracked so valid work is not repeated unnecessarily.

## h02 — Ab initio molecular dynamics

```mermaid
flowchart TB
  O[Optimized structure] --> T[Expand temperature matrix]
  T --> J[Generate per-temperature inputs]
  J --> S[Submit scheduler jobs]
  S --> R[Reconcile each job]
  R --> V{Trajectory complete?}
  V -->|yes| A[Register trajectories]
  V -->|no| F[Retry or record failure]
```

**Gate:** readable trajectories with adequate sampling coverage. Temperature jobs form a parallel execution set.

## h03 — Migration barriers with NEB

```mermaid
flowchart TB
  O[Optimized structure] --> P[Define migration path]
  P --> I[Generate intermediate images]
  I --> J[Run constrained NEB]
  J --> C{Images converged?}
  C -->|yes| E[Extract profile and barrier]
  C -->|no| R[Refine or report failure]
```

The forward barrier is \(E_m=\max_i E_i-E_0\). Acceptance also requires sensible image ordering and convergence.

## h04 — Machine-learned interatomic potential

```mermaid
flowchart TB
  A[AIMD configurations] --> D[Assemble and split dataset]
  D --> T[Train enabled backend]
  T --> V[Evaluate energies forces and stress]
  V --> G{Acceptance criteria pass?}
  G -->|yes| M[Register model and metadata]
  G -->|no| R[Retune or request data]
```

Validation must be independent of training data, and the model remains bounded by its declared chemical and thermodynamic domain.

## h05 — Classical MD and MLMD

```mermaid
flowchart TB
  C1[Designed molecular system] --> C2[Resolve classical force field]
  C2 --> C3[NPT equilibration]
  C3 --> C4[NVT production]
  M1[Accepted MLIP] --> M2[NPT equilibration]
  M2 --> M3[NVT production]
  C4 --> G[Trajectory integrity gate]
  M3 --> G
  G --> A[Analysis-ready unwrapped trajectories]
```

Classical MD and MLMD remain distinct sources so downstream comparisons do not silently treat different physical models as equivalent.

## h06 — Analysis

This handler fans out across data sources, temperatures, and observables. See [Analysis and mathematics](analysis-and-mathematics.md).

## h07 — Electronic analysis

```mermaid
flowchart TB
  D[DFT outputs] --> B[Parse Bader charges]
  D --> O[Parse total and projected DOS]
  B --> Q[Compute charge transfer]
  O --> G[Estimate band edges and gap]
  Q --> V[Validate atom and species mapping]
  G --> V
  V --> A[Tables and figures]
```

Charge arrays must map to expected atoms. Energy references and DOS thresholds must accompany any extracted gap.

## h08 — Electrochemistry

```mermaid
flowchart TB
  E[Consistent DFT energies] --> F[Formation energies]
  F --> H[Convex-hull stability]
  F --> O[Composition-dependent voltage]
  H --> W[Stability window]
  O --> R[OCV profile]
  W --> R
```

For transfer of \(n\) electrons, \(V=-\Delta G/(nF)\). If zero-temperature electronic energies approximate \(\Delta G\), that approximation must be stated.

## h09 — Continuum models

```mermaid
flowchart TB
  A[Atomistic transport outputs] --> S[Select model]
  S --> N[Nernst-Planck]
  S --> F[Fickian profile]
  S --> V[VTF conductivity]
  S --> K[KJMA transformation]
  S --> G[Growth or Vegard stress]
  N --> C[Check units and boundaries]
  F --> C
  V --> C
  K --> C
  G --> C
  C --> O[Curves parameters assumptions]
```

Continuum results inherit the uncertainty and domain limits of their atomistic inputs. Boundary conditions, units, parameter sources, and approximations are mandatory provenance.

## h10 — Plotting

```mermaid
flowchart TB
  D[Analysis CSV and JSON] --> S[Schema and unit checks]
  S --> F[Generate consistent figures]
  F --> P[PNG artifact]
  F --> H[Interactive HTML]
  P --> M[Figure manifest]
  H --> M
```

Figures remain linked to source data, axis units, transformation choices, and generation context.

## h11 — Manuscript

```mermaid
flowchart TB
  A[Validated analyses] --> F[Resolve figures and tables]
  F --> N[Generate technical narrative]
  N --> C[Attach methods and provenance]
  C --> R[Human scientific review]
  R --> D[Draft manuscript]
```

Generated prose is a draft. Claims must be traceable to validated artifacts and reviewed by a domain expert.

## h12 — Chaai adaptation

```mermaid
flowchart TB
  E[Approved examples] --> S[Sanitize and structure]
  S --> Q[Quality and leakage review]
  Q --> T[Create training records]
  T --> J[Submit adaptation pipeline]
  J --> V[Evaluate adapted model]
```

This handler is independent of the simulation chain. Only reviewed, non-sensitive examples should enter training data.

## h13 — Active learning

```mermaid
flowchart TB
  M[Current MLIP] --> X[Explore configurations]
  X --> U[Estimate uncertainty]
  U --> S[Select informative structures]
  S --> Q[Reference labeling]
  Q --> D[Extend versioned dataset]
  D --> T[Retrain and revalidate]
  T --> M
```

A candidate model replaces the current model only after fixed validation tests and coverage tests for the newly sampled region pass.
