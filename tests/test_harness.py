from pathlib import Path

from zip_agent.harness.datasets import load_jsonl_dataset
from zip_agent.harness.report import write_markdown_report
from zip_agent.harness.runner import run_benchmark


def test_benchmark_report_is_generated(tmp_path: Path) -> None:
    tasks = load_jsonl_dataset(Path("benchmarks/tasks/korean_coding_prompts.jsonl"))
    report = tmp_path / "latest.md"
    results = run_benchmark(tasks[:1], ("baseline", "rtk"))

    write_markdown_report(report, results, dry_run=True)

    assert report.exists()
    assert "Z.I.P. Benchmark Report" in report.read_text(encoding="utf-8")
    assert len(results) == 2
