# /zip-benchmark

Run the benchmark harness and update `reports/latest.md`.

```bash
python3 -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

Summarize savings, quality pass rate, failed gates, and dry-run limitations.

Mirror parity:

- Canonical command: `zip-benchmark`
- Repo-local: `commands/zip-benchmark.md`
- Claude slash spec: `claude/commands/zip-benchmark.md`
- Hermes command spec: `hermes/commands/zip-benchmark.md`
- Skill package: `skills/zip-token-saver/SKILL.md`
