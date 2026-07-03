# Z.I.P. Benchmark Report

Mode: dry-run deterministic fixture mode

Dry-run results measure prompt-token changes and deterministic guard behavior only.

## Summary

- Rows: 60
- Average input-token saving: 1.6%
- Quality pass rate: 78.3%

## Results

| task | type | policy | input before | input after | saving | quality | Z.I.P. score | notes |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| kr-edit-001 | korean_translation_heavy | baseline | 91 | 91 | 0.0% | 0.82 | 0.490 | no compression; failed preserves_korean_intent |
| kr-edit-001 | korean_translation_heavy | linguaroom | 91 | 133 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-edit-001 | korean_translation_heavy | headroom | 91 | 91 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed preserves_korean_intent |
| kr-edit-001 | korean_translation_heavy | rtk | 91 | 91 | 0.0% | 0.82 | 0.490 | failed preserves_korean_intent |
| kr-edit-001 | korean_translation_heavy | caveman | 91 | 88 | 3.3% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed preserves_korean_intent |
| kr-edit-001 | korean_translation_heavy | zip-auto | 91 | 133 | 0.0% | 1.00 | 0.600 | Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |
| kr-edit-002 | repo_edit | baseline | 71 | 71 | 0.0% | 1.00 | 0.600 | no compression |
| kr-edit-002 | repo_edit | linguaroom | 71 | 115 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-edit-002 | repo_edit | headroom | 71 | 71 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-edit-002 | repo_edit | rtk | 71 | 65 | 8.5% | 1.00 | 0.634 |  |
| kr-edit-002 | repo_edit | caveman | 71 | 65 | 8.5% | 1.00 | 0.634 | terse compression applied within safe-risk limit |
| kr-edit-002 | repo_edit | zip-auto | 71 | 65 | 8.5% | 1.00 | 0.634 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit |
| kr-debug-001 | debugging | baseline | 80 | 80 | 0.0% | 1.00 | 0.600 | no compression |
| kr-debug-001 | debugging | linguaroom | 80 | 124 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-debug-001 | debugging | headroom | 80 | 80 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-debug-001 | debugging | rtk | 80 | 65 | 18.8% | 1.00 | 0.675 |  |
| kr-debug-001 | debugging | caveman | 80 | 77 | 3.8% | 1.00 | 0.615 | terse compression applied within safe-risk limit |
| kr-debug-001 | debugging | zip-auto | 80 | 62 | 22.5% | 1.00 | 0.690 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit |
| kr-design-001 | design | baseline | 59 | 59 | 0.0% | 1.00 | 0.600 | no compression |
| kr-design-001 | design | linguaroom | 59 | 92 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-design-001 | design | headroom | 59 | 59 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-design-001 | design | rtk | 59 | 59 | 0.0% | 1.00 | 0.600 |  |
| kr-design-001 | design | caveman | 59 | 59 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate |
| kr-design-001 | design | zip-auto | 59 | 92 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |
| kr-verify-001 | verification | baseline | 47 | 47 | 0.0% | 1.00 | 0.600 | no compression |
| kr-verify-001 | verification | linguaroom | 47 | 90 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-verify-001 | verification | headroom | 47 | 47 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-verify-001 | verification | rtk | 47 | 47 | 0.0% | 1.00 | 0.600 |  |
| kr-verify-001 | verification | caveman | 47 | 47 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit |
| kr-verify-001 | verification | zip-auto | 47 | 90 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |
| kr-doc-001 | documentation | baseline | 50 | 50 | 0.0% | 1.00 | 0.600 | no compression |
| kr-doc-001 | documentation | linguaroom | 50 | 72 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-doc-001 | documentation | headroom | 50 | 50 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-doc-001 | documentation | rtk | 50 | 44 | 12.0% | 1.00 | 0.648 |  |
| kr-doc-001 | documentation | caveman | 50 | 50 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit |
| kr-doc-001 | documentation | zip-auto | 50 | 72 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |
| kr-rag-001 | rag_heavy | baseline | 69 | 69 | 0.0% | 1.00 | 0.600 | no compression |
| kr-rag-001 | rag_heavy | linguaroom | 69 | 107 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-rag-001 | rag_heavy | headroom | 69 | 69 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-rag-001 | rag_heavy | rtk | 69 | 69 | 0.0% | 1.00 | 0.600 |  |
| kr-rag-001 | rag_heavy | caveman | 69 | 66 | 4.3% | 1.00 | 0.617 | terse compression applied within safe-risk limit |
| kr-rag-001 | rag_heavy | zip-auto | 69 | 66 | 4.3% | 1.00 | 0.617 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit |
| kr-explain-001 | explanation | baseline | 49 | 49 | 0.0% | 1.00 | 0.600 | no compression |
| kr-explain-001 | explanation | linguaroom | 49 | 83 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-explain-001 | explanation | headroom | 49 | 49 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-explain-001 | explanation | rtk | 49 | 49 | 0.0% | 1.00 | 0.600 |  |
| kr-explain-001 | explanation | caveman | 49 | 49 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate |
| kr-explain-001 | explanation | zip-auto | 49 | 83 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |
| kr-edit-003 | korean_translation_heavy | baseline | 68 | 68 | 0.0% | 0.82 | 0.490 | no compression; failed contains_patch |
| kr-edit-003 | korean_translation_heavy | linguaroom | 68 | 110 | 0.0% | 0.82 | 0.490 | LinguaRoom integration placeholder; deterministic local optimizer used.; failed contains_patch |
| kr-edit-003 | korean_translation_heavy | headroom | 68 | 68 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed contains_patch |
| kr-edit-003 | korean_translation_heavy | rtk | 68 | 68 | 0.0% | 0.82 | 0.490 | failed contains_patch |
| kr-edit-003 | korean_translation_heavy | caveman | 68 | 68 | 0.0% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed contains_patch |
| kr-edit-003 | korean_translation_heavy | zip-auto | 68 | 110 | 0.0% | 0.82 | 0.490 | Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; failed contains_patch |
| kr-security-001 | unknown | baseline | 61 | 61 | 0.0% | 1.00 | 0.600 | no compression |
| kr-security-001 | unknown | linguaroom | 61 | 103 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used. |
| kr-security-001 | unknown | headroom | 61 | 61 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200 |
| kr-security-001 | unknown | rtk | 61 | 61 | 0.0% | 1.00 | 0.600 |  |
| kr-security-001 | unknown | caveman | 61 | 61 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate |
| kr-security-001 | unknown | zip-auto | 61 | 103 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200 |

