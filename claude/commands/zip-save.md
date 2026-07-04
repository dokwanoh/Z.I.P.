# /zip-save

Purpose: compress the current request and relevant repo context using Z.I.P.

Run:

```bash
python3 -m zip_agent.cli save --help
```

Behavior:

1. Estimate original token count.
2. Classify task and risk.
3. Route to `linguaroom`, `headroom`, `rtk`, or guarded `caveman`.
4. Show before/after token estimates.
5. Explain what was removed and what was preserved.
6. Ask confirmation only when risk is medium or high.

Mirror parity:

- Canonical command: `zip-save`
- Repo-local: `commands/zip-save.md`
- Claude slash spec: `claude/commands/zip-save.md`
- Hermes command spec: `hermes/commands/zip-save.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
