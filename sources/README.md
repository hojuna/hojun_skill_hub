# 공개 출처와 확인 범위

조사 기준일: 2026-10-30.

아래 공개 페이지의 설명·스킬 본문을 확인해 후보를 정리했다. 이 저장소는 원문을 재배포하지 않고 링크와 자체 작성한 적용 계획만 제공한다. 확인한 페이지가 있다고 해서 저장소 전체·모든 스크립트·의존성·라이선스 검토가 완료됐다는 뜻은 아니다.

| 출처 | 확인한 항목 | 이 저장소에서의 용도 |
|---|---|---|
| [Cofa Probe](https://www.getcofa.com/ko/probe) | 산출물·작업 기록·사후 설명을 함께 검토한다는 공개 설명 | 평가 방향 참고, 비공개 점수 추정은 하지 않음 |
| [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | 시각 방향, 타이포그래피, 레이아웃 지침 | 웹 UI 풀이 후보 |
| [Anthropic webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) | 로컬 웹앱 Playwright 사용, 서버·브라우저 테스트 | 공통 검수의 웹 보조 후보 |
| [Superpowers systematic-debugging](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md) | 재현·원인 조사·수정 흐름 | 코드 수정 풀이 후보 |
| [Superpowers verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md) | 완료 주장 전에 실행 근거 확인 | 공통 검수 설계 참고 |
| [Vercel React Best Practices](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md) | React/Next.js 성능 규칙 | 해당 스택일 때만 참고 |
| [FastAPI Templates](https://github.com/wshobson/agents/blob/main/plugins/api-scaffolding/skills/fastapi-templates/SKILL.md) | API 구조·의존성·오류·테스트 예시 | Python API 과제의 선택 후보 |
| [Exploratory Data Analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/exploratory-data-analysis/SKILL.md) | 로컬 지원 형식, 데이터 진단 범위, 런타임 요건 | 경량 데이터 스킬의 참고 후보 |
| [Doc Coauthoring](https://github.com/anthropics/skills/blob/main/skills/doc-coauthoring/SKILL.md) | 맥락 수집·구조화·독자 관점 점검 | 문서 풀이 지침 참고 |
| [SQL Optimization Patterns](https://github.com/wshobson/agents/blob/main/plugins/developer-essentials/skills/sql-optimization-patterns/SKILL.md) | 실행 계획·인덱스·성능 패턴 | 후순위 후보 |
| [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp) | MCP/CLI 비교, 설정, 로컬 브라우저 도구, 보안 경계 주의 | 조건부 브라우저 도구 후보 |
| [Playwright Page API](https://playwright.dev/docs/api/class-page) | 테스트에서 networkidle을 권장하지 않음 | webapp-testing 채택 시 수정할 점 |
| [Context7](https://github.com/upstash/context7) | 문서 검색과 query 인자 | 외부 질의 데이터 주의, 기본 비활성 |
| [OpenAI Skills & Plugins](https://developers.openai.com/codex/skills-and-plugins) | 스킬·플러그인의 개념과 선택 방식 | 설치와 단순 clone을 구분 |

## 아직 하지 않은 일

원본 커밋 고정, 라이선스별 재배포 범위 검토, 파일·스크립트 전체 보안 점검, 스킬 본문 수정·포함, 패키지 설치, MCP 연결, 실제 제공 에이전트 호환성 확인, 시나리오별 에이전트 실행과 비교.

따라서 현재 링크는 원문 탐색용이다. 실제 도입 시 선택한 파일과 필요한 참조 자료를 명시하고 버전을 고정해야 한다. 공급망 검사 없이 설치 명령이나 원격 스크립트를 실행하지 않는다.

## 포함하지 않는 자료

개인 이메일, 비공개 운영 가이드 원문, 응시 접속 링크, 실제 시험 문제·답안·작업 로그, 개인 계정·API 인증 정보. 모든 시나리오는 자체 작성한 가상 사례다.
