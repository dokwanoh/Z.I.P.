from __future__ import annotations

import re
from typing import List

from zip_agent.core.schemas import BenchmarkTask, PolicyOutput

BLOCKED_TYPES = {"design", "security", "compliance", "legal", "unknown"}


def apply_caveman(task: BenchmarkTask) -> PolicyOutput:
    if task.risk_level == "high" or task.task_type in BLOCKED_TYPES:
        return PolicyOutput(
            policy="caveman",
            prompt=task.input_prompt,
            notes=("blocked by risk gate",),
            blocked=True,
        )
    words = re.findall(r"`[^`]+`|\S+", task.input_prompt)
    terse: List[str] = []
    for word in words:
        if _keep(word):
            terse.append(_shorten(word))
    return PolicyOutput(
        policy="caveman",
        prompt=" ".join(terse[:120]),
        notes=("terse compression applied within safe-risk limit",),
    )


def _keep(word: str) -> bool:
    lower = word.lower().strip(".,")
    return (
        word.startswith("`")
        or "/" in word
        or "_" in word
        or lower not in {"please", "detail", "explain", "kindly", "the", "a", "an"}
    )


def _shorten(word: str) -> str:
    return word.replace("implement", "impl").replace("수정해주세요", "fix")