## Best Policy Per Task

- kr-edit-001: linguaroom (0.0% saving, quality 1.00)
- kr-edit-002: rtk (8.5% saving, quality 1.00)
- kr-debug-001: zip-auto (22.5% saving, quality 1.00)
- kr-design-001: baseline (0.0% saving, quality 1.00)
- kr-verify-001: baseline (0.0% saving, quality 1.00)
- kr-doc-001: rtk (12.0% saving, quality 1.00)
- kr-rag-001: caveman (4.3% saving, quality 1.00)
- kr-explain-001: baseline (0.0% saving, quality 1.00)
- kr-edit-003: baseline (0.0% saving, quality 0.82)
- kr-security-001: baseline (0.0% saving, quality 1.00)

## Best Policy By Workload

- korean_translation_heavy: caveman (3.3% saving)
- repo_edit: rtk (8.5% saving)
- debugging: zip-auto (22.5% saving)
- design: baseline (0.0% saving)
- verification: baseline (0.0% saving)
- documentation: rtk (12.0% saving)
- rag_heavy: caveman (4.3% saving)
- explanation: baseline (0.0% saving)
- unknown: baseline (0.0% saving)

## Honest Limitations

- This report is dry-run unless model API integration is explicitly enabled.
- Output tokens are fixture estimates, not live model completions.
- Cost values are estimates from configured per-token rates.
- Claims should say target or observed-in-this-workload until model-backed runs validate quality.
