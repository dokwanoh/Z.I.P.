# /zip-verify

Run quality guard checks before completion.

Run:

```bash
python3 -m zip_agent.cli verify --help
```

Confirm:

- command/test evidence exists
- acceptance criteria were preserved
- early-stop language is absent
- compression risk is stated
- reproducibility command is included

Mirror parity:

- Canonical command: `zip-verify`
- Repo-local: `commands/zip-verify.md`
- Claude slash spec: `claude/commands/zip-verify.md`
- Hermes command spec: `hermes/commands/zip-verify.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
