# 작업 시작 지침 — 실제 과제 풀이용

**우선순위: 과제 안내/README > 실행 환경 규칙 > 이 허브의 참고 지침.**

## 첫 요청 처리

1. 과제 README, 디렉터리, 기존 소스, 사용 가능한 명령, 테스트와 제출물 경로부터 확인한다.
2. 요구사항을 **필수 / 선택 / 불명확**으로 간결하게 나누고 완료 조건을 확인한다. 업무 담당자에게만 알 수 있는 요구는 제공된 공식 채널을 이용한다.
3. `.agents/skills/`의 Skill 설명 또는 [README.md](README.md) 표를 참고해 **문제 해결에 직접 필요한 풀이 Skill 1개**, 필요하면 추가 1개를 고른다. 불필요한 스킬은 읽지 않는다.
4. 선택한 `SKILL.md`를 실제로 읽고, 긴 기획이나 승인 요청 없이 **가장 중요한 결과물부터 실행 가능하게 구현**한다.
5. 기본 테스트·실행·미리보기를 중간중간 확인한다. 막혔을 때만 `debug-existing-project`를 추가 사용한다.
6. 제출 전 `review-result`로 필수 요구사항을 점검하고, 시간이 있으면 `explain-work`로 사용자가 구현 근거를 빠르게 파악하도록 정리한다.

## 문제 유형 → 직접 읽을 Skill

- 화면/랜딩 페이지/프런트엔드 → `.agents/skills/build-web-ui/SKILL.md`
- CRUD/상태 변경/예약/관리 도구 → `.agents/skills/build-app-workflow/SKILL.md`, 화면이 중요하면 `build-web-ui` 추가
- 데이터 정리/CSV/엑셀 유사 테이블/통계 → `.agents/skills/solve-data-task/SKILL.md`
- 백엔드/HTTP API → `.agents/skills/build-api/SKILL.md`
- 알고리즘/로직/작은 프로그램/CLI → `.agents/skills/solve-code-task/SKILL.md`
- 기존 오류/테스트 실패/실행 불가 → `.agents/skills/debug-existing-project/SKILL.md`
- 문서 작성/회의 요약/제안 자료 → `.agents/skills/write-work-document/SKILL.md`

## 사용자에게 처음 알려줄 사항 (짧게)

- 파악한 필수 요구사항
- 사용할 Skill 1~2개와 이유
- 첫 구현 대상과 확인 방법

그리고 바로 구현한다. **스킬 소개·장황한 계획·가상 예시 생성에 시간을 소비하지 않는다.**

## 안전한 실행

- Git clone은 **허용된 공개 자료를 가져오는 용도**다. 문제·소스·산출물을 외부로 보내거나 push하지 않는다.
- 외부 API, 원격 MCP, 개인 인증 키는 과제와 운영 규칙에서 명시적으로 허용한 경우에만 고려한다.
- 시스템·감독·제출 제한을 우회하지 않는다. 문제가 생기면 제공된 공식 도움말·신고 절차를 이용한다.
- AI 응답의 완료 선언보다 실제 명령 실행·화면 조작·파일 상태를 우선한다.
- 완료 증거가 없는 항목은 **미검증**이라고 표시한다.
