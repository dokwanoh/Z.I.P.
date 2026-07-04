# zip-verify

Run the quality guard against a compressed prompt or benchmark report.

Run:

```bash
python3 -m zip_agent.cli verify --help
```

Check:

- evidence command exists
- acceptance criteria preserved
- early-stop language absent
- risky compression rolled back
- dry-run limitations stated

Mirror parity:

- Canonical command: `zip-verify`
- Repo-local: `commands/zip-verify.md`
- Claude slash spec: `claude/commands/zip-verify.md`
- Hermes command spec: `hermes/commands/zip-verify.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
