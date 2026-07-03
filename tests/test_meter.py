from zip_agent.core.meter import measure_prompt
from zip_agent.core.tokenizer import estimate_tokens


def test_token_meter_counts_consistently_when_prompt_repeated() -> None:
    first = estimate_tokens("fix fetch_user_profile 한국어")
    second = measure_prompt("fix fetch_user_profile 한국어").input_tokens

    assert first == second
    assert first > 0
