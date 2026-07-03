from __future__ import annotations

from zip_agent.core.schemas import BenchmarkTask, PolicyOutput, QualityResult
from zip_agent.quality_guard.verifier import verify_policy_output


def run_fablize_gate(task: BenchmarkTask, output: PolicyOutput) -> QualityResult:
    return verify_policy_output(task, output)
