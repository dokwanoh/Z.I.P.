from zip_agent.compression.caveman import apply_caveman
from zip_agent.compression.rtk import apply_rtk
from zip_agent.core.schemas import BenchmarkTask
from zip_agent.linguaroom.adapter import apply_linguaroom


def test_rtk_deduplicates_repeated_prompt_without_removing_code_symbols() -> None:
    prompt = "Please fix fetch_user_profile\nPlease fix fetch_user_profile\n```python\nfetch_user_profile()\n```"
    output = apply_rtk(prompt)

    assert output.prompt.count("fix fetch_user_profile") == 1
    assert "fetch_user_profile()" in output.prompt


def test_linguaroom_preserves_korean_intent_and_code_identifiers() -> None:
    output = apply_linguaroom("영어로 번역해서 src/api/client.py 의 fetch_user_profile 수정해주세요")

    assert "fetch_user_profile" in output.prompt
    assert "src/api/client.py" in output.prompt


def test_caveman_policy_is_blocked_for_high_risk_tasks() -> None:
    task = BenchmarkTask(
        id="risk",
        task_type="unknown",
        input_prompt="compress auth/permissions.py but preserve audit_log",
        repo_context="",
        expected_behavior="preserve auth/permissions.py audit_log",
        quality_checks=("blocks_unsafe_compression",),
        risk_level="high",
    )
    output = apply_caveman(task)

    assert output.blocked is True
    assert output.prompt == task.input_prompt
