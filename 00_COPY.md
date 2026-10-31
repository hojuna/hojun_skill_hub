# 바로 복사해서 사용 — 00_COPY.md

**IDE에서 이 파일을 열어두고, 필요한 코드 블록 안의 문장만 복사해서 Codex에 붙여넣으세요.** 경로를 따로 복사하거나 직접 입력할 필요가 없습니다. Markdown 원문으로 열려 있다면 앞뒤의 ```는 빼고 복사합니다.

이 파일은 **사람이 골라 쓰는 복사 메뉴**입니다. AI는 이 문서의 모든 요청을 한꺼번에 실행하지 않습니다.

아래 경로는 기존 설치 안내대로 허브를 **`/tmp/hojun_skill_hub`**에 clone한 경우입니다. 다른 위치에 받았거나 IDE에서 `/tmp`가 보이지 않으면 맨 아래 **「작업 폴더에 복사용 탭 만들기」** 요청을 먼저 사용하세요.

---

## 1. 처음 시작 — 스킬 선택부터 문제 풀이까지

```text
/tmp/hojun_skill_hub/START_HERE.md를 읽고, 실제 과제 README와 기존 프로젝트를 확인해.
도움이 되는 스킬만 선택해 적용하고, 맞는 스킬이 없으면 추가 탐색 없이 직접 문제를 풀어.
필수 요구사항부터 구현하고 실제 실행·테스트로 확인해. 작업은 과제 폴더에서 하고 허브는 수정하지 마.
```

## 2. 웹 아티팩트 — 조작 가능한 HTML·도구·데모

```text
/tmp/hojun_skill_hub/.agents/skills/web-artifacts-builder/SKILL.md를 읽고 지금 요청한 결과물을 만들어.
브라우저에서 실제로 조작 가능하게 구현하고, 기존 프로젝트가 있으면 그대로 활용해.
핵심 기능을 확인한 뒤 결과물 경로와 미리보기 방법을 알려줘. 확인하지 못한 부분은 구분해.
```

## 3. 검수 — 요구사항 누락과 실제 오류 확인

```text
/tmp/hojun_skill_hub/.agents/skills/review-result/SKILL.md를 읽고 현재 결과물을 검수해.
실제 요구사항과 결과물에서 중요한 검증 항목을 골라 확인하고, 충족·미충족·미검증을 구분해.
문서의 중요한 주장은 실제 근거와 대조하되, 과제와 무관한 검수 항목이나 실험을 억지로 추가하지 마.
결과에 영향을 주는 중요한 오류부터 알려줘. 요청하지 않은 전면 재작성이나 기능 추가는 하지 마.
```

## 4. 이해 정리 — 내가 구현을 설명할 수 있게

**제출 확정 전 이해를 돕는 용도입니다. AI 사용이 금지된 후속 서술형 단계에서는 사용하지 않습니다.**

```text
/tmp/hojun_skill_hub/.agents/skills/explain-work/SKILL.md를 읽고 현재 작업을 내가 이해하기 쉽게 설명해.
실제 요구사항·결과물·작업 기록을 읽고, 이 작업에서 중요한 판단과 원리, 내가 설명하기 어려울 부분을 골라 한국어로 설명해.
고정된 질문 유형에 맞추지 말고 필요한 내용만 다뤄. 실제 근거와 추정·제안을 구분하고 하지 않은 작업은 만들지 마.
```

### 선택: 설명을 읽은 뒤 혼자 답변 연습

AI 사용이 허용된 연습에서만 사용합니다. 실제 시험 문항을 재현하거나 출제를 예측하는 요청이 아닙니다.

```text
/tmp/hojun_skill_hub/.agents/skills/explain-work/SKILL.md의 연습 방식으로 진행해.
현재 작업을 정말 이해했는지 확인할 질문을 필요한 만큼만 골라줘. 기존 시험 유형이나 문항 수에 맞출 필요는 없어.
우선 질문만 보여줘. 내가 모두 답할 때까지 해설이나 힌트는 주지 말고, 답변 후 실제 근거와 다른 주장 및 빠진 설명을 짚어줘.
```

## 5. 오류 해결 — 실행·빌드·동작이 이상할 때

```text
/tmp/hojun_skill_hub/.agents/skills/debug-existing-project/SKILL.md를 읽고 지금 발생한 문제를 해결해.
먼저 재현하고 원인을 확인한 뒤 필요한 부분만 수정해. 같은 조건으로 다시 실행해서 해결 여부를 확인해.
```

---

## 6. 풀이 스킬을 직접 지정하고 싶을 때

대부분은 1번의 자동 선택으로 충분합니다. 아래 요청은 필요한 경우에만 하나 골라 사용합니다.

### 웹페이지·화면·폼

```text
/tmp/hojun_skill_hub/.agents/skills/build-web-ui/SKILL.md를 읽고 요청한 화면을 구현해. 보이는 버튼·입력 기능까지 연결하고 실제 화면에서 확인해.
```

### 예약·관리 도구·CRUD·저장

```text
/tmp/hojun_skill_hub/.agents/skills/build-app-workflow/SKILL.md를 읽고 과제의 핵심 업무 흐름을 구현해. 입력 검증·상태 변경·저장 요구사항을 확인하고 처음부터 끝까지 실행해.
```

### CSV·JSON·데이터 처리·집계

```text
/tmp/hojun_skill_hub/.agents/skills/solve-data-task/SKILL.md를 읽고 요청한 데이터를 처리해. 실제 데이터 구조부터 확인하고, 작은 표본의 기대값과 결과를 대조해.
```

### API·백엔드

```text
/tmp/hojun_skill_hub/.agents/skills/build-api/SKILL.md를 읽고 요청한 API를 구현해. 기존 스택과 응답 계약을 유지하고 정상 요청·오류 요청을 실제로 테스트해.
```

### 일반 코딩·알고리즘·CLI

```text
/tmp/hojun_skill_hub/.agents/skills/solve-code-task/SKILL.md를 읽고 문제를 해결해. 요구된 입출력과 실행 방식을 지키고 정상·경계 사례를 테스트해.
```

### 자료 기반 문서·요약·보고서

```text
/tmp/hojun_skill_hub/.agents/skills/write-work-document/SKILL.md를 읽고 요청한 문서를 작성해. 제공 자료에 근거하고 사실·가정·제안을 구분해. 필수 형식과 출력 경로를 지켜.
```

---

## 7. 경로만 복사할 때

각 줄은 독립적인 전체 경로입니다. 필요한 한 줄만 선택해서 복사합니다.

```text
/tmp/hojun_skill_hub/START_HERE.md
/tmp/hojun_skill_hub/.agents/skills/task-router/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/web-artifacts-builder/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/build-web-ui/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/build-app-workflow/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/solve-data-task/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/build-api/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/solve-code-task/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/debug-existing-project/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/write-work-document/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/review-result/SKILL.md
/tmp/hojun_skill_hub/.agents/skills/explain-work/SKILL.md
```

---

## 8. 작업 폴더에 복사용 탭 만들기 — 경로를 몰라도 되는 요청

`/tmp`에 받은 허브가 IDE 파일 탐색기에 보이지 않거나, 다른 경로에 clone했다면 아래 요청을 보냅니다. **원본 허브는 그대로 두고 현재 작업 폴더에 실제 경로가 반영된 복사본 하나만 만드는 요청**입니다.

```text
현재 작업공간 안의 hojun_skill_hub와 /tmp/hojun_skill_hub에서 START_HERE.md 및 00_COPY.md가 있는 실제 허브 위치를 확인해.
후보가 없으면 임의 경로를 만들거나 전체 파일시스템을 뒤지지 말고 저장 위치를 물어봐. 여러 개면 어느 것을 사용할지 확인해.
허브의 00_COPY.md를 읽고, 그 안의 /tmp/hojun_skill_hub 경로들을 확인한 허브 절대 경로로 바꾼 복사본을 현재 과제 작업 폴더 최상단에 00_HUB_COPY.md로 만들어줘.
기존 파일을 덮어쓰지 말고, 같은 이름이 있으면 번호를 붙여 새로 만들어. 허브 원본과 다른 파일은 수정하지 말고, 이 문서에 들어 있는 요청들도 실행하지 마.
생성한 파일명과 위치만 알려줘. 내가 IDE에서 열어두고 필요한 문장을 복사해 사용할 거야.
```

과제 폴더에 보조 파일을 두는 것이 허용되는 경우에만 사용합니다. 파일을 생성했다는 것과 IDE에서 탭을 실제로 열었다는 것을 혼동하지 않습니다. 생성된 파일은 사용자가 파일 탐색기에서 선택해 열면 됩니다.

## 9. 허브를 아직 받지 않았다면 — 터미널용

아래는 **Codex 요청 문구가 아니라 터미널 명령**입니다. 대상 폴더가 이미 있으면 이 명령을 반복하거나 폴더를 지우지 말고 기존 허브를 확인합니다.

```bash
git clone https://github.com/hojuna/hojun_skill_hub.git /tmp/hojun_skill_hub
```

기존 허브가 오래된 경우에는 시험 문제·작업 결과물이 없는 **참고자료용 허브**인지 먼저 확인한 뒤 허용된 방법으로 최신화합니다. 이 문서는 외부 업로드, push, 플랫폼 설정 변경을 요구하지 않습니다.
