---
name: review-result
description: Independently verify a completed solution against the task README and acceptance criteria. Use before submission to catch missing features, broken commands, data inconsistencies, incorrect paths, untested assumptions, and critical regressions.
---

# Verify the deliverable, not the agent's confidence

**Default: inspect and report.** If asked to fix issues, fix critical ones and rerun tests; don't expand scope into optional refactors.

1. Re-read the real assignment/README. Extract each **mandatory** item and its exact output path/format.
2. Inspect source and created files. Check output artifacts exist and the expected entrypoint runs.
3. Execute the best existing tests/build/CLI. For a web UI, use actual preview/main user flow if accessible. For data, reconcile counts and a sample expected output.
4. Distinguish **passed / failed / not tested** for each mandatory item. A successful build is not proof that clicks/forms work.
5. Rank problems: (P0) cannot run, missing submission, incorrect primary result; (P1) broken mandatory edge case; (P2) nonessential polish.
6. Recommend the **next highest-impact fix** with exact file or reproduction steps. Never make up command output.

## Short required format

```text
판정: 제출 가능 / 수정 필요 / 확인 불가
필수조건: 충족 N / 미충족 N / 미검증 N
실행 증거: [명령/사용자 흐름] → [실제 결과]
핵심 문제: [파일·재현 조건·심각도, 없으면 '확인 범위에서 없음']
다음 행동: [가장 중요한 수정 또는 제출 전 확인]
```

If environment limitations prevented checking, state them. Do not rewrite the entire app simply because a different architecture looks cleaner.
