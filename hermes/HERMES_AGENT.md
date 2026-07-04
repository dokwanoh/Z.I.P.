# Hermes Z.I.P. Agent

Hermes should use the Z.I.P. policy router for prompt-saving decisions.

Rules:

- Prefer structured JSON input/output for harness operations.
- Preserve Korean engineering intent, file paths, identifiers, API names, error messages, and acceptance criteria.
- Emit compact patch-first outputs for coding tasks.
- Run verification before completion.
- Produce evidence logs with command, dataset, policy, token counts, quality score, and limitations.

Adapter point: if Hermes command syntax differs, wrap the markdown command specs in the local Hermes command loader.

Command surface parity:

- `commands/zip-save.md` mirrors `claude/commands/zip-save.md` and `hermes/commands/zip-save.md`.
- `commands/zip-benchmark.md` mirrors `claude/commands/zip-benchmark.md` and `hermes/commands/zip-benchmark.md`.
- `commands/zip-verify.md` mirrors `claude/commands/zip-verify.md` and `hermes/commands/zip-verify.md`.
- `skills/zip-token-saver/SKILL.md` lists the same command surfaces for package discovery.
