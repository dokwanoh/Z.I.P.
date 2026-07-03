from __future__ import annotations

import re

from zip_agent.core.schemas import PolicyOutput


def patch_first_prompt(prompt: str) -> PolicyOutput:
    instruction = (
        "Use Ponytail: produce the minimal patch, reference unchanged code, "
        "keep type hints/tests, and avoid full-file dumps."
    )
    return PolicyOutput(policy="ponytail", prompt=f"{prompt.strip()}\n{instruction}", notes=("patch discipline added",))


def compact_code_response(response: str) -> str:
    if "```diff" in response or "--- " in response:
        return response.strip()
    without_preface = re.sub(r"(?is)^.*?(?=```)", "", response).strip()
    return without_preface or response.strip()
