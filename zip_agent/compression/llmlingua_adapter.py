from __future__ import annotations

from zip_agent.core.schemas import PolicyOutput


def apply_llmlingua_placeholder(prompt: str) -> PolicyOutput:
    return PolicyOutput(
        policy="llmlingua",
        prompt=prompt,
        notes=("LLMLingua-family adapter placeholder; no external dependency invoked.",),
    )
