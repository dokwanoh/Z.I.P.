from __future__ import annotations

import statistics
import time
from typing import Final, List, Sequence

from zip_agent.core.meter import measure_prompt
from zip_agent.core.model_client import CompletionResult, ModelClient, build_model_client_from_env
from zip_agent.core.pipeline import run_policy
from zip_agent.core.schemas import BenchmarkResult, BenchmarkTask, QualityResult
from zip_agent.quality_guard.fablize_adapter import run_fablize_gate

QUALITY_PASS_THRESHOLD: Final = 0.82
JUDGE_PROVENANCE: Final = "fablize-deterministic"


def run_benchmark(
    tasks: Sequence[BenchmarkTask],
    policies: Sequence[str],
    repeats: int = 1,
    model_client: ModelClient | None = None,
) -> List[BenchmarkResult]:
    client = model_client if model_client is not None else build_model_client_from_env()
    repeat_count = max(1, repeats)
    rows: List[BenchmarkResult] = []
    for task in tasks:
        baseline_prompt = f"{task.input_prompt}\n\nContext:\n{task.repo_context}".strip()
        baseline_completion = _complete(client, baseline_prompt, task)
        baseline_reading = measure_prompt(baseline_prompt, baseline_completion.content)
        for policy in policies:
            output = run_policy(task, policy)
            quality = run_fablize_gate(task, output)
            completion, elapsed_ms = _timed_completion(client, output.prompt, task)
            latencies_ms = [elapsed_ms]
            for _ in range(1, repeat_count):
                _, repeat_elapsed_ms = _timed_completion(client, output.prompt, task)
                latencies_ms.append(repeat_elapsed_ms)
            latency_mean_ms = int(round(statistics.fmean(latencies_ms)))
            latency_variance_ms = round(statistics.pvariance(latencies_ms), 3)
            latency_stdev_ms = round(statistics.pstdev(latencies_ms), 3)
            compressed_reading = measure_prompt(output.prompt, completion.content)
            saving = _saving_ratio(baseline_reading.input_tokens, compressed_reading.input_tokens)
            notes = "; ".join(
                tuple(output.notes)
                + tuple(quality.notes)
                + tuple(completion.notes)
                + (completion.capabilities.as_note(),)
            )
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
                    latency_ms=latency_mean_ms,
                    notes=notes,
                    provider=completion.provider,
                    provider_capabilities=completion.capabilities,
                    repeat_count=repeat_count,
                    cache_status=completion.capabilities.cache_status(),
                    latency_variance_ms=latency_variance_ms,
                    latency_stdev_ms=latency_stdev_ms,
                    judge_provenance=JUDGE_PROVENANCE,
                    threshold_summary=_threshold_summary(quality),
                )
            )
    return rows


def _timed_completion(client: ModelClient, prompt: str, task: BenchmarkTask) -> tuple[CompletionResult, int]:
    started = time.perf_counter()
    completion = _complete(client, prompt, task)
    elapsed_ms = completion.latency_ms or int((time.perf_counter() - started) * 1000)
    return completion, elapsed_ms


def _complete(client: ModelClient, prompt: str, task: BenchmarkTask) -> CompletionResult:
    return client.complete(
        prompt,
        system_prompt=(
            "Return concise code-agent output that preserves the requested behavior. "
            f"Required behavior: {task.expected_behavior}. "
            "Preserve file paths, identifiers, acceptance criteria, and verification evidence."
        ),
        max_output_tokens=_max_output_tokens(task),
    )


def _saving_ratio(before: int, after: int) -> float:
    if before == 0:
        return 0.0
    return round(max(0.0, (before - after) / before), 4)


def _max_output_tokens(task: BenchmarkTask) -> int:
    if task.risk_level == "high":
        return 800
    return 1200


def _threshold_summary(quality: QualityResult) -> str:
    status = "pass" if quality.passed else "fail"
    return (
        f"quality_score={quality.score:.3f}; "
        f"pass_threshold>{QUALITY_PASS_THRESHOLD:.3f}; status={status}"
    )
