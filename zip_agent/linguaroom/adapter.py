from __future__ import annotations

from zip_agent.core.schemas import PolicyOutput
from zip_agent.linguaroom.korean_prompt_optimizer import optimize_korean_prompt


def apply_linguaroom(prompt: str) -> PolicyOutput:
    return PolicyOutput(
        policy="linguaroom",
        prompt=optimize_korean_prompt(prompt),
        notes=("LinguaRoom integration placeholder; deterministic local optimizer used.",),
    )
