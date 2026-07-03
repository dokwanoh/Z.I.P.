from __future__ import annotations

import re
from typing import List

from zip_agent.linguaroom.intent_normalizer import normalize_korean_engineering_intent

IDENTIFIER_RE = re.compile(r"`[^`]+`|[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*|[\w./-]+\.(?:py|ts|tsx|go|rs|md)")


def optimize_korean_prompt(prompt: str) -> str:
    normalized = normalize_korean_engineering_intent(prompt)
    identifiers = _collect_identifiers(prompt)
    compact = normalized.replace("반드시", "must").replace("수정해", "fix")
    if identifiers:
        compact = f"{compact}\nPreserve identifiers: {', '.join(identifiers)}"
    return compact.strip()


def _collect_identifiers(prompt: str) -> List[str]:
    identifiers: List[str] = []
    seen = set()
    for match in IDENTIFIER_RE.finditer(prompt):
        item = match.group(0).strip("`")
        if item not in seen and len(item) > 2:
            identifiers.append(item)
            seen.add(item)
    return identifiers[:12]
