from __future__ import annotations

import json
from pathlib import Path
from typing import List

from zip_agent.core.schemas import BenchmarkTask


def load_jsonl_dataset(path: Path) -> List[BenchmarkTask]:
    tasks: List[BenchmarkTask] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if line.strip() == "":
                continue
            raw = json.loads(line)
            if not isinstance(raw, dict):
                raise TypeError(f"line {line_number} must be a JSON object")
            tasks.append(BenchmarkTask.from_mapping(raw))
    return tasks
