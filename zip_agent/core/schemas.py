from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Mapping, Sequence


@dataclass(frozen=True)
class ProviderCapabilities:
    """Provider feature metadata.

    Defaults document the conservative dry-run/unknown-provider posture:
    no prompt caching, no structured output transport, no server-side state,
    and string fields set to "none" rather than provider-specific values.
    """

    supports_prompt_caching: bool = False
    prompt_cache_mode: str = "none"
    supports_structured_output: bool = False
    structured_output_transport: str = "none"
    supports_server_side_state: bool = False
    state_handle_name: str = "none"

    def as_json_fields(self) -> Mapping[str, bool | str]:
        return {
            "supports_prompt_caching": self.supports_prompt_caching,
            "prompt_cache_mode": self.prompt_cache_mode,
            "supports_structured_output": self.supports_structured_output,
            "structured_output_transport": self.structured_output_transport,
            "supports_server_side_state": self.supports_server_side_state,
            "state_handle_name": self.state_handle_name,
        }

    def as_note(self) -> str:
        fields = self.as_json_fields()
        return "; ".join(f"{key}={value}" for key, value in fields.items())

    def cache_status(self) -> str:
        if self.supports_prompt_caching:
            return f"supported:{self.prompt_cache_mode}"
        return "unsupported"


@dataclass(frozen=True)
class BenchmarkTask:
    id: str
    task_type: str
    input_prompt: str
    repo_context: str
    expected_behavior: str
    quality_checks: Sequence[str]
    risk_level: str

    @classmethod
    def from_mapping(cls, row: Mapping[str, object]) -> "BenchmarkTask":
        checks = row.get("quality_checks", [])
        if not isinstance(checks, list) or not all(isinstance(item, str) for item in checks):
            raise TypeError("quality_checks must be a list of strings")
        return cls(
            id=_required_str(row, "id"),
            task_type=_required_str(row, "task_type"),
            input_prompt=_required_str(row, "input_prompt"),
            repo_context=_required_str(row, "repo_context"),
            expected_behavior=_required_str(row, "expected_behavior"),
            quality_checks=tuple(checks),
            risk_level=_required_str(row, "risk_level"),
        )


@dataclass(frozen=True)
class PolicyOutput:
    policy: str
    prompt: str
    notes: Sequence[str] = field(default_factory=tuple)
    blocked: bool = False


@dataclass(frozen=True)
class QualityResult:
    score: float
    passed: bool
    notes: Sequence[str]


@dataclass(frozen=True)
class BenchmarkResult:
    task_id: str
    task_type: str
    policy: str
    input_tokens_before: int
    input_tokens_after: int
    output_tokens: int
    estimated_cost_before: float
    estimated_cost_after: float
    saving_ratio: float
    quality_score: float
    quality_pass: bool
    latency_ms: int
    notes: str
    provider: str = "unknown"
    provider_capabilities: ProviderCapabilities = field(default_factory=ProviderCapabilities)
    repeat_count: int = 1
    cache_status: str = "unsupported"
    latency_variance_ms: float = 0.0
    latency_stdev_ms: float = 0.0
    judge_provenance: str = "fablize-deterministic"
    threshold_summary: str = "quality_score=0.000; pass_threshold>0.820; status=fail"

    def as_json_row(self) -> Mapping[str, object]:
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "policy": self.policy,
            "input_tokens_before": self.input_tokens_before,
            "input_tokens_after": self.input_tokens_after,
            "output_tokens": self.output_tokens,
            "estimated_cost_before": self.estimated_cost_before,
            "estimated_cost_after": self.estimated_cost_after,
            "saving_ratio": self.saving_ratio,
            "quality_score": self.quality_score,
            "quality_pass": self.quality_pass,
            "latency_ms": self.latency_ms,
            "notes": self.notes,
            "provider": self.provider,
            **self.provider_capabilities.as_json_fields(),
            "repeat_count": self.repeat_count,
            "cache_status": self.cache_status,
            "latency_variance_ms": self.latency_variance_ms,
            "latency_stdev_ms": self.latency_stdev_ms,
            "judge_provenance": self.judge_provenance,
            "threshold_summary": self.threshold_summary,
        }


@dataclass(frozen=True)
class BenchmarkSummary:
    results: Sequence[BenchmarkResult]

    @property
    def best_results(self) -> Sequence[BenchmarkResult]:
        best: dict[str, BenchmarkResult] = {}
        for result in self.results:
            current = best.get(result.task_id)
            if current is None or _rank(result) > _rank(current):
                best[result.task_id] = result
        return tuple(best.values())


def _rank(result: BenchmarkResult) -> tuple[bool, float, float]:
    return (result.quality_pass, result.quality_score, result.saving_ratio)


def _required_str(row: Mapping[str, object], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or value == "":
        raise TypeError(f"{key} must be a non-empty string")
    return value


def average(values: Iterable[float]) -> float:
    items = list(values)
    if not items:
        return 0.0
    return sum(items) / len(items)
