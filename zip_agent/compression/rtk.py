from __future__ import annotations

import re
from typing import List, Set

from zip_agent.core.schemas import PolicyOutput

FILLER_RE = re.compile(r"\b(please|kindly|thanks|thank you|부탁드립니다|제발|감사합니다)\b", re.IGNORECASE)


def apply_rtk(prompt: str) -> PolicyOutput:
    kept: List[str] = []
    seen_lines: Set[str] = set()
    in_code = False
    notes: List[str] = []
    for line in prompt.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            kept.append(line)
            continue
        canonical = _canonical(stripped)
        if in_code or canonical == "":
            kept.append(line)
            continue
        if canonical in seen_lines:
            notes.append(f"removed duplicate line: {stripped[:48]}")
            continue
        seen_lines.add(canonical)
        kept.append(FILLER_RE.sub("", line).strip())
    compact = _collapse_stack_noise("\n".join(kept))
    return PolicyOutput(policy="rtk", prompt=compact.strip(), notes=tuple(notes))


def _canonical(line: str) -> str:
    return re.sub(r"\s+", " ", line.lower())


def _collapse_stack_noise(text: str) -> str:
    lines = text.splitlines()
    compact: List[str] = []
    repeated_trace = 0
    for line in lines:
        if line.strip().startswith("at ") or "Traceback" in line:
            repeated_trace += 1
            if repeated_trace > 3:
                continue
        compact.append(line)
    return "\n".join(compact)
