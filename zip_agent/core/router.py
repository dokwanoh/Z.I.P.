from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from zip_agent.core.schemas import BenchmarkTask

SAFE_TYPES = {"design", "verification", "documentation", "explanation", "unknown"}


@dataclass(frozen=True)
class RouteDecision:
    task_type: str
    policies: Sequence[str]
    aggressiveness: str
    notes: Sequence[str]


def classify_task(prompt: str, declared_type: str = "unknown") -> str:
    lowered = prompt.lower()
    if declared_type != "unknown":
        return declared_type
    if "traceback" in lowered or "error" in lowered or "버그" in prompt:
        return "debugging"
    if "readme" in lowered or "문서" in prompt:
        return "documentation"
    if "design" in lowered or "ux" in lowered or "설계" in prompt:
        return "design"
    if "테스트" in prompt or "verify" in lowered:
        return "verification"
    if "한국어" in prompt or "영어로" in prompt:
        return "korean_translation_heavy"
    if "diff" in lowered or "patch" in lowered or "수정" in prompt:
        return "repo_edit"
    return "unknown"


def select_route(task: BenchmarkTask) -> RouteDecision:
    task_type = classify_task(task.input_prompt, task.task_type)
    if task.risk_level == "high" or task_type in SAFE_TYPES:
        return RouteDecision(
            task_type=task_type,
            policies=("linguaroom", "headroom", "rtk"),
            aggressiveness="conservative",
            notes=("caveman disabled for risk-sensitive workload",),
        )
    if task_type == "korean_translation_heavy":
        return RouteDecision(
            task_type=task_type,
            policies=("linguaroom", "rtk", "headroom"),
            aggressiveness="moderate",
            notes=("Korean intent normalization prioritized",),
        )
    return RouteDecision(
        task_type=task_type,
        policies=("rtk", "headroom", "caveman"),
        aggressiveness="moderate",
        notes=("adaptive policy mix selected",),
    )
