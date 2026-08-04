# Security

Production scientific agents require defense in depth:

- per-user authentication and state isolation;
- least-privilege, short-lived credentials;
- allowlisted commands, paths and scheduler operations;
- isolated execution rather than `shell=True` filtering;
- human approval for destructive, costly or external actions;
- secret and sensitive-data scanning before indexing or training;
- immutable audit records and incident response procedures;
- dependency pinning, vulnerability review and signed releases.

Report vulnerabilities using the private channel in the repository security policy.

