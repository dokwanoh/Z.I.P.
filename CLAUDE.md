# Claude Code Usage

Use `claude/commands/zip-save.md`, `zip-benchmark.md`, and `zip-verify.md` as slash-command specs.

Run:

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

Treat dry-run reports as prompt-token evidence, not live model-quality proof.
