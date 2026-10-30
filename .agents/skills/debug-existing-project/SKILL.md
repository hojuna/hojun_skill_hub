---
name: debug-existing-project
description: Diagnose and fix an existing program when tests fail, runtime crashes, build errors occur, an API behaves incorrectly, or UI interactions break. Use when the main task is debugging or when another solving skill gets stuck.
---

# Evidence-driven debugging

Apply only when an error or broken behavior is present.

1. **Reproduce:** run the smallest existing command or user flow; record expected vs observed behavior and precise error/output.
2. **Locate:** inspect stack trace, failing test, relevant function, recent diff, state changes, and comparable working paths. Trace the input until the first incorrect state/result.
3. **Hypothesis:** state one likely root cause and the evidence. Avoid changing multiple independent variables together.
4. **Fix minimally:** add or update a regression test when feasible; change the fewest necessary lines to address the cause, not symptoms.
5. **Re-run:** repeat the original failing scenario and nearby relevant tests. Compare with baseline and check for regressions.
6. **Escalate if stuck:** after two ineffective attempts, stop repeating guesses; check assumptions, versions/configuration, logs and whether the requirement was misread.

## Time-limited decisions

- Prioritize errors blocking required behavior.
- Preserve existing architecture and working routes.
- An environment issue is not proof the code is correct; report what could not run.
- For flaky/browser issues, use explicit event or readiness checks rather than arbitrary sleeps when possible.

## Output

`재현 조건 → 근본 원인/근거 → 수정 위치 → 동일 조건 재검증 결과 → 남은 위험`.

Do not claim the bug is fixed until the same failing condition is tested successfully.
