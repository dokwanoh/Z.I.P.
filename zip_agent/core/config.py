from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class BenchmarkConfig:
    dataset: Path
    policies: Sequence[str]
    report: Path
    dry_run: bool = True
