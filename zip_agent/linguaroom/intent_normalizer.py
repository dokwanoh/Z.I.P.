from __future__ import annotations

import re
from typing import List

KOREAN_BOILERPLATE = (
    "영어로 번역해서",
    "한국어로 설명하면",
    "자세히 설명해 주세요",
    "부탁드립니다",
    "가능하면",
)


def normalize_korean_engineering_intent(prompt: str) -> str:
    text = prompt
    for phrase in KOREAN_BOILERPLATE:
        text = text.replace(phrase, "")
    lines: List[str] = []
    for raw_line in text.splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if line:
            lines.append(line)
    return "\n".join(lines)
