from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
import time
from typing import Protocol, runtime_checkable
from urllib import error as urlerror
from urllib import request as urlrequest

from zip_agent.core.schemas import ProviderCapabilities
from zip_agent.core.tokenizer import estimate_tokens


@dataclass(frozen=True)
class CompletionResult:
    content: str
    latency_ms: int
    prompt_tokens: int
    output_tokens: int
    provider: str
    capabilities: ProviderCapabilities = field(default_factory=ProviderCapabilities)
    notes: tuple[str, ...] = ()


@dataclass(frozen=True)
class ModelConfig:
    endpoint_url: str
    model: str
    api_key: str | None = None
    timeout_seconds: float = 30.0
    max_output_tokens: int = 1200
    capabilities: ProviderCapabilities = field(default_factory=ProviderCapabilities)


@dataclass(frozen=True)
class ModelRequestError(Exception):
    message: str
    status_code: int | None = None

    def __str__(self) -> str:
        if self.status_code is None:
            return self.message
        return f"{self.message} (status={self.status_code})"


@runtime_checkable
class ModelClient(Protocol):
    def complete(self, prompt: str, *, system_prompt: str, max_output_tokens: int) -> CompletionResult:
        ...


@dataclass(frozen=True)
class DryRunModelClient:
    def complete(self, prompt: str, *, system_prompt: str, max_output_tokens: int) -> CompletionResult:
        content = f"dry-run output satisfies:\n{system_prompt}\n{prompt}"
        return CompletionResult(
            content=content,
            latency_ms=0,
            prompt_tokens=estimate_tokens(system_prompt + "\n" + prompt),
            output_tokens=estimate_tokens(content),
            provider="dry-run",
            capabilities=ProviderCapabilities(),
            notes=("fixture completion",),
        )


@dataclass(frozen=True)
class OpenAICompatibleClient:
    config: ModelConfig

    def complete(self, prompt: str, *, system_prompt: str, max_output_tokens: int) -> CompletionResult:
        started = time.perf_counter()
        body = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": min(max_output_tokens, self.config.max_output_tokens),
            "temperature": 0,
        }
        data = json.dumps(body).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.config.api_key is not None:
            headers["Authorization"] = f"Bearer {self.config.api_key}"
        req = urlrequest.Request(self.config.endpoint_url, data=data, headers=headers, method="POST")
        try:
            with urlrequest.urlopen(req, timeout=self.config.timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urlerror.HTTPError as exc:
            raise ModelRequestError("model request failed", status_code=exc.code) from exc
        except urlerror.URLError as exc:
            raise ModelRequestError(f"model request failed: {exc.reason}") from exc
        content = _extract_content(payload)
        return CompletionResult(
            content=content,
            latency_ms=int((time.perf_counter() - started) * 1000),
            prompt_tokens=estimate_tokens(system_prompt + "\n" + prompt),
            output_tokens=estimate_tokens(content),
            provider="openai-compatible",
            capabilities=self.config.capabilities,
            notes=("live completion",),
        )


def build_model_client_from_env() -> ModelClient:
    endpoint = os.environ.get("ZIP_MODEL_ENDPOINT")
    model = os.environ.get("ZIP_MODEL_NAME")
    if endpoint is None or model is None:
        return DryRunModelClient()
    api_key = os.environ.get("ZIP_MODEL_API_KEY")
    timeout = float(os.environ.get("ZIP_MODEL_TIMEOUT_SECONDS", "30"))
    max_output_tokens = int(os.environ.get("ZIP_MODEL_MAX_OUTPUT_TOKENS", "1200"))
    capabilities = ProviderCapabilities(
        supports_prompt_caching=_env_flag("ZIP_MODEL_SUPPORTS_PROMPT_CACHING"),
        prompt_cache_mode=os.environ.get("ZIP_MODEL_PROMPT_CACHE_MODE", "none"),
        supports_structured_output=_env_flag("ZIP_MODEL_SUPPORTS_STRUCTURED_OUTPUT"),
        structured_output_transport=os.environ.get("ZIP_MODEL_STRUCTURED_OUTPUT_TRANSPORT", "none"),
        supports_server_side_state=_env_flag("ZIP_MODEL_SUPPORTS_SERVER_SIDE_STATE"),
        state_handle_name=os.environ.get("ZIP_MODEL_STATE_HANDLE_NAME", "none"),
    )
    return OpenAICompatibleClient(
        config=ModelConfig(
            endpoint_url=endpoint,
            model=model,
            api_key=api_key,
            timeout_seconds=timeout,
            max_output_tokens=max_output_tokens,
            capabilities=capabilities,
        ),
    )


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _extract_content(payload: object) -> str:
    if not isinstance(payload, dict):
        raise ModelRequestError("invalid model payload")
    choices = payload.get("choices")
    if not isinstance(choices, list) or len(choices) == 0:
        raise ModelRequestError("model payload missing choices")
    choice = choices[0]
    if not isinstance(choice, dict):
        raise ModelRequestError("model payload choice is invalid")
    message = choice.get("message")
    if not isinstance(message, dict):
        raise ModelRequestError("model payload missing message")
    content = message.get("content")
    if not isinstance(content, str):
        raise ModelRequestError("model payload missing content")
    return content
