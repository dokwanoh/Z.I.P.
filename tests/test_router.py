from zip_agent.core.router import select_route
from zip_agent.core.schemas import BenchmarkTask


def test_router_selects_safer_policy_for_design_tasks() -> None:
    task = BenchmarkTask(
        id="design",
        task_type="design",
        input_prompt="review UX design and accessibility",
        repo_context="",
        expected_behavior="preserve accessibility",
        quality_checks=("no_missing_acceptance_criteria",),
        risk_level="high",
    )
    route = select_route(task)

    assert "caveman" not in route.policies
    assert route.aggressiveness == "conservative"
