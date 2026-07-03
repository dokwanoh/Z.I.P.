# Policies

`baseline` preserves the original prompt.

`linguaroom` removes translation boilerplate and preserves Korean engineering intent, identifiers, file paths, API names, and acceptance criteria.

`headroom` reserves output and verification budget, preferring repo maps and diffs over full files.

`rtk` removes repeated instructions, repeated file lists, stack-trace noise, polite filler, and duplicate Korean/English restatements.

`caveman` is risky and must be blocked for high-risk, security, legal, compliance, ambiguous, design-heavy, or multi-step tasks.

`zip-auto` classifies the workload, chooses a policy mix, runs the quality guard, and rolls back unsafe compression.
