from zip_agent.core.schemas import BenchmarkTask, PolicyOutput
from zip_agent.quality_guard.evidence_gate import catches_early_stop_language
from zip_agent.quality_guard.verifier import verify_policy_output


def test_quality_guard_catches_missing_acceptance_criteria() -> None:
    task = BenchmarkTask(
        id="criteria",
        task_type="repo_edit",
        input_prompt="fix function",
        repo_context="Acceptance: preserve timeout_ms",
        expected_behavior="preserve timeout_ms",
        quality_checks=("no_missing_acceptance_criteria",),
        risk_level="low",
    )
    result = verify_policy_output(task, PolicyOutput(policy="rtk", prompt="fix function"))

    assert result.passed is False
    assert "failed no_missing_acceptance_criteria" in result.notes


def test_early_stop_guard_catches_completion_language() -> None:
    assert catches_early_stop_language("I will test later") is True
