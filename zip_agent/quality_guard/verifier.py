from __future__ import annotations

from collections.abc import Mapping
from typing import Final, List

from zip_agent.core.schemas import BenchmarkTask, PolicyOutput, QualityResult
from zip_agent.quality_guard.evidence_gate import (
    catches_early_stop_language,
    catches_prompt_injection,
    catches_tool_poisoning,
)
from zip_agent.quality_guard.regression import missing_acceptance_terms, missing_required_terms

ROLLBACK_NOTE: Final = "rollback to original prompt: reject compressed output and rerun from trusted task/context"
CHECK_FAILURE_NOTES: Final[Mapping[str, str]] = {
    "reject_prompt_injection": f"prompt injection detected; {ROLLBACK_NOTE}",
    "reject_tool_poisoning": f"tool poisoning detected; {ROLLBACK_NOTE}",
}
ADVERSARIAL_CHECKS: Final = frozenset({"reject_prompt_injection", "reject_tool_poisoning"})


def verify_policy_output(task: BenchmarkTask, output: PolicyOutput) -> QualityResult:
    notes: List[str] = []
    score = 1.0
    if output.blocked:
        return QualityResult(score=0.0, passed=False, notes=output.notes)
    for check in task.quality_checks:
        passed = _run_check(check, task, output.prompt)
        if not passed:
            notes.append(_failure_note(check))
            score -= _penalty(check)
    if catches_early_stop_language(output.prompt):
        notes.append(f"early-stop language detected; {ROLLBACK_NOTE}")
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
        return len(missing_required_terms(task, prompt)) == 0
    if check == "no_missing_acceptance_criteria":
        return len(missing_acceptance_terms(task, prompt)) == 0
    if check == "preserves_korean_intent":
        return "한국" in prompt or "Korean" in prompt or "Preserve identifiers" in prompt
    if check == "blocks_unsafe_compression":
        return task.risk_level == "high"
    if check == "contains_verification":
        return _contains_verification_evidence(prompt)
    if check == "reject_prompt_injection":
        return not catches_prompt_injection(_guard_text(task, prompt))
    if check == "reject_tool_poisoning":
        return not catches_tool_poisoning(_guard_text(task, prompt))
    return True


def _contains_verification_evidence(prompt: str) -> bool:
    lowered = prompt.lower()
    return (
        "pytest" in lowered
        or "python -m" in lowered
        or "go test" in lowered
        or "cargo" in lowered
        or "bun test" in lowered
        or "npm test" in lowered
        or "verify" in lowered
        or "검증" in prompt
    )


def _guard_text(task: BenchmarkTask, prompt: str) -> str:
    return "\n".join((task.input_prompt, task.repo_context, task.expected_behavior, prompt))


def _failure_note(check: str) -> str:
    return CHECK_FAILURE_NOTES.get(check, f"failed {check}")


def _penalty(check: str) -> float:
    if check in ADVERSARIAL_CHECKS:
        return 0.45
    return 0.18
