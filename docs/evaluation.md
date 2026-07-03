# Evaluation

The primary reproducible command is:

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

Every task row includes `id`, `task_type`, `input_prompt`, `repo_context`, `expected_behavior`, `quality_checks`, and `risk_level`.

Every result row includes baseline tokens, compressed tokens, output-token estimate, estimated costs, saving ratio, quality score, quality pass/fail, latency, and notes.

Current default mode is dry-run. It measures prompt-token deltas and deterministic quality checks, not live model completion quality.
