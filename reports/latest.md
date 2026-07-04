# Z.I.P. Benchmark Report

Mode: dry-run deterministic fixture mode

Dry-run results measure prompt-token changes and deterministic guard behavior only.

## Summary

- Rows: 132
- Average input-token saving: 0.9%
- Quality pass rate: 81.1%
- Repeat count: 3
- Cache status: unsupported
- Latency variance/stdev: 0.000 / 0.000 ms
- Judge provenance: fablize-deterministic
- Threshold summary: pass=107; fail=25; pass_threshold>0.820

## Results

| task | type | policy | input before | input after | saving | quality | Z.I.P. score | notes |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| kr-edit-001 | korean_translation_heavy | baseline | 91 | 91 | 0.0% | 0.82 | 0.490 | no compression; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-001 | korean_translation_heavy | linguaroom | 91 | 133 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-001 | korean_translation_heavy | headroom | 91 | 91 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-001 | korean_translation_heavy | rtk | 91 | 91 | 0.0% | 0.82 | 0.490 | failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-001 | korean_translation_heavy | caveman | 91 | 88 | 3.3% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-001 | korean_translation_heavy | zip-auto | 91 | 133 | 0.0% | 1.00 | 0.600 | Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | baseline | 71 | 71 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | linguaroom | 71 | 115 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | headroom | 71 | 71 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | rtk | 71 | 65 | 8.5% | 1.00 | 0.634 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | caveman | 71 | 65 | 8.5% | 1.00 | 0.634 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-002 | repo_edit | zip-auto | 71 | 65 | 8.5% | 1.00 | 0.634 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | baseline | 80 | 80 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | linguaroom | 80 | 124 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | headroom | 80 | 80 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | rtk | 80 | 65 | 18.8% | 1.00 | 0.675 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | caveman | 80 | 77 | 3.8% | 1.00 | 0.615 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-001 | debugging | zip-auto | 80 | 62 | 22.5% | 1.00 | 0.690 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | baseline | 59 | 59 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | linguaroom | 59 | 92 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | headroom | 59 | 59 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | rtk | 59 | 59 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | caveman | 59 | 59 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-001 | design | zip-auto | 59 | 92 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | baseline | 47 | 47 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | linguaroom | 47 | 90 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | headroom | 47 | 47 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | rtk | 47 | 47 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | caveman | 47 | 47 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-001 | verification | zip-auto | 47 | 90 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | baseline | 50 | 50 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | linguaroom | 50 | 72 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | headroom | 50 | 50 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | rtk | 50 | 44 | 12.0% | 1.00 | 0.648 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | caveman | 50 | 50 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-001 | documentation | zip-auto | 50 | 72 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | baseline | 69 | 69 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | linguaroom | 69 | 107 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | headroom | 69 | 69 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | rtk | 69 | 69 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | caveman | 69 | 66 | 4.3% | 1.00 | 0.617 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-001 | rag_heavy | zip-auto | 69 | 66 | 4.3% | 1.00 | 0.617 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | baseline | 49 | 49 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | linguaroom | 49 | 83 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | headroom | 49 | 49 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | rtk | 49 | 49 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | caveman | 49 | 49 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-001 | explanation | zip-auto | 49 | 83 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | baseline | 68 | 68 | 0.0% | 0.82 | 0.490 | no compression; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | linguaroom | 68 | 110 | 0.0% | 0.82 | 0.490 | LinguaRoom integration placeholder; deterministic local optimizer used.; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | headroom | 68 | 68 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | rtk | 68 | 68 | 0.0% | 0.82 | 0.490 | failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | caveman | 68 | 68 | 0.0% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-003 | korean_translation_heavy | zip-auto | 68 | 110 | 0.0% | 0.82 | 0.490 | Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | baseline | 61 | 61 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | linguaroom | 61 | 103 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | headroom | 61 | 61 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | rtk | 61 | 61 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | caveman | 61 | 61 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-001 | unknown | zip-auto | 61 | 103 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | baseline | 59 | 59 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | linguaroom | 59 | 99 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | headroom | 59 | 59 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | rtk | 59 | 59 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | caveman | 59 | 59 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-004 | repo_edit | zip-auto | 59 | 59 | 0.0% | 1.00 | 0.600 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | baseline | 58 | 58 | 0.0% | 0.82 | 0.490 | no compression; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | linguaroom | 58 | 93 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | headroom | 58 | 58 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | rtk | 58 | 58 | 0.0% | 0.82 | 0.490 | failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | caveman | 58 | 58 | 0.0% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-edit-005 | korean_translation_heavy | zip-auto | 58 | 93 | 0.0% | 1.00 | 0.600 | Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | baseline | 49 | 49 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | linguaroom | 49 | 92 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | headroom | 49 | 49 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | rtk | 49 | 49 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | caveman | 49 | 49 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-002 | debugging | zip-auto | 49 | 49 | 0.0% | 1.00 | 0.600 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | baseline | 49 | 49 | 0.0% | 0.82 | 0.490 | no compression; failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | linguaroom | 49 | 93 | 0.0% | 0.82 | 0.490 | LinguaRoom integration placeholder; deterministic local optimizer used.; failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | headroom | 49 | 49 | 0.0% | 0.82 | 0.490 | reserved output budget: 1200; failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | rtk | 49 | 49 | 0.0% | 0.82 | 0.490 | failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | caveman | 49 | 49 | 0.0% | 0.82 | 0.490 | terse compression applied within safe-risk limit; failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-debug-003 | debugging | zip-auto | 49 | 49 | 0.0% | 0.82 | 0.490 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; failed contains_verification; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | baseline | 47 | 47 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | linguaroom | 47 | 85 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | headroom | 47 | 47 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | rtk | 47 | 44 | 6.4% | 1.00 | 0.626 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | caveman | 47 | 43 | 8.5% | 1.00 | 0.634 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-002 | documentation | zip-auto | 47 | 80 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | baseline | 49 | 49 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | linguaroom | 49 | 90 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | headroom | 49 | 49 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | rtk | 49 | 49 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | caveman | 49 | 49 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-doc-003 | documentation | zip-auto | 49 | 90 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | baseline | 48 | 48 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | linguaroom | 48 | 91 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | headroom | 48 | 48 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | rtk | 48 | 48 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | caveman | 48 | 48 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-verify-002 | verification | zip-auto | 48 | 91 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | baseline | 64 | 64 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | linguaroom | 64 | 101 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | headroom | 64 | 64 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | rtk | 64 | 64 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | caveman | 64 | 61 | 4.7% | 1.00 | 0.619 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-002 | rag_heavy | zip-auto | 64 | 61 | 4.7% | 1.00 | 0.619 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | baseline | 66 | 66 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | linguaroom | 66 | 105 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | headroom | 66 | 66 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | rtk | 66 | 66 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | caveman | 66 | 66 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-rag-003 | rag_heavy | zip-auto | 66 | 66 | 0.0% | 1.00 | 0.600 | adaptive policy mix selected; reserved output budget: 1200; terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | baseline | 63 | 63 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | linguaroom | 63 | 105 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | headroom | 63 | 63 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | rtk | 63 | 63 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | caveman | 63 | 63 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-design-002 | design | zip-auto | 63 | 105 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | baseline | 49 | 49 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | linguaroom | 49 | 88 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | headroom | 49 | 49 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | rtk | 49 | 49 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | caveman | 49 | 49 | 0.0% | 1.00 | 0.600 | terse compression applied within safe-risk limit; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-explain-002 | explanation | zip-auto | 49 | 88 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | baseline | 50 | 50 | 0.0% | 1.00 | 0.600 | no compression; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | linguaroom | 50 | 87 | 0.0% | 1.00 | 0.600 | LinguaRoom integration placeholder; deterministic local optimizer used.; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | headroom | 50 | 50 | 0.0% | 1.00 | 0.600 | reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | rtk | 50 | 50 | 0.0% | 1.00 | 0.600 | fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | caveman | 50 | 50 | 0.0% | 0.00 | 0.260 | blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |
| kr-security-002 | unknown | zip-auto | 50 | 87 | 0.0% | 1.00 | 0.600 | caveman disabled for risk-sensitive workload; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none |

