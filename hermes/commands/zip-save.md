# zip-save

Portable Hermes command spec.

Input: current user request and repo context.
Output: JSON with `policy`, `input_tokens_before`, `input_tokens_after`, `risk_level`, `removed`, `preserved`, and `requires_confirmation`.

Run:

```bash
python3 -m zip_agent.cli save --help
```

Mirror parity:

- Canonical command: `zip-save`
- Repo-local: `commands/zip-save.md`
- Claude slash spec: `claude/commands/zip-save.md`
- Hermes command spec: `hermes/commands/zip-save.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
