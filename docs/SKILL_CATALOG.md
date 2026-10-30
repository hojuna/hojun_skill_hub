# Skill 후보 목록과 도입 순서

상태: **목록·설계 단계**. 아래 외부 스킬은 원문을 확인한 참고 후보이며 이 저장소에 설치·복제되지 않았다. 직접 작성 항목도 아직 SKILL.md로 구현되지 않았다. P0/P1/P2는 준비 우선순위이지 공식 점수·출제 확률이 아니다.

## 1. 우선 준비할 풀이 능력

| ID | 후보 | 출처/상태 | 적용 과제 | 도입 시 핵심 조정 |
|---|---|---|---|---|
| SOLVE-UI | frontend-design | Anthropic 공개 원문 확인, P0 | S01~S05, S08 | 기능·기존 디자인을 우선. 새 브랜드 제안이나 장시간 사용자 승인 절차를 강제하지 않기 |
| SOLVE-APP | workflow-app-building | 직접 작성 예정, P0 | S01~S04, S08~S09 | CRUD, 상태 변경, 영속성, 폼 검증, 핵심 사용자 경로를 묶는 짧은 풀이 스킬 |
| SOLVE-DATA | data-transform-report | 직접 작성 예정, P0 | S05~S06, S08, S11 | 타입·중복·집계 정책→변환→작은 정답 표 대조→결과 파일. 과학 분석 풀스택은 제외 |
| SOLVE-DEBUG | systematic-debugging | obra/superpowers 공개 원문 확인, P0 | S07 및 막힌 과제 | 재현·원인·최소 변경·재확인만 중심으로 축소. 전체 Superpowers 워크플로는 설치하지 않기 |
| SOLVE-SEARCH | local-search | 직접 작성 예정, P1 | S10 | 로컬 파일 검색, 출처, 찾지 못함 처리. 모델 API·벡터 DB는 자동 도입하지 않기 |
| SOLVE-BRIEF | brief-writing | 직접 작성 예정, doc-coauthoring 참고, P1 | S12 | 사실/제안 분리, 근거 위치, 실행안. 긴 인터뷰·설계 승인 반복을 줄이기 |

`workflow-app-building`은 특히 중요하다. 시각 디자인 스킬만으로 데이터 모델·저장·상태 전이까지 안정적으로 다룬다고 가정하지 않는다. 디자인과 업무 로직을 별도 능력으로 준비한다.

## 2. 공통 보조는 두 개

| ID | 계획한 이름 | 역할 | 참고 자료 |
|---|---|---|---|
| CHECK | review-result | 요구사항 충족, 실행 가능성, 중요한 오류, 제출 경로를 한 번에 확인 | verification-before-completion + 웹 과제일 때 webapp-testing |
| EXPLAIN | explain-work | 목적, 구현 흐름, 선택 이유, 실제 검증·개선, 한계를 이해하기 쉽게 정리 | 직접 작성 예정 |

### review-result 출력 계약

```text
판정: 제출 가능 / 수정 필요 / 확인 불가
요구사항: 충족 / 미충족 / 미검증
검증: 실제 실행 명령 또는 실제 수행 절차와 관찰 결과
문제: 결과에 영향을 주는 항목, 위치와 재현 방법
다음 행동: 가장 중요한 수정
```

검수는 작성자의 완료 선언을 그대로 믿지 않는다. 스타일 지적과 무관한 리팩터링으로 시간을 쓰지 않는다. 브라우저를 확인하지 못했다면 빌드 통과만으로 UI 검증 완료라고 하지 않는다.

### explain-work 출력 계약

```text
해결한 문제:
입력 → 처리 → 저장/출력 흐름:
핵심 파일·함수:
선택한 방법과 이유:
실제로 수행한 검증:
실제로 바꾼 점과 확인한 효과:
남은 한계·미검증 사항:
```

요구되지 않은 장문의 문서보다 짧은 정확한 설명을 우선한다. 개선 전후 측정이 없으면 수치를 만들어내지 않는다.

## 3. 환경에 따라 추가할 후보

