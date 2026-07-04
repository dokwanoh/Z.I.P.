from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from zip_agent.core.model_client import CompletionResult
from zip_agent.core.schemas import BenchmarkResult, BenchmarkTask
from zip_agent.harness.datasets import load_jsonl_dataset
from zip_agent.harness.report import write_markdown_report
from zip_agent.harness.runner import run_benchmark


def test_current_report_surface_and_json_row_contract_are_preserved(tmp_path: Path) -> None:
    # Given: the current markdown report surface and result JSON row shape.
    result = BenchmarkResult(
        task_id="task-1",
        task_type="coding",
        policy="baseline",
        input_tokens_before=100,
        input_tokens_after=90,
        output_tokens=25,
        estimated_cost_before=0.001,
        estimated_cost_after=0.0009,
        saving_ratio=0.1,
        quality_score=0.91,
        quality_pass=True,
        latency_ms=12,
        notes="fixture completion",
    )
    report = tmp_path / "baseline.md"

    # When: a markdown report and JSON row are produced.
    write_markdown_report(report, (result,), dry_run=True)
    row = result.as_json_row()
    report_text = report.read_text(encoding="utf-8")

    # Then: the existing human and machine contract remains present.
    assert "# Z.I.P. Benchmark Report" in report_text
    assert "## Summary" in report_text
    assert "## Results" in report_text
    assert "| task | type | policy | input before | input after | saving | quality | Z.I.P. score | notes |" in report_text
    assert tuple(row.keys())[:13] == (
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


def test_benchmark_report_is_generated(tmp_path: Path) -> None:
    tasks = load_jsonl_dataset(Path("benchmarks/tasks/korean_coding_prompts.jsonl"))
    report = tmp_path / "latest.md"
    results = run_benchmark(tasks[:1], ("baseline", "rtk"))

    write_markdown_report(report, results, dry_run=True)

    assert report.exists()
    assert "Z.I.P. Benchmark Report" in report.read_text(encoding="utf-8")
    assert len(results) == 2


def test_benchmark_repeats_record_latency_variance_and_threshold_evidence() -> None:
    # Given: one task, one policy, and a deterministic model client with three policy latencies.
    task = BenchmarkTask(
        id="repeat-task",
        task_type="coding",
        input_prompt="Patch fetch_user_profile and run pytest.",
        repo_context="",
        expected_behavior="preserve fetch_user_profile",
        quality_checks=(),
        risk_level="low",
    )
    client = FixedLatencyClient(latencies_ms=(1, 10, 20, 30))

    # When: the benchmark is run with three repeats.
    result = run_benchmark((task,), ("baseline",), repeats=3, model_client=client)[0]
    row = result.as_json_row()

    # Then: repeat count, latency variance/stdev, cache, judge, and threshold evidence are recorded.
    assert result.repeat_count == 3
    assert result.latency_ms == 20
    assert result.latency_variance_ms == pytest.approx(66.667, abs=0.001)
    assert result.latency_stdev_ms == pytest.approx(8.165, abs=0.001)
    assert row["repeat_count"] == 3
    assert row["cache_status"] == "unsupported"
    assert row["latency_variance_ms"] == pytest.approx(66.667, abs=0.001)
    assert row["latency_stdev_ms"] == pytest.approx(8.165, abs=0.001)
    assert row["judge_provenance"] == "fablize-deterministic"
    assert row["threshold_summary"] == "quality_score=1.000; pass_threshold>0.820; status=pass"


def test_report_records_evidence_fields_without_replacing_markdown(tmp_path: Path) -> None:
    # Given: a benchmark result carrying the new evidence fields.
    result = BenchmarkResult(
        task_id="task-1",
        task_type="coding",
        policy="zip-auto",
        input_tokens_before=100,
        input_tokens_after=80,
        output_tokens=30,
        estimated_cost_before=0.001,
        estimated_cost_after=0.0008,
        saving_ratio=0.2,
        quality_score=0.95,
        quality_pass=True,
        latency_ms=20,
        notes="fixture completion",
        repeat_count=3,
        cache_status="unsupported",
        latency_variance_ms=66.667,
        latency_stdev_ms=8.165,
        judge_provenance="fablize-deterministic",
        threshold_summary="quality_score=0.950; pass_threshold>0.820; status=pass",
    )
    report = tmp_path / "latest.md"

    # When: the markdown report is written.
    write_markdown_report(report, (result,), dry_run=True)
    report_text = report.read_text(encoding="utf-8")

    # Then: markdown remains the human surface and includes the new evidence.
    assert "## Results" in report_text
    assert "## Evidence Summary" in report_text
    assert "Repeat count: 3" in report_text
    assert "Cache status: unsupported" in report_text
    assert "Latency variance/stdev: 66.667 / 8.165 ms" in report_text
    assert "Judge provenance: fablize-deterministic" in report_text
    assert "Threshold summary: quality_score=0.950; pass_threshold>0.820; status=pass" in report_text
    assert "| task | policy | repeat count | cache status | latency ms | latency variance | latency stdev | judge provenance | threshold summary |" in report_text


def test_cli_accepts_repeats_and_writes_report_evidence(tmp_path: Path) -> None:
    # Given: a minimal dataset and the benchmark CLI.
    dataset = tmp_path / "tasks.jsonl"
    report = tmp_path / "latest.md"
    dataset.write_text(
        json.dumps(
            {
                "id": "cli-repeat-task",
                "task_type": "coding",
                "input_prompt": "Patch fetch_user_profile and run pytest.",
                "repo_context": "zip_agent/core/profile.py",
                "expected_behavior": "preserve fetch_user_profile",
                "quality_checks": ["preserves_api_name"],
                "risk_level": "low",
            },
        )
        + "\n",
        encoding="utf-8",
    )

    # When: the CLI is invoked with --repeats 3.
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "zip_agent.cli",
            "benchmark",
            "--dataset",
            str(dataset),
            "--policies",
            "baseline",
            "--repeats",
            "3",
            "--report",
            str(report),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    # Then: the report records the evidence instead of trusting CLI success text alone.
    assert completed.returncode == 0, completed.stderr
    report_text = report.read_text(encoding="utf-8")
    assert "Repeat count: 3" in report_text
    assert "Cache status: unsupported" in report_text
    assert "Latency variance/stdev:" in report_text
    assert "Judge provenance: fablize-deterministic" in report_text
    assert "Threshold summary:" in report_text


class FixedLatencyClient:
    def __init__(self, latencies_ms: tuple[int, ...]) -> None:
        self._latencies_ms = latencies_ms
        self._index = 0

    def complete(self, prompt: str, *, system_prompt: str, max_output_tokens: int) -> CompletionResult:
        latency_ms = self._latencies_ms[self._index]
        self._index += 1
        return CompletionResult(
            content=f"{system_prompt}\n{prompt}\n{max_output_tokens}",
            latency_ms=latency_ms,
            prompt_tokens=1,
            output_tokens=1,
            provider="fixture",
            notes=("fixture completion",),
        )
