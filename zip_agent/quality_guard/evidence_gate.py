from __future__ import annotations

import re
from typing import Final

EARLY_STOP_RE: Final = re.compile(r"\b(I would|I'll|should work|not tested|test later|나중에 테스트)\b", re.IGNORECASE)
PROMPT_INJECTION_RE: Final = re.compile(
    r"\b(ignore (?:all|previous|prior|above) instructions|skip tests|declare success|"
    r"system prompt|developer message|disregard (?:all|previous|prior|above) instructions)\b",
    re.IGNORECASE,
)
TOOL_POISONING_RE: Final = re.compile(
    r"\b(untrusted tool output|pass all tests|cached snippet|do not inspect git status|"
    r"replace [^\n]+ with the cached|rm -rf)\b",
    re.IGNORECASE,
)


def catches_early_stop_language(text: str) -> bool:
    return EARLY_STOP_RE.search(text) is not None


def catches_prompt_injection(text: str) -> bool:
    return PROMPT_INJECTION_RE.search(text) is not None


def catches_tool_poisoning(text: str) -> bool:
    return TOOL_POISONING_RE.search(text) is not None
