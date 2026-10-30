# Hojun Skill Hub

범용 코딩 에이전트용 **실제 실행 가능한 Agent Skills 모음**. 특정 시험 문제, 답안, 가상 문제집이 들어 있지 않습니다.

## 핵심 원칙

- **풀이 우선:** 과제 요구사항을 충족하는 작동 결과물을 만드는 데 집중합니다.
- **선택적으로 사용:** 과제와 관련된 풀이 Skill 1~2개만 읽습니다. 전체 Skill을 한꺼번에 적용하지 않습니다.
- **맞는 스킬이 없어도 대응:** `resolve-skill-gap`이 기존 스킬 조합, 일반 풀이, 허용된 자료 탐색, 실제 장애 보고 중 적합한 경로를 안내합니다.
- **검수·이해는 보조:** `review-result`, `explain-work`를 필요할 때 한 번씩 사용합니다.
- **기존 환경 존중:** 제공된 코드·테스트·도구·제출 규칙이 언제나 우선합니다.
- **규정 준수:** 문제·파일·산출물의 외부 전송, 비허용 도구 사용, 감독·플랫폼 제한 우회를 지시하지 않습니다.

## 0. 빠른 시작 — 그대로 따라 하기

**① 작업 환경 터미널에서 공개 허브 가져오기**

```bash
git clone https://github.com/hojuna/hojun_skill_hub.git /tmp/hojun_skill_hub
```

**② 과제의 작업 디렉터리에서 선택적으로 Skill 설치 (선택 사항)**

```bash
bash /tmp/hojun_skill_hub/scripts/install-skills.sh "$PWD"
```

위 스크립트는 `<현재 작업 디렉터리>/.agents/skills/`에 각 Skill 디렉터리를 복사하며, **같은 이름의 기존 Skill을 덮어쓰지 않습니다**. 스크립트는 네트워크 접속이나 파일 업로드를 하지 않습니다. 과제 작업 폴더에 스킬 복사 자체가 부적절하다면 이 단계를 건너뛰세요.

**③ Codex 시작 / 지시**

이미 실행 중이거나 설치한 스킬이 자동 인식되지 않으면, Codex에서 먼저 다음 파일을 직접 읽도록 지시하면 됩니다.

```text
/tmp/hojun_skill_hub/START_HERE.md를 읽고, 실제 과제 README와
기존 프로젝트를 확인해. 필요한 풀이 스킬만 선택해서 구현해.
맞는 스킬이 없거나 일부만 맞으면 resolve-skill-gap을 읽고
적합한 대안을 선택해. 경로는 읽은 START_HERE.md의 디렉터리를 기준으로 해.
```

Skill 자동 발견은 Codex 배포 버전·세션 시작 시점에 따라 다를 수 있습니다. 이 저장소는 **수동 파일 읽기**로도 사용 가능합니다. Codex 업데이트를 요구하지 않습니다.

### 이미 설치한 경우

설치 스크립트를 다시 실행해도 **복사된 기존 Skill은 갱신되지 않습니다**. 허용된 환경에서 허브 원본을 최신화한 뒤 최신 허브의 `START_HERE.md`와 그 안의 스킬을 직접 읽도록 지정하면 됩니다. 제공된 Codex나 플랫폼 설정은 변경하지 않습니다. 시험 문제·결과물이 없는 공개 참고자료용 허브와 실제 작업 폴더를 구분하세요.

## 상황별 스킬

| 필요한 상황 | 사용 스킬 | 역할 |
|---|---|---|
| 과제가 무엇인지 분류 | `task-router` | 시작 시 필요한 Skill만 선택 |
| 맞는 스킬이 없음·일부만 맞음 | `resolve-skill-gap` | 조합·일반 풀이·자료 탐색·장애 대응 선택 |
| 웹페이지·랜딩 페이지 | `build-web-ui` | 실제로 작동하는 화면, 폼, 반응형 |
| 예약·문의·할 일·관리 앱 | `build-app-workflow` | CRUD, 상태, 저장, 검증 |
| CSV/JSON 가공·집계·리포트 | `solve-data-task` | 데이터 정합성과 출력 검증 |
| REST API·서버 작업 | `build-api` | 라우트, 계약, 오류 처리, API 테스트 |
| 알고리즘·유틸리티·CLI 로직 | `solve-code-task` | 정답 로직과 경계 입력 |
| 기존 코드 오류·빌드 실패 | `debug-existing-project` | 재현→원인→최소 수정→재실행 |
| 자료 기반 문서·요약·제안서 | `write-work-document` | 근거 기반 문서와 필수 형식 |
| 완료 후 핵심 검수 | `review-result` | 미충족·미검증·제출 상태 확인 |
| 본인이 구현을 이해하고 싶을 때 | `explain-work` | 코드 흐름과 실제 판단 근거 요약 |

처음 읽을 파일: [START_HERE.md](START_HERE.md) · [MCP 판단 기준](docs/MCP.md) · [참고 출처](docs/SOURCES.md)

## 저장소 구조

```text
.agents/skills/
  task-router/SKILL.md
  resolve-skill-gap/SKILL.md
  build-web-ui/SKILL.md
  build-app-workflow/SKILL.md
  solve-data-task/SKILL.md
  build-api/SKILL.md
  solve-code-task/SKILL.md
  debug-existing-project/SKILL.md
  write-work-document/SKILL.md
  review-result/SKILL.md
  explain-work/SKILL.md
START_HERE.md
AGENTS.md
scripts/install-skills.sh
scripts/validate-skills.py
docs/MCP.md
docs/SOURCES.md
```

## 검증

```bash
python3 scripts/validate-skills.py
```

이 검사는 **Skill 구조·메타데이터의 기본 유효성만 확인**합니다. 각 과제에서 성능 향상과 Codex 자동 발견까지 증명하는 테스트는 아닙니다.
