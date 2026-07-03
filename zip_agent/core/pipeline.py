from __future__ import annotations

from typing import List

from zip_agent.compression.caveman import apply_caveman
from zip_agent.compression.headroom import apply_headroom
from zip_agent.compression.rtk import apply_rtk
from zip_agent.core.router import select_route
from zip_agent.core.schemas import BenchmarkTask, PolicyOutput
from zip_agent.linguaroom.adapter import apply_linguaroom


def run_policy(task: BenchmarkTask, policy: str) -> PolicyOutput:
    if policy == "baseline":
        return PolicyOutput(policy="baseline", prompt=_combined_prompt(task), notes=("no compression",))
    if policy == "linguaroom":
        return apply_linguaroom(_combined_prompt(task))
    if policy == "headroom":
        return apply_headroom(_combined_prompt(task))
    if policy == "rtk":
        return apply_rtk(_combined_prompt(task))
    if policy == "caveman":
        return apply_caveman(_with_combined_prompt(task))
    if policy == "zip-auto":
        return run_zip_auto(task)
    return PolicyOutput(policy=policy, prompt=task.input_prompt, notes=(f"unknown policy: {policy}",), blocked=True)


def run_zip_auto(task: BenchmarkTask) -> PolicyOutput:
    route = select_route(task)
    prompt = _combined_prompt(task)
    notes: List[str] = list(route.notes)
    for policy in route.policies:
        candidate_task = BenchmarkTask(
            id=task.id,
            task_type=route.task_type,
            input_prompt=prompt,
            repo_context="",
            expected_behavior=task.expected_behavior,
            quality_checks=task.quality_checks,
            risk_level=task.risk_level,
        )
        output = run_policy(candidate_task, policy)
        if output.blocked:
            notes.extend(output.notes)
            continue
        prompt = output.prompt
        notes.extend(output.notes)
    return PolicyOutput(policy="zip-auto", prompt=prompt, notes=tuple(notes))


def _combined_prompt(task: BenchmarkTask) -> str:
    if task.repo_context.strip() == "":
        return task.input_prompt
    return f"{task.input_prompt}\n\nContext:\n{task.repo_context}"


def _with_combined_prompt(task: BenchmarkTask) -> BenchmarkTask:
    return BenchmarkTask(
        id=task.id,
        task_type=task.task_type,
        input_prompt=_combined_prompt(task),
        repo_context="",
        expected_behavior=task.expected_behavior,
        quality_checks=task.quality_checks,
        risk_level=task.risk_level,
    )
