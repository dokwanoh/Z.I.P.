from __future__ import annotations

from typing import List

from zip_agent.core.schemas import BenchmarkTask, PolicyOutput, QualityResult
from zip_agent.quality_guard.evidence_gate import catches_early_stop_language


def verify_policy_output(task: BenchmarkTask, output: PolicyOutput) -> QualityResult:
    notes: List[str] = []
    score = 1.0
    if output.blocked:
        return QualityResult(score=0.0, passed=False, notes=output.notes)
    for check in task.quality_checks:
        passed = _run_check(check, task, output.prompt)
        if not passed:
            notes.append(f"failed {check}")
            score -= 0.18
    if catches_early_stop_language(output.prompt):
        notes.append("early-stop language detected")
        score -= 0.35
    if task.risk_level == "high" and output.policy == "caveman":
        notes.append("caveman blocked for high risk")
        score = 0.0
    final_score = max(0.0, round(score, 3))
    return QualityResult(score=final_score, passed=final_score > 0.82, notes=tuple(notes))


def _run_check(check: str, task: BenchmarkTask, prompt: str) -> bool:
    if check == "contains_patch":
        return "patch" in prompt.lower() or "diff" in prompt.lower() or "수정" in prompt
    if check == "preserves_api_name":
        return _contains_identifier_from(task.expected_behavior, prompt)
    if check == "no_missing_acceptance_criteria":
        return "acceptance" in prompt.lower() or "AC:" in prompt or "must" in prompt.lower() or "반드시" in prompt
    if check == "preserves_korean_intent":
        return "한국" in prompt or "Korean" in prompt or "Preserve identifiers" in prompt
    if check == "blocks_unsafe_compression":
        return task.risk_level == "high"
    if check == "contains_verification":
        return "test" in prompt.lower() or "verify" in prompt.lower() or "검증" in prompt
    return True


def _contains_identifier_from(expected: str, prompt: str) -> bool:
    for item in expected.replace(",", " ").split():
        token = item.strip("`.;:")
        if ("_" in token or "." in token or "/" in token) and token in prompt:
            return True
    return False
