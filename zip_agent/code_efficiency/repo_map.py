from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


def build_repo_map(paths: Iterable[Path]) -> str:
    rows: List[str] = []
    for path in sorted(paths):
        if path.is_file():
            rows.append(str(path))
    return "\n".join(rows)
