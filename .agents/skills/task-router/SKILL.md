---
name: task-router
description: Choose relevant local solving skills for a new coding or practical task; when no skill fits, solve the task directly using the agent's normal reasoning, implementation, and verification abilities without searching for or inventing a skill.
---

# Choose only useful skills; otherwise solve directly

1. Read the actual task README, files, source, available commands, tests, required outputs, and time constraints.
2. Decide whether a local Skill **materially improves** solving this task. Use the following only as guides:
   - Interactive web artifact, standalone HTML, browser-openable tool or app demo → `web-artifacts-builder`
   - Web page, UI, form (without artifact packaging needs) → `build-web-ui`
   - CRUD, booking, stateful workflows → `build-app-workflow`
   - CSV/JSON cleaning or aggregation → `solve-data-task`
   - HTTP API/backend → `build-api`
   - Functions, algorithm, CLI utility → `solve-code-task`
   - Existing bug or broken project → `debug-existing-project`
   - Evidence-based written report → `write-work-document`
3. If useful: read **one** primary solving Skill; optionally one supplementary Skill. Apply only the relevant guidance; the task specification takes precedence.
4. **If no Skill is a good fit, or only part of one is useful:** do not treat it as a problem. **No fallback Skill is needed.** Solve the task using ordinary engineering judgment and built-in tools. Do **not** search for more Skills, invent a new Skill, configure MCPs, or stall just because no Skill matches.
5. **Always, with or without a Skill:**
   - Identify mandatory input/output, behavior, constraints, and observable completion criteria.
   - Inspect the existing project and reuse its stack and tools.
   - Implement the smallest **complete, working** result first, then required remaining details.
   - Run actual code/tests/preview; check normal and important failure/boundary cases.
   - Fix defects and rerun relevant checks. Mark unverified work honestly.
6. State only a concise plan if needed, then **start solving**. Do not spend time discussing the Skill selection.
7. Before submission, use `review-result` when useful. To help the user understand actual implementation and tests, use `explain-work` before any phase that prohibits AI.

**A Skill is optional assistance, not a prerequisite for solving.** Never force-fit tasks or collect tools for their own sake. Follow the assignment and environment rules; never transfer task materials to unapproved external systems.
