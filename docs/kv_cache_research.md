# KV-cache Research Track

KV-cache compression is a separate research track. It is not part of the core Z.I.P. runtime path, not a shipped compression policy, and not included in benchmark saving claims.

## Why it is separate

Core Z.I.P. compresses prompt and repo-context text before a model call, then measures token deltas and quality-guard outcomes. KV-cache compression works inside the inference serving layer after tokens have already entered the model. That layer has different failure modes: attention-state corruption, long-context recall loss, provider-specific cache semantics, and hardware-dependent latency tradeoffs.

## Current scope

- Survey KV-cache and long-context serving papers.
- Track prototype ideas that could matter if Z.I.P. later owns the serving stack.
- Define measurement fixtures for cache hit rate, latency, memory pressure, and quality retention.
- Keep all notes separate from the main policy router and benchmark report.

## Out of scope for core runtime

- No KV-cache implementation in `zip_agent`.
- No KV-cache option in `zip-auto` or the policy router.
- No benchmark report language that counts KV-cache behavior as Z.I.P. product savings.
- No production claim without a named dataset, model, serving stack, and rollback threshold.

## Promotion criteria

Moving this research track toward product work would require a future plan that owns the serving stack, adds a reversible implementation behind explicit capability detection, and benchmarks quality retention against a named dataset. Until then, KV-cache work remains documentation and research only.
