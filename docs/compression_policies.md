# Compression Policies

## baseline

Preserve the original combined prompt and context. This is the measurement control.

## linguaroom

Normalize Korean/English engineering intent, remove translation boilerplate, and preserve identifiers. The current implementation is a deterministic adapter placeholder for future `dokwanoh/LinguaRoom` integration.

## headroom

Reserve budget for model output and verification. Prefer critical task lines, repo maps, acceptance criteria, and diffs over full context.

## rtk

Redundant Token Killer removes duplicate lines, repeated stack-trace noise, and polite filler while preserving code blocks.

## caveman

Terse compression is blocked for high-risk, ambiguous, design, security, legal, and compliance tasks. It is measured against baseline and should roll back if quality drops.

## zip-auto

Classify the workload, choose a policy mix, run the guard, and report measured savings only when quality passes.

## KV-cache research boundary

KV-cache compression is a separate research track, not a core prompt-compression policy. The shipped policy surface remains `baseline`, `linguaroom`, `headroom`, `rtk`, `caveman`, and `zip-auto`; any KV-cache experiment must stay documented outside the runtime path until it has independent serving-stack evidence and rollback criteria.