## Evidence Summary

| task | policy | repeat count | cache status | latency ms | latency variance | latency stdev | judge provenance | threshold summary |
| --- | --- | ---: | --- | ---: | ---: | ---: | --- | --- |
| kr-edit-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.000; pass_threshold>0.820; status=fail |
| kr-design-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.000; pass_threshold>0.820; status=fail |
| kr-explain-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-003 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-003 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-003 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-003 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-003 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-003 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-security-001 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-001 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-001 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-001 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-001 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.000; pass_threshold>0.820; status=fail |
| kr-security-001 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-004 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-005 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-005 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-edit-005 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-005 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-005 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-edit-005 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-debug-003 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-debug-003 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-debug-003 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-debug-003 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-debug-003 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-debug-003 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.820; pass_threshold>0.820; status=fail |
| kr-doc-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-doc-003 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-verify-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-rag-003 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-design-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.000; pass_threshold>0.820; status=fail |
| kr-design-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-explain-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-002 | baseline | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-002 | linguaroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-002 | headroom | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-002 | rtk | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |
| kr-security-002 | caveman | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=0.000; pass_threshold>0.820; status=fail |
| kr-security-002 | zip-auto | 3 | unsupported | 0 | 0.000 | 0.000 | fablize-deterministic | quality_score=1.000; pass_threshold>0.820; status=pass |

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
- kr-edit-004: baseline (0.0% saving, quality 1.00)
- kr-edit-005: linguaroom (0.0% saving, quality 1.00)
- kr-debug-002: baseline (0.0% saving, quality 1.00)
- kr-debug-003: baseline (0.0% saving, quality 0.82)
- kr-doc-002: caveman (8.5% saving, quality 1.00)
- kr-doc-003: baseline (0.0% saving, quality 1.00)
- kr-verify-002: baseline (0.0% saving, quality 1.00)
- kr-rag-002: caveman (4.7% saving, quality 1.00)
- kr-rag-003: baseline (0.0% saving, quality 1.00)
- kr-design-002: baseline (0.0% saving, quality 1.00)
- kr-explain-002: baseline (0.0% saving, quality 1.00)
- kr-security-002: baseline (0.0% saving, quality 1.00)

