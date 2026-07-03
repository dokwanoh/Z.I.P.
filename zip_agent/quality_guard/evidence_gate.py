from __future__ import annotations

import re

EARLY_STOP_RE = re.compile(r"\b(I would|I'll|should work|not tested|test later|나중에 테스트)\b", re.IGNORECASE)


def catches_early_stop_language(text: str) -> bool:
    return EARLY_STOP_RE.search(text) is not None
