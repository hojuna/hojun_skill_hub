---
name: explain-work
description: Help the user understand their actual work in Korean. Select explanation topics from the task, deliverable, consequential decisions, evidence and understanding gaps rather than a fixed checklist or past assessment questions. Offer independent question practice only when requested.
---

# Understand this work, not a question template

Help the owner explain what they actually made and why it satisfies the task. **Solving remains the priority.** This is an optional explanation aid, not an exam syllabus, a new implementation phase or a mandatory report.

## Ground the explanation

Read the actual requirements, relevant deliverable/source/configuration, available work history, tests, execution outputs and notes. Follow the supplied task's terminology and success criteria. Do not silently replace them with a generic architecture or assumptions about what an evaluator wants.

Distinguish implementation, observed execution, unsupported document claims and inference/proposals. Cite actual files/symbols, source sections or test/log locations where useful; use line numbers only when checked. Missing records mean **확인 불가**, not proof an action never happened. A test definition is not proof of execution. Do not invent commands, numbers, states, guarantees or historical decisions.

Default to reading and explaining. Do not edit the deliverable or launch new experiments solely to create a more impressive explanation. If verification is requested, label new runs **이번 점검에서 재실행**, not historical evidence.

## Choose topics from the work itself

1. Identify what the user was asked to achieve and what was actually produced.
2. Find the parts most important to understanding that result: consequential choices, non-obvious reasoning, difficult changes, assumptions that affect correctness, or claims whose evidence is unclear.
3. Select only the topics that matter for this deliverable and the user's current understanding. Prefer a small number of meaningful explanations over exhaustive coverage. Do not force a fixed number of sections or questions.
4. Explain each chosen point with its actual mechanism or reasoning, connection to the requirement, supporting evidence and relevant limits. Use a worked example or input-to-output trace when it clarifies the point; do not impose a component diagram on every task.
5. Notice important topics not suggested by any example list. If the user reveals confusion, clarify that part rather than repeating a preset report.

A web interaction might need a state-flow explanation; a data analysis might need its aggregation assumptions; a small algorithm might need an invariant; a written proposal might need its source-to-conclusion reasoning. These are **illustrations, not required categories or predicted questions**. Architecture, failures, performance, user experience, AI collaboration, alternative methods or any other topic belong only when supported by this task, its risks, records or the user's request.

Past question examples illustrate possible depth of understanding; they do not establish future topics, probabilities, scoring weights, a required architecture or a fixed question count. Do not reconstruct, publish or drill a protected assessment question set.

## Keep useful lessons without turning them into a checklist

- Explain important choices against actual constraints, including costs or limitations when relevant. Separate documented historical reasons from present-day interpretation. A new alternative is **사후 비교·대안 제안**, not something supposedly considered earlier.
- Match claims to evidence. A claim about accuracy needs appropriate correctness evidence; a claim about speed needs actual measurements under stated conditions. Do not demand performance benchmarks for work that neither requires nor claims performance improvement.
- Where a comparison is claimed, check the baseline and comparability. Say **정량 비교 없음** or **근거 확인 불가** when appropriate, rather than inventing a benefit.
- Where behavior is described, distinguish observed behavior from static inspection or prediction. A technology's name is not evidence that a particular safeguard exists.
- Explain how the result satisfies the task's real success criteria. A completed process, polished appearance or passing test need not prove every claimed property. Do not add unrequested quality standards as mandatory requirements.

## Response and optional practice

Respond in clear Korean. Start with a brief account of the goal and actual result, then explain the selected important points at a useful depth with source pointers. Mention material uncertainties or understanding gaps. Omit irrelevant topics entirely; do not fill sections with '해당 없음'. No fixed section layout, question count or exhaustive file inventory is required. Do not create a long document unless requested.

Only when requested, generate **연습용 생성 질문** from the current work, meaningful decisions and understanding gaps. Follow the user's requested length or count; otherwise keep the set small and relevant. Do not copy past question patterns, imply known future exam questions, or insist on one question per category. A changed assumption can be explored when it helps test understanding, clearly as a hypothetical rather than an implemented feature.

For independent practice, show questions without answers or hints. After the user answers, compare the response with actual evidence, explain inaccuracies and omissions, and adapt follow-up questions to the user's understanding. Do not reward an answer merely for matching a memorized phrasing.

Keep task-specific explanations in the task workspace/conversation, not the public hub. Follow assessment rules: never assist during a phase that prohibits AI, manipulate question generation, fabricate records or publish protected task materials. Use this skill before such a phase or for permitted post-assessment review.