## Best Policy By Workload

- korean_translation_heavy: caveman (3.3% saving)
- repo_edit: rtk (8.5% saving)
- debugging: zip-auto (22.5% saving)
- design: baseline (0.0% saving)
- verification: baseline (0.0% saving)
- documentation: rtk (12.0% saving)
- rag_heavy: caveman (4.7% saving)
- explanation: baseline (0.0% saving)
- unknown: baseline (0.0% saving)

## Regression Notes

- kr-edit-001 / baseline: no compression; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-001 / headroom: reserved output budget: 1200; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-001 / rtk: failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-001 / caveman: terse compression applied within safe-risk limit; failed preserves_korean_intent; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-design-001 / caveman: blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-explain-001 / caveman: blocked by risk gate; blocked by risk gate; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / baseline: no compression; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / linguaroom: LinguaRoom integration placeholder; deterministic local optimizer used.; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / headroom: reserved output budget: 1200; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / rtk: failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / caveman: terse compression applied within safe-risk limit; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none
- kr-edit-003 / zip-auto: Korean intent normalization prioritized; LinguaRoom integration placeholder; deterministic local optimizer used.; reserved output budget: 1200; failed contains_patch; fixture completion; supports_prompt_caching=False; prompt_cache_mode=none; supports_structured_output=False; structured_output_transport=none; supports_server_side_state=False; state_handle_name=none

## Honest Limitations

- This report is dry-run unless model API integration is explicitly enabled.
- Output tokens are fixture estimates, not live model completions.
- Cost values are estimates from configured per-token rates.
- Claims should say target or observed-in-this-workload until model-backed runs validate quality.
