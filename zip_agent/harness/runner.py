from __future__ import annotations

import time
from typing import List, Sequence

from zip_agent.core.meter import measure_prompt
from zip_agent.core.pipeline import run_policy
from zip_agent.core.schemas import BenchmarkResult, BenchmarkTask
from zip_agent.quality_guard.fablize_adapter import run_fablize_gate


def run_benchmark(tasks: Sequence[BenchmarkTask], policies: Sequence[str]) -> List[BenchmarkResult]:
    rows: List[BenchmarkResult] = []
    for task in tasks:
        baseline_prompt = f"{task.input_prompt}\n\nContext:\n{task.repo_context}".strip()
        baseline_reading = measure_prompt(baseline_prompt, _fixture_output(task))
        for policy in policies:
            started = time.perf_counter()
            output = run_policy(task, policy)
            quality = run_fablize_gate(task, output)
            compressed_reading = measure_prompt(output.prompt, _fixture_output(task))
            elapsed_ms = int((time.perf_counter() - started) * 1000)
            saving = _saving_ratio(baseline_reading.input_tokens, compressed_reading.input_tokens)
            notes = "; ".join(tuple(output.notes) + tuple(quality.notes))
            rows.append(
                BenchmarkResult(
                    task_id=task.id,
                    task_type=task.task_type,
                    policy=policy,
                    input_tokens_before=baseline_reading.input_tokens,
                    input_tokens_after=compressed_reading.input_tokens,
                    output_tokens=compressed_reading.output_tokens,
                    estimated_cost_before=round(baseline_reading.estimated_cost, 6),
                    estimated_cost_after=round(compressed_reading.estimated_cost, 6),
                    saving_ratio=saving,
                    quality_score=quality.score,
                    quality_pass=quality.passed,
                    latency_ms=elapsed_ms,
                    notes=notes,
                )
            )
    return rows


def _fixture_output(task: BenchmarkTask) -> str:
    return f"dry-run output satisfies: {task.expected_behavior}"


def _saving_ratio(before: int, after: int) -> float:
    if before == 0:
        return 0.0
    return round(max(0.0, (before - after) / before), 4)
