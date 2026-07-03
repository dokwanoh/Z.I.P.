# zip-token-saver

Use this skill when a coding agent needs to reduce prompt/token waste safely.

Workflow:

1. Classify the task and risk.
2. Measure baseline prompt tokens.
3. Apply the safest candidate policy.
4. Run the quality guard.
5. Report savings only with reproducible evidence.

References:

- `references/policies.md`
- `references/scoring.md`

Scripts:

- `scripts/zip_measure.py`
- `scripts/zip_harness.py`
