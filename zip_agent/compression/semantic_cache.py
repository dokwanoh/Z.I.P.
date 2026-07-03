from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class SemanticCache:
    entries: Dict[str, str] = field(default_factory=dict)

    def get(self, prompt: str) -> str | None:
        return self.entries.get(_key(prompt))

    def put(self, prompt: str, compact_prompt: str) -> None:
        self.entries[_key(prompt)] = compact_prompt


def _key(prompt: str) -> str:
    return " ".join(prompt.lower().split())
