from __future__ import annotations

from zip_agent.core.schemas import BenchmarkResult


def zip_score(result: BenchmarkResult) -> float:
    cost_saving_score = max(0.0, min(1.0, result.saving_ratio))
    quality_score = max(0.0, min(1.0, result.quality_score))
    latency_score = 1.0 if result.latency_ms <= 100 else max(0.0, 1.0 - (result.latency_ms / 5000))
    reproducibility_score = 1.0
    safety_score = 1.0 if result.quality_pass else 0.2
    total = (
        0.40 * cost_saving_score
        + 0.30 * quality_score
        + 0.15 * latency_score
        + 0.10 * reproducibility_score
        + 0.05 * safety_score
    )
    if not result.quality_pass:
        total = min(total, 0.49)
    return round(total, 3)
