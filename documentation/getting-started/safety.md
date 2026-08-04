# Safety model

Scientific agents must operate with least privilege and explicit boundaries.

- Read operations precede mutations.
- Compute runs through a scheduler, not shared login resources.
- Destructive actions require explicit authorization and resolved targets.
- Filesystem and command access are allowlisted in production deployments.
- Credentials never enter prompts, training data, logs, or repositories.
- Model output is untrusted until schema and domain validation pass.
- Every submitted job, artifact, model, and decision records provenance.
- Human review remains mandatory for scientific and release decisions.

The current Chaai shell blocklist is a prototype safeguard, not an operating-system sandbox. Production deployment requires process isolation, scoped credentials, allowlisted commands and paths, audit logs, and per-user state isolation.

