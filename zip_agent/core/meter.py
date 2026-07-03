from __future__ import annotations

from dataclasses import dataclass

from zip_agent.core.tokenizer import estimate_tokens


@dataclass(frozen=True)
class MeterConfig:
    input_cost_per_million: float = 3.0
    output_cost_per_million: float = 15.0


@dataclass(frozen=True)
class MeterReading:
    input_tokens: int
    output_tokens: int
    estimated_cost: float


def measure_prompt(prompt: str, output_text: str = "", config: MeterConfig = MeterConfig()) -> MeterReading:
    input_tokens = estimate_tokens(prompt)
    output_tokens = estimate_tokens(output_text)
    cost = (
        input_tokens * config.input_cost_per_million
        + output_tokens * config.output_cost_per_million
    ) / 1_000_000
    return MeterReading(input_tokens=input_tokens, output_tokens=output_tokens, estimated_cost=cost)
