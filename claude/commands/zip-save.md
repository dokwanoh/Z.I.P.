# /zip-save

Purpose: compress the current request and relevant repo context using Z.I.P.

Behavior:

1. Estimate original token count.
2. Classify task and risk.
3. Route to `linguaroom`, `headroom`, `rtk`, or guarded `caveman`.
4. Show before/after token estimates.
5. Explain what was removed and what was preserved.
6. Ask confirmation only when risk is medium or high.
