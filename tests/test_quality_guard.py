from pathlib import Path
from typing import Sequence

from zip_agent.compression.caveman import apply_caveman
from zip_agent.core.schemas import BenchmarkTask, PolicyOutput
from zip_agent.core.pipeline import run_policy
from zip_agent.harness.datasets import load_jsonl_dataset
from zip_agent.quality_guard.evidence_gate import catches_early_stop_language
from zip_agent.quality_guard.regression import missing_acceptance_terms, missing_required_terms
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


def test_quality_guard_required_terms_ignore_prose_but_keep_identifiers() -> None:
    task = BenchmarkTask(
        id="identifier-terms",
        task_type="repo_edit",
        input_prompt="fix src/api/client.py fetch_user_profile timeout_ms",
        repo_context=(
            "Files: src/api/client.py, tests/test_client.py\n"
            "Acceptance: preserve fetch_user_profile and timeout_ms\n"
            "Acceptance: return patch"
        ),
        expected_behavior="contains patch preserving fetch_user_profile timeout_ms",
        quality_checks=("preserves_api_name", "no_missing_acceptance_criteria"),
        risk_level="low",
    )
    complete_prompt = "Patch src/api/client.py and tests/test_client.py; keep fetch_user_profile timeout_ms."
    incomplete_prompt = "Patch src/api/client.py; keep fetch_user_profile."

    assert missing_required_terms(task, complete_prompt) == ()
    assert missing_acceptance_terms(task, complete_prompt) == ()
    assert missing_required_terms(task, incomplete_prompt) == ("timeout_ms", "tests/test_client.py")
    assert missing_acceptance_terms(task, incomplete_prompt) == ("timeout_ms",)


def test_quality_guard_required_terms_ignore_backticked_prose_labels_but_keep_identifiers() -> None:
    task = BenchmarkTask(
        id="backticked-prose-labels",
        task_type="repo_edit",
        input_prompt="fix profile loader",
        repo_context=(
            "`Files`: zip_agent/services/profile.py\n"
            "`Acceptance`: `preserve` fetch_user_profile `and` `return` timeout_ms\n"
            "`Acceptance`: `contains` tests/test_profile.py"
        ),
        expected_behavior=(
            "`Acceptance` `and` `return` `preserve` `contains` `Files` "
            "fetch_user_profile timeout_ms zip_agent/services/profile.py tests/test_profile.py"
        ),
        quality_checks=("preserves_api_name", "no_missing_acceptance_criteria"),
        risk_level="low",
    )
    complete_prompt = (
        "Update fetch_user_profile in zip_agent/services/profile.py and tests/test_profile.py "
        "with timeout_ms."
    )
    incomplete_prompt = "Update fetch_user_profile in zip_agent/services/profile.py."

    assert missing_required_terms(task, complete_prompt) == ()
    assert missing_acceptance_terms(task, complete_prompt) == ()
    assert missing_required_terms(task, incomplete_prompt) == ("timeout_ms", "tests/test_profile.py")
    assert missing_acceptance_terms(task, incomplete_prompt) == ("timeout_ms", "tests/test_profile.py")


def test_caveman_high_risk_block_and_early_stop_baseline_behavior() -> None:
    task = BenchmarkTask(
        id="baseline-risk",
        task_type="repo_edit",
        input_prompt="compress auth/session.py but keep audit_log",
        repo_context="",
        expected_behavior="preserve auth/session.py audit_log",
        quality_checks=("blocks_unsafe_compression",),
        risk_level="high",
    )

    output = apply_caveman(task)
    result = verify_policy_output(task, output)

    assert output.blocked is True
    assert output.prompt == task.input_prompt
    assert output.notes == ("blocked by risk gate",)
    assert result.passed is False
    assert result.score == 0.0
    assert result.notes == ("blocked by risk gate",)
    assert catches_early_stop_language("not tested") is True


def test_prompt_injection_fixture_blocked() -> None:
    task = _fixture("benchmarks/tasks/security_injection_tasks.jsonl", "security-injection-001")

    result = verify_policy_output(task, run_policy(task, "zip-auto"))

    assert result.passed is False
    assert any("prompt injection" in note for note in result.notes)
    assert _has_rollback_note(result.notes)


def test_tool_poisoning_fixture_blocked() -> None:
    task = _fixture("benchmarks/tasks/tool_poisoning_tasks.jsonl", "tool-poisoning-001")

    result = verify_policy_output(task, run_policy(task, "zip-auto"))

    assert result.passed is False
    assert any("tool poisoning" in note for note in result.notes)
    assert _has_rollback_note(result.notes)


def _fixture(path: str, task_id: str) -> BenchmarkTask:
    tasks = load_jsonl_dataset(Path(path))
    for task in tasks:
        if task.id == task_id:
            return task
    raise AssertionError(f"missing fixture {task_id}")


def _has_rollback_note(notes: Sequence[str]) -> bool:
    return any("rollback" in note.lower() and "original prompt" in note.lower() for note in notes)
