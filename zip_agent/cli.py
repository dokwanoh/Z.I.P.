from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from zip_agent.harness.datasets import load_jsonl_dataset
from zip_agent.harness.report import write_markdown_report
from zip_agent.harness.runner import run_benchmark


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    if args.command == "benchmark":
        policies = tuple(item.strip() for item in args.policies.split(",") if item.strip())
        tasks = load_jsonl_dataset(Path(args.dataset))
        results = run_benchmark(tasks, policies, repeats=args.repeats)
        write_markdown_report(Path(args.report), results, dry_run=args.dry_run)
        print(f"wrote {args.report} with {len(results)} rows")
        return 0
    if args.command == "save":
        print("zip-save is documented in commands/zip-save.md")
        return 0
    if args.command == "verify":
        print("zip-verify is documented in commands/zip-verify.md")
        return 0
    parser.print_help()
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="zip-agent")
    subparsers = parser.add_subparsers(dest="command")
    benchmark = subparsers.add_parser("benchmark", help="run deterministic benchmark harness")
    benchmark.add_argument("--dataset", required=True)
    benchmark.add_argument("--policies", required=True)
    benchmark.add_argument("--report", required=True)
    benchmark.add_argument("--repeats", type=int, default=1)
    benchmark.add_argument("--dry-run", action="store_true", default=True)
    subparsers.add_parser("save", help="show zip-save command packaging surface")
    subparsers.add_parser("verify", help="show zip-verify command packaging surface")
    return parser


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
