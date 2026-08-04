# Tools and backends

Chaai currently supports a local Qwen2.5-Coder-32B backend served through vLLM and experimental alternative adapters. The demonstrated local context configuration is 16,384 tokens; larger contexts are roadmap items unless separately validated.

The tool registry includes scheduler operations, controlled shell and file actions, Python analysis, atomic structures, VASP, LAMMPS, GROMACS, ASE, pymatgen, AtomicAI, diagnostics, plotting, indexing, and GPU monitoring.

Tool availability does not imply that every scientific workflow is validated. Each tool needs input validation, permission enforcement, deterministic error handling, tests, and a documented artifact contract.

