# First workflow

A safe workflow begins with a bounded scientific question and an explicit decision criterion.

1. Define the material, property, fidelity, uncertainty tolerance, and compute budget.
2. Encode inputs in a versioned project specification.
3. Validate schema, structures, scheduler resources, and dependencies.
4. Review the execution plan and authorize mutating or costly actions.
5. Execute stages through the scheduler.
6. Reconcile state after failures or restarts.
7. Validate scientific outputs and preserve provenance.

```yaml
project:
  name: example-solid-electrolyte
  category: crystalline
workflow:
  stages: [design, dft, aimd, mlip, mlmd, analysis]
validation:
  require_structure_check: true
  require_model_acceptance: true
```

This illustrative specification omits site-specific resources and executable settings.

