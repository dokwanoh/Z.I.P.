from __future__ import annotations

from typing import Sequence


def missing_terms(expected: str, actual: str) -> Sequence[str]:
    required = [item.strip(".,:;") for item in expected.split() if _important(item)]
    actual_lower = actual.lower()
    return tuple(item for item in required if item.lower() not in actual_lower)


def _important(item: str) -> bool:
    return item.startswith("`") or "_" in item or "/" in item or item[:1].isupper()
