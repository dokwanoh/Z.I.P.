# zip-save

Compress the current coding-agent prompt with Z.I.P.

Run:

```bash
python3 -m zip_agent.cli save --help
```

Steps:

1. Estimate original prompt tokens.
2. Classify workload and risk.
3. Apply safe policy candidates.
4. Show before/after token estimate.
5. List removed material and preserved identifiers.
6. Ask confirmation only for medium/high compression risk.

Mirror parity:

- Canonical command: `zip-save`
- Repo-local: `commands/zip-save.md`
- Claude slash spec: `claude/commands/zip-save.md`
- Hermes command spec: `hermes/commands/zip-save.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
