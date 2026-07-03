from __future__ import annotations

from zip_agent.core.schemas import PolicyOutput


def apply_minimal_diff(prompt: str) -> PolicyOutput:
    addition = "\nRespond with the smallest unified diff or patch-first answer; omit unchanged code."
    return PolicyOutput(policy="minimal-diff", prompt=f"{prompt.strip()}{addition}", notes=("patch-first prompt added",))
