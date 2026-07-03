from __future__ import annotations

from typing import List

from zip_agent.core.schemas import PolicyOutput

IMPORTANT_PREFIXES = ("Goal:", "Task:", "Acceptance:", "Files:", "Error:", "Expected:", "Context:")


def apply_headroom(prompt: str, output_budget_tokens: int = 1200) -> PolicyOutput:
    budget = max(80, output_budget_tokens // 2)
    lines = prompt.splitlines()
    selected: List[str] = []
    notes: List[str] = [f"reserved output budget: {output_budget_tokens}"]
    for line in lines:
        if _is_important(line) or len(selected) < 8:
            selected.append(line)
        if _rough_tokens("\n".join(selected)) >= budget:
            notes.append("stopped at headroom budget")
            break
    return PolicyOutput(policy="headroom", prompt="\n".join(selected).strip(), notes=tuple(notes))


def _is_important(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith(IMPORTANT_PREFIXES) or "`" in stripped or "AC:" in stripped


def _rough_tokens(text: str) -> int:
    return max(1, len(text) // 4)
