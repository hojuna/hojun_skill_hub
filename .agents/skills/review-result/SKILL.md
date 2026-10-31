---
name: review-result
description: Verify a solution against requirements, actual execution, failure paths and user-visible output quality. Use before submission to catch missing behavior, untested states, unsupported test or performance claims in documents, critical regressions and incorrect deliverable paths.
---

# Verify behavior and claims, not the agent's confidence

**Default: inspect, run bounded relevant checks, and report.** Fix only when requested, then rerun. Do not expand into optional refactors, mandatory benchmarks or extra infrastructure. Task-solving time and the original requirements remain the priority.

## Focused checks

1. Read the actual task/README. Extract mandatory behavior, output paths/formats and acceptance criteria. Inspect implementation and existing tests rather than relying on a completion summary.
2. Trace the primary end-to-end action. Check component handoffs and, where applicable, who reads/writes state, persistence and transition rules. Distinguish an accepted request from a completed result; compare the user's displayed status with actual outcome.
3. Run the best existing tests/build/CLI and one primary user flow when accessible. Compare a representative output with task-defined constraints or a known expected result. A successful build, HTTP response or execution status is not proof of usable/correct output. State what a validator covers and leaves unchecked.
4. Check relevant negative paths: malformed/semantically invalid input, processing failure, timeouts and resource limits where they exist. Verify the resulting response/state, partial data and user-visible error. Do not infer retry/recovery/concurrency guarantees from the architecture's name. Label static inspection separately from executed checks.
5. Audit important assertions in README, reports and explanation files against code and actual run records using the evidence check below. Flag contradictions or unsupported claims even when functionality works.
6. Mark mandatory items **passed / failed / not tested**. Prioritize P0: cannot run/missing output/wrong primary result; P1: mandatory edge-case or serious unsupported claim; P2: optional polish. Give the next highest-impact correction with exact reproduction or source location.

## Evidence check for document claims

For important claims record **주장 → 코드·테스트 위치 → 실제 실행 명령/조건/결과 → 근거 상태**. A script or test definition is not an execution record. Missing evidence means **확인 불가**, not that the claimed action certainly did not occur.

For a load/performance claim, look for workload/data size, concurrency or arrival rate, duration/count, environment and revision, metrics and recorded results. Separate request acceptance time from actual completion time. For an improvement, verify a baseline, the actual code/config change and a comparable rerun; note changed conditions and measurement limits. Do not invent numbers or describe a theoretical benefit as a measured speedup.

If evidence is missing, recommend an accurate qualification such as **정량 비교 없음** or **실행 근거 확인 불가**, or a safe future check. Do not silently rewrite historical records, manufacture evidence, or run a benchmark solely to validate a past-tense claim. New verification is labeled **이번 점검에서 재실행**. Change documents only when authorized.

## Safe scope

Use existing bounded local tests first. Do not automatically saturate CPU/RAM, flood requests, stop shared processes, or test external services. A new load/fault-injection test requires explicit authorization, an isolated permitted target, resource/time limits and a stop condition. If unavailable, report **부하·장애 실험 미검증** and inspect existing code/records instead.

Do not impose every check on every task. A small script does not need a distributed-system review. Do not publish task files or logs to the public hub or unapproved services.

## Short required output

```text
판정: 제출 가능 / 수정 필요 / 확인 불가
필수조건: 충족 N / 미충족 N / 미검증 N
실행 증거: [명령/사용자 흐름과 조건] → [실제 결과 또는 실행하지 못함]
상태·실패 경로: [확인한 전이·오류 처리 / 코드만 확인 / 미검증 / 해당 없음]
문서 주장 대조: [근거 확인 / 불일치 / 근거 확인 불가, 중요한 항목만]
사용자 결과 확인: [화면·파일에서 확인할 조건과 방법, 검증 범위의 한계]
핵심 문제: [파일·재현 조건·심각도, 없으면 '확인 범위에서 없음']
다음 행동: [가장 중요한 수정 또는 제출 전 확인]
```

State environment limitations and unknowns honestly. Do not rewrite the app just because another architecture looks cleaner. Explain documented choices and possible alternatives without presenting hypothetical trade-offs as tested results.
