# Benchmark Template

Command:

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

Report claims must include baseline tokens, compressed tokens, cost estimate, latency, quality score, regression threshold, and dry-run/model-backed status.
