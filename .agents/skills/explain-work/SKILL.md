---
name: explain-work
description: Explain an implemented project in simple Korean from actual source, commits, and test results. Use when the user needs to understand how it works, what was verified, why choices were made, and what could be improved before an independent oral or written explanation.
---

# Make the implementation understandable to its owner

Read the real task, relevant source and actual test/command results first. **Do not infer actions that did not happen.** Keep the explanation short enough to absorb before an interview or review.

## Output structure (default ~10–20 lines)

1. **한 문장 요약:** 무엇을 해결했나?
2. **동작 흐름:** 입력 → 핵심 처리 → 저장/출력 (쉬운 말로).
3. **핵심 파일·함수:** 실제 경로와 역할을 2–4개.
4. **선택 이유:** 왜 이 구현이 요구사항에 적합했나? 대안은 실제 고려한 경우에만 언급.
5. **검증:** 정확히 어떤 명령·화면 조작·입력으로 무엇을 확인했나?
6. **수정·개선:** 실제로 고친 것과 전후 근거. 비교 실험이 없으면 '정량 비교 없음'.
7. **한계:** 미구현, 미검증, 확장 시 주의할 점을 명확히.

## Understanding check

Finish with **three short self-check questions** based on the actual work, e.g.:
- 이 함수가 값을 잘못 받으면 어떻게 되나?
- 어떤 테스트가 해당 규칙을 확인했나?
- 지금 결과물이 보장하지 못하는 것은 무엇인가?

The user must be able to answer in their own words. If a task's follow-up phase prohibits AI, **only use this skill before that phase** and do not prepare or inject prohibited live answers.
