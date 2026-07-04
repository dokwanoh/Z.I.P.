# Evaluation

The primary reproducible command is:

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --repeats 3 --report reports/latest.md
```

Every task row includes `id`, `task_type`, `input_prompt`, `repo_context`, `expected_behavior`, `quality_checks`, and `risk_level`.

Every result row includes baseline tokens, compressed tokens, output-token estimate, estimated costs, saving ratio, quality score, quality pass/fail, latency, repeat count, cache status, latency variance/stdev, judge provenance, threshold summary, and notes.

The markdown report remains the human-facing surface. Its evidence summary records the repeat count used for the run, provider cache status, latency variance and standard deviation, deterministic judge provenance, and whether each row cleared the quality threshold.

Current corpus has 22 tasks and 132 policy rows. Default mode is dry-run. It measures prompt-token deltas and deterministic quality checks, not live model completion quality.

KV-cache compression is a separate research track and is excluded from core benchmark claims. Z.I.P. reports should not count KV-cache behavior as product savings unless a future serving-stack benchmark names the dataset, model, cache method, and quality threshold.
