# Z.I.P. Agent

Zero-waste Intelligent Pipeline Agent for coding-agent token efficiency.

## Why

Coding agents can spend large token budgets on repeated repo summaries, translation boilerplate, duplicated instructions, stack traces, and full-file rewrites. Korean engineering teams often pay extra for mixed Korean/English intent restatement and translation scaffolding.

## What it does

Z.I.P. measures prompt-token waste, routes each workload to conservative compression policies, runs quality checks, and writes reproducible benchmark reports. Compression methods are candidates, not truths.

## Architecture

LinguaRoom normalizes Korean/English engineering intent. Headroom preserves output and verification budget. RTK removes repeated prompt material. Caveman is a guarded terse mode. Ponytail asks for patch-first code output. The Fablize-inspired quality guard blocks unsafe results.

## Quickstart

```bash
python -m zip_agent.cli --help
python -m pip install -e .
```

## Run benchmark

```bash
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

## Example result

Open `reports/latest.md` after running the command. Dry-run results are clearly marked as fixture-based prompt-token measurements.

## Install

```bash
python -m pip install -e .
```

## Model-backed runs

If `ZIP_MODEL_ENDPOINT` and `ZIP_MODEL_NAME` are set, the harness uses a live OpenAI-compatible completion endpoint instead of dry-run fixtures. Otherwise it stays in dry-run mode.

If `ZIP_LINGUAROOM_COMMAND` is set, the LinguaRoom adapter runs that command on stdin/stdout and falls back to the local optimizer if it fails.

## Compression policies

- `baseline`: no compression.
- `linguaroom`: removes Korean/English translation boilerplate while preserving identifiers.
- `headroom`: keeps task-critical lines within a budget.
- `rtk`: deduplicates repeated instructions and filler.
- `caveman`: terse compression only for low-risk tasks.
- `zip-auto`: routes by task type and risk, then applies a safe policy mix.

## Research boundary

KV-cache compression is a separate research track, not a shipped Z.I.P. product behavior. It stays out of the core Z.I.P. runtime path and out of benchmark saving claims until a future implementation owns the serving stack and passes its own quality gates.

## Quality guard

The guard checks acceptance criteria, identifier preservation, verification evidence, early-stop language, and unsafe policy use. Failed quality gates cap the score.

## Claude Code commands

See `claude/commands/zip-save.md`, `claude/commands/zip-benchmark.md`, and `claude/commands/zip-verify.md`.

## Hermes support

See `hermes/HERMES_AGENT.md` and `hermes/commands/`.

## Skill package

The reusable skill skeleton lives at `skills/zip-token-saver/`.

## Reproducibility

The benchmark corpus is JSONL under `benchmarks/tasks/`. Reports include the exact command and dry-run limitations.

Install and deploy notes are in [docs/deploy.md](docs/deploy.md).

CI is defined in `.github/workflows/ci.yml`.

## Honest limitations

This vertical slice is deterministic and model-free by default. It proves prompt-token reduction and guard behavior, not live completion quality. Real API adapters should be added before making production saving claims.
