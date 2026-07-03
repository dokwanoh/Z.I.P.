# /zip-benchmark

Run the benchmark harness and update `reports/latest.md`.

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

Summarize savings, quality pass rate, failed gates, and dry-run limitations.
