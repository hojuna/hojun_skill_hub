---
name: explain-work
description: Explain actual implementation in Korean using source and execution evidence. Use for request flow, component responsibilities and states, design trade-offs and alternatives, failure behavior, test and performance claims, user-visible result quality, and optional independent explanation practice.
---

# Explain the actual work, not a plausible architecture

Help the owner understand and defend what was really built. **Solving remains the priority:** this is an explanation aid, not a new implementation or documentation ceremony. Apply only the lenses relevant to the task; do not invent components to fill a template.

## Ground the explanation first

Read the task, relevant source/configuration, available diffs, tests, execution outputs and submitted notes. Source shows implementation; observed runs show behavior; a document's claim is not proof of either. Distinguish **구현 확인 / 실행 확인 / 문서 주장·근거 미확인 / 추정·제안** where it matters.

Cite actual file paths and symbols, plus test/log locations or observed command results. Use line numbers only when checked. Missing records mean **확인 불가**, not proof that an action never happened. Do not invent numbers, historical decisions, commands, states or guarantees.

Default to reading and explaining. Do not launch load tests, modify code or rewrite documents just to produce an explanation. If the user requests verification, perform only scoped, permitted checks; label new runs as **이번 점검에서 재실행**, not historical evidence.

## Five explanation lenses

### 1. Request flow, responsibility and state

Trace one real user action from entry to final output in execution order, including handoffs, reads/writes, validation and how the result reaches the user. Distinguish request acceptance from actual completion.

For each component that exists, explain: **input → responsibility → output → owned state/data → next recipient**, with its actual file/function. Identify who owns state changes, who merely reads them, and when data becomes persistent. Use actual status names and transitions, not invented generic states. For asynchronous work, show how processing starts and how the user learns completion/failure. For a small script, a compact input/process/output chain is sufficient.

### 2. Design choice, trade-offs and alternatives

Choose the most consequential one or two decisions. Explain **requirement/constraint → chosen mechanism → useful benefit → cost/limitation**. State documented historical reasons separately from a present-day interpretation of why the choice fits.

Compare one or two viable alternatives when useful: how each would work, what code/infrastructure/state handling would change, and when it would be preferable. Previously unconsidered alternatives must be labeled **사후 비교·대안 제안**; never claim they were considered during implementation. Do not describe one approach as universally better.

Check guarantees in code/configuration. An architectural label alone does not establish bounded concurrency, retry, recovery, cancellation or duplicate prevention. Say which mechanisms actually exist and which are proposals.

### 3. Invalid input, failures and overload

Select realistic failure paths relevant to the implementation: malformed input, semantically invalid data, computation/validation errors, dependency failure, timeout, or excessive concurrent work. Trace **where detected → actual response/state → saved or partial results → what the user sees → recovery/retry, if implemented**.

Separate observed behavior from a static-code prediction. Check admission/concurrency limits and timeouts only where applicable. If overload or recovery was not tested, say so; never promise graceful rejection, automatic recovery or loss-free processing without evidence. Explain an unsafe/unhandled path as a limitation rather than an implemented safeguard.

### 4. Verification and improvement evidence

Audit claims such as 'tested', 'load-tested', 'faster' or 'robust' against available evidence. For each important claim, connect **claim → actual command/script → input and conditions → observed output/log → conclusion and limit**. A test file's existence is not evidence it ran.

For performance/load claims, look for the actual workload, concurrency or arrival rate, request count/duration, data size, environment/version, metric definition and results. Distinguish submission/acceptance latency from end-to-end completion; distinguish waiting from processing when relevant. Report only measured metrics; do not invent percentiles, throughput, error rates or thresholds.

For an improvement, show **observed bottleneck → exact change → same-condition recheck → before/after evidence → trade-off**. Flag changed workloads/environments and noncomparable runs. With no baseline, say **정량 비교 없음**; with code but no run, **구현 확인·실행 미검증**; with missing logs, **근거 확인 불가**. Do not turn a proposed optimization into a proven speedup. Surface important unsupported document claims instead of repeating them as facts.

### 5. How the user can judge the result

Explain which screen/file/report the user opens and the concrete steps to confirm the output matches the original request. Separate **request accepted**, **processing succeeded**, **specified constraints passed**, and **useful result quality**; do not infer all of them from one success indicator.

Use only task-defined or implemented checks: inspect important values, compare with a known expected example, check a validation report, or confirm output constraints, as applicable. Identify what any validator actually checks and does not check; passing it is not proof of optimality or domain usefulness. Mark additional quality criteria as proposals. Explain how the user sees failure, partial results, warnings and required corrective action.

## Default response: compact, evidence-linked Korean

Start with one sentence describing the deliverable. Give five short sections using the lenses above, about 2–4 sentences each, plus key source/test pointers. Expand only risky or unclear parts. If a lens does not apply, say so briefly. Prioritize explaining the system over listing files.

End with **핵심 한계·근거 부족** and three self-check questions targeting weak understanding or weak evidence. Do not generate a long report file unless requested or required. Leave the public hub unchanged and keep task-specific explanations in the task workspace/conversation.

## Optional question practice — only when requested

Generate six practice questions by default, based on actual work and evidence gaps, covering the applicable lenses. Label them **연습용 생성 질문**, not known assessment questions or a reconstruction of an unknown question. Do not promise a future evaluator will ask them.

Show questions without model answers. Let the user answer independently; do not reveal answer hints during the attempt. Afterwards, compare each answer with code and recorded evidence, pointing out correct claims, unsupported claims and omissions. Newly proposed alternatives are allowed if clearly distinguished from past actions.

If a follow-up assessment prohibits AI, use this skill only before that phase, or for permitted post-assessment review. Never assist during a prohibited live answering phase, manipulate question generation, fabricate logs, or publish protected assessment questions/answers or task materials to the public hub or external services.
