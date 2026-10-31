---
name: review-result
description: Verify a deliverable against its own requirements and evidence. Select checks according to the actual task, material risks and claims rather than a fixed architecture or assessment pattern. Report missing behavior, incorrect outputs, unsupported claims and unverified items.
---

# Check this deliverable against this task

**Default: inspect, run bounded relevant checks, and report.** Fix only when requested, then rerun. Task solving remains the priority. Do not turn past assessment examples into mandatory checks, add features for a hypothetical exam, or require a benchmark or distributed-system review for every task.

## Derive the review from the task

1. Read the actual requirements, submission rules and supplied acceptance criteria. Identify the mandatory result, output paths/formats and what would make the result incorrect or unusable.
2. Inspect the deliverable and its supporting code/data/sources. Follow its main behavior or reasoning far enough to understand the result. Choose checks based on the requirements, material risks and claims actually made, not a preset list of technologies.
3. Use existing tests, build/CLI checks, representative inputs, browser interaction or source-to-conclusion checks as appropriate. Compare with an independently derived expected result or task-defined criterion where feasible. Distinguish static inspection from execution. A successful build or completed process does not by itself validate every property of the result.
4. Probe relevant boundaries, failure modes or weak assumptions when they could materially affect the task. State/ownership, concurrency, statistical assumptions, accessibility, security, output formatting and other concerns are possible topics, **not mandatory headings**. Do not invent components or new requirements to fit a review template.
5. Check important assertions in the deliverable and accompanying notes against the available evidence. Prioritize claims relevant to acceptance, user understanding or decisions; do not exhaustively audit irrelevant wording.
6. Mark mandatory items **passed / failed / not tested**. Prioritize blocking execution/output errors, wrong primary results and unmet requirements over optional polish. Report serious unsupported claims separately from proven functional failures.

## Evidence discipline

For a material claim, connect **주장 → 관련 구현·자료 → 확인 방법·조건 → 관찰 결과 → 주장 가능한 범위**. Source or a test definition is not an execution record. Missing records mean **근거 확인 불가**, not proof that no work occurred. Do not invent measurements, past actions or guarantees.

Only when performance or an improvement is required or claimed, inspect the relevant measurement conditions, actual results, baseline and comparability. Do not impose load testing on unrelated work. The same principle applies to any conclusion: its evidence must support the specific claim, not merely look technical.

If evidence is missing, recommend an accurate qualification or a proportionate future check. Do not silently rewrite history or manufacture proof. Label new verification **이번 점검에서 재실행** and change documents only when authorized.

## Scope and output

Use existing bounded local checks first. Do not automatically flood requests, exhaust resources, stop shared processes or test external services. A new disruptive load/fault test needs explicit authorization, an isolated permitted target, limits and a stop condition. Mention an untested area only when relevant; do not list every conceivable missing experiment as a defect.

Keep the report concise:

```text
판정: 제출 가능 / 수정 필요 / 확인 불가
필수조건: 충족 N / 미충족 N / 미검증 N
확인 근거: [실제로 확인한 내용·방법·조건·결과]
핵심 문제·한계: [요구사항 영향, 재현/근거, 불일치 또는 미검증]
다음 행동: [가장 중요한 수정 또는 제출 전 확인]
```

Add topic-specific detail only when it explains a material finding. Preserve the task's terminology and criteria. Do not rewrite the app for stylistic preference, publish task files/logs, or describe a hypothetical improvement as a measured result.
