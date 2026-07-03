# Z.I.P. Agent

코딩 에이전트의 토큰 낭비를 측정하고, 안전한 경우에만 프롬프트를 줄이는 측정 우선 프레임워크입니다.

## 왜 필요한가

한국어 개발 환경에서는 번역 요청, 중복 설명, 반복된 저장소 요약, 긴 오류 로그, 전체 파일 재출력 때문에 토큰 비용이 쉽게 커집니다.

## 무엇을 하나

Z.I.P.는 작업 유형을 분류하고 LinguaRoom, Headroom, RTK, Caveman 후보 정책을 적용한 뒤 품질 가드로 회귀를 검사합니다. 결과는 재현 가능한 벤치마크 리포트로 남깁니다.

## 빠른 시작

```bash
python -m zip_agent.cli --help
python -m zip_agent.cli benchmark --dataset benchmarks/tasks/korean_coding_prompts.jsonl --policies baseline,linguaroom,headroom,rtk,caveman,zip-auto --report reports/latest.md
```

## 정책

- `baseline`: 원문 유지
- `linguaroom`: 한국어/영어 혼합 의도 정규화
- `headroom`: 출력과 검증 예산을 남기는 문맥 구성
- `rtk`: 중복 지시와 반복 로그 제거
- `caveman`: 낮은 위험 작업에서만 짧은 표현 사용
- `zip-auto`: 작업 유형과 위험도에 따라 정책 조합 선택

## 한계

현재 기본 모드는 dry-run입니다. 프롬프트 토큰 감소와 품질 가드 동작을 검증하지만, 실제 모델 응답 품질을 보장하지 않습니다. 90% 절감은 목표이며, 특정 데이터셋에서 측정될 때만 관측 결과로 표현해야 합니다.
