from __future__ import annotations

from typing import List


def prune_context(context: str, max_lines: int = 20) -> str:
    lines: List[str] = []
    for line in context.splitlines():
        if len(lines) >= max_lines:
            break
        if line.strip():
            lines.append(line)
    return "\n".join(lines)