| 후보 | 원문에서 확인한 범위 | 사용 조건 | 이번 계획의 판단 |
|---|---|---|---|
| vercel-react-best-practices | React/Next.js 렌더링·데이터 로딩·성능 규칙 | 실제 프로젝트가 React/Next.js일 때 | P1. 모든 규칙을 읽거나 성능 리팩터링부터 하지 않기 |
| fastapi-templates | FastAPI 구조, 비동기, 의존성, 오류 처리, 테스트 예시 | Python/FastAPI 과제일 때 | P1. 기존 API 유지. 예제의 DB·인증·계층 구조를 통째로 복제하지 않기 |
| exploratory-data-analysis | 지원되는 로컬 데이터의 진단·결측·분포 등 | 데이터 구조를 먼저 파악해야 할 때 | P1 참고용. 정제·집계 자체를 대신하는 스킬은 아님. 런타임·의존성 별도 확인 |
| doc-coauthoring | 문서 맥락 수집, 구조화, 독자 관점 점검 | 문서가 실제 제출물일 때 | P1. 반복 질문·긴 공동 집필 절차를 시간 제한에 맞게 축소 |
| sql-optimization-patterns | 실행 계획·인덱스·쿼리 성능 패턴 | 측정된 SQL 병목 또는 명시적 성능 요구가 있을 때 | P2. 간단한 목록 과제의 기본 팩에서는 제외 |

## 4. 그대로 가져오지 않을 부분

- `frontend-design`: 짧은 실무 과제에서도 독특한 미감·사용자 재승인을 지나치게 앞세우지 않는다. 과제와 기존 디자인을 우선한다.
- `webapp-testing`: 확인한 원문에는 `networkidle` 대기를 강하게 권장하는 내용이 있다. Playwright 공식 문서는 테스트에서 이를 권장하지 않으며 web-first assertion으로 준비 상태를 확인하라고 안내한다. 채택 시 요소·상태 단위 대기 방식으로 수정할 계획이다.
- `fastapi-templates`: 작은 CRUD에 다층 구조, 별도 DB, 인증 스택을 모두 도입하지 않는다.
- `exploratory-data-analysis`: 진단 범위와 Python·추가 라이브러리 요구를 확인한다. 전체 과학 스킬 묶음을 설치하지 않는다.
- `doc-coauthoring`: 맥락이 이미 있는 과제에서 반복 인터뷰를 강제하지 않는다.
- 모든 후보: 라이브러리 예제에 나온 외부 API·서비스를 자동으로 사용하지 않는다. 제공 환경에 없는 전용 런타임도 전제하지 않는다.

## 5. 도입 작업 순서

1. SOLVE-UI, SOLVE-APP, SOLVE-DATA, SOLVE-DEBUG를 먼저 정한다.
2. CHECK와 EXPLAIN을 각각 하나로 작성한다. 검수용 보조 브라우저 지침은 CHECK 아래에서만 선택한다.
3. S02 예약, S05 데이터, S07 버그 수정 시나리오로 없는 경우와 비교한다.
4. 실제 이득이 확인된 항목만 기본 팩에 넣고 나머지는 선택형으로 남긴다.
5. 실제 도입 시 원본 커밋 SHA, 라이선스, 포함할 참조·스크립트, 수정 내역, 의존성, 외부 통신을 기록한다.

최종 자동 발견 방식은 제공된 에이전트 버전에서 확인해야 한다. 단순 clone만으로 모든 스킬이 자동 설치됐다고 가정하지 않는다. 자동 발견이 없더라도 명시적으로 필요한 문서를 읽는 경로를 둔다. 도구 버전 업그레이드를 전제로 설계하지 않는다.

## 원문

- [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)
- [webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md)
- [systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)
- [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)
- [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)
- [fastapi-templates](https://github.com/wshobson/agents/blob/main/plugins/api-scaffolding/skills/fastapi-templates/SKILL.md)
- [exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/exploratory-data-analysis/SKILL.md)
- [doc-coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md)
- [sql-optimization-patterns](https://github.com/wshobson/agents/blob/main/plugins/developer-essentials/skills/sql-optimization-patterns/SKILL.md)
- [Playwright Page API: networkidle 주의](https://playwright.dev/docs/api/class-page)
- [OpenAI Skills & Plugins 개요](https://developers.openai.com/codex/skills-and-plugins)
