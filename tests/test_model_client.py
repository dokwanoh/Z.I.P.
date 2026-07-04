from pytest import MonkeyPatch

from zip_agent.core.model_client import (
    CompletionResult,
    DryRunModelClient,
    OpenAICompatibleClient,
    ProviderCapabilities,
    build_model_client_from_env,
)
from zip_agent.core.schemas import BenchmarkResult, BenchmarkTask
from zip_agent.harness.runner import run_benchmark


def test_model_client_defaults_to_dry_run_when_env_missing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.delenv("ZIP_MODEL_ENDPOINT", raising=False)
    monkeypatch.delenv("ZIP_MODEL_NAME", raising=False)

    client = build_model_client_from_env()

    assert isinstance(client, DryRunModelClient)


def test_dry_run_model_client_returns_fixture_completion() -> None:
    client = DryRunModelClient()
    completion = client.complete("fix fetch_user_profile", system_prompt="system", max_output_tokens=128)

    assert "dry-run output satisfies" in completion.content
    assert completion.provider == "dry-run"
    assert completion.capabilities == ProviderCapabilities()


def test_model_client_env_config_carries_provider_capabilities(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("ZIP_MODEL_ENDPOINT", "https://models.example.invalid/v1/chat/completions")
    monkeypatch.setenv("ZIP_MODEL_NAME", "zip-fixture")
    monkeypatch.setenv("ZIP_MODEL_SUPPORTS_PROMPT_CACHING", "true")
    monkeypatch.setenv("ZIP_MODEL_PROMPT_CACHE_MODE", "ephemeral")
    monkeypatch.setenv("ZIP_MODEL_SUPPORTS_STRUCTURED_OUTPUT", "1")
    monkeypatch.setenv("ZIP_MODEL_STRUCTURED_OUTPUT_TRANSPORT", "json_schema")
    monkeypatch.setenv("ZIP_MODEL_SUPPORTS_SERVER_SIDE_STATE", "yes")
    monkeypatch.setenv("ZIP_MODEL_STATE_HANDLE_NAME", "response_id")

    client = build_model_client_from_env()

    assert isinstance(client, OpenAICompatibleClient)
    assert client.config.capabilities == ProviderCapabilities(
        supports_prompt_caching=True,
        prompt_cache_mode="ephemeral",
        supports_structured_output=True,
        structured_output_transport="json_schema",
        supports_server_side_state=True,
        state_handle_name="response_id",
    )


def test_benchmark_result_json_row_preserves_existing_keys() -> None:
    result = BenchmarkResult(
        task_id="task-1",
        task_type="coding",
        policy="baseline",
        input_tokens_before=100,
        input_tokens_after=80,
        output_tokens=20,
        estimated_cost_before=0.001,
        estimated_cost_after=0.0008,
        saving_ratio=0.2,
        quality_score=0.95,
        quality_pass=True,
        latency_ms=12,
        notes="fixture completion",
    )

    existing_keys = (
        "task_id",
        "task_type",
        "policy",
        "input_tokens_before",
        "input_tokens_after",
        "output_tokens",
        "estimated_cost_before",
        "estimated_cost_after",
        "saving_ratio",
        "quality_score",
        "quality_pass",
        "latency_ms",
        "notes",
    )
    assert tuple(result.as_json_row().keys())[: len(existing_keys)] == existing_keys


def test_provider_capabilities_round_trip_through_benchmark_json_row() -> None:
    capabilities = ProviderCapabilities(
        supports_prompt_caching=True,
        prompt_cache_mode="ephemeral",
        supports_structured_output=True,
        structured_output_transport="json_schema",
        supports_server_side_state=True,
        state_handle_name="response_id",
    )
    task = BenchmarkTask(
        id="capability-task",
        task_type="coding",
        input_prompt="Refactor the fetch_user_profile helper.",
        repo_context="",
        expected_behavior="preserve behavior",
        quality_checks=(),
        risk_level="low",
    )

    class CapabilityClient:
        def complete(self, prompt: str, *, system_prompt: str, max_output_tokens: int) -> CompletionResult:
            return CompletionResult(
                content=f"{system_prompt}\n{prompt}\n{max_output_tokens}",
                latency_ms=7,
                prompt_tokens=11,
                output_tokens=5,
                provider="fixture-live",
                capabilities=capabilities,
                notes=("fixture completion",),
            )

    result = run_benchmark((task,), ("baseline",), model_client=CapabilityClient())[0]
    row = result.as_json_row()

    assert result.provider == "fixture-live"
    assert result.provider_capabilities == capabilities
    assert row["provider"] == "fixture-live"
    assert row["supports_prompt_caching"] is True
    assert row["prompt_cache_mode"] == "ephemeral"
    assert row["supports_structured_output"] is True
    assert row["structured_output_transport"] == "json_schema"
    assert row["supports_server_side_state"] is True
    assert row["state_handle_name"] == "response_id"
