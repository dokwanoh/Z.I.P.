from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Sequence

from zip_agent.core.schemas import BenchmarkResult, BenchmarkSummary, average
from zip_agent.harness.scoring import zip_score


def write_markdown_report(path: Path, results: Sequence[BenchmarkResult], dry_run: bool) -> None:
    summary = BenchmarkSummary(results=results)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Z.I.P. Benchmark Report",
        "",
        f"Mode: {'dry-run deterministic fixture mode' if dry_run else 'model-backed mode'}",
        "",
        "Dry-run results measure prompt-token changes and deterministic guard behavior only.",
        "",
        "## Summary",
        "",
        f"- Rows: {len(results)}",
        f"- Average input-token saving: {average(r.saving_ratio for r in results):.1%}",
        f"- Quality pass rate: {average(1.0 if r.quality_pass else 0.0 for r in results):.1%}",
        "",
        "## Results",
        "",
        "| task | type | policy | input before | input after | saving | quality | Z.I.P. score | notes |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for result in results:
        lines.append(
            f"| {result.task_id} | {result.task_type} | {result.policy} | {result.input_tokens_before} | "
            f"{result.input_tokens_after} | {result.saving_ratio:.1%} | "
            f"{result.quality_score:.2f} | {zip_score(result):.3f} | {result.notes} |"
        )
    lines.extend(["", "## Best Policy Per Task", ""])
    for result in summary.best_results:
        lines.append(f"- {result.task_id}: {result.policy} ({result.saving_ratio:.1%} saving, quality {result.quality_score:.2f})")
    lines.extend(["", "## Best Policy By Workload", ""])
    for task_type, result in _best_by_type(results).items():
        lines.append(f"- {task_type}: {result.policy} ({result.saving_ratio:.1%} saving)")
    lines.extend(
        [
            "",
            "## Honest Limitations",
            "",
            "- This report is dry-run unless model API integration is explicitly enabled.",
            "- Output tokens are fixture estimates, not live model completions.",
            "- Cost values are estimates from configured per-token rates.",
            "- Claims should say target or observed-in-this-workload until model-backed runs validate quality.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _best_by_type(results: Sequence[BenchmarkResult]) -> Dict[str, BenchmarkResult]:
    best: Dict[str, BenchmarkResult] = {}
    for result in results:
        task_type = result.task_type
        current = best.get(task_type)
        if current is None or result.saving_ratio > current.saving_ratio:
            best[task_type] = result
    return best
