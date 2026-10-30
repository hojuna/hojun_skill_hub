---
name: task-router
description: Select relevant local skills for a new task after reading the assignment README and project. Use when an agent needs to decide which skill to use for web pages, CRUD apps, CSV/JSON, APIs, debugging, CLI logic, or document work.
---

# Task router: small and useful

1. Read the actual task README, file tree, existing code, tests and completion criteria **before choosing skills**.
2. Identify the main deliverable and choose **one** primary solving skill. Choose one additional skill only if a second capability is clearly necessary.
3. Use this routing table (read the selected SKILL.md, not all files):
   - Visual website, landing page, form → `build-web-ui`
   - CRUD, booking, dashboard interactions, saved state → `build-app-workflow`
   - CSV/JSON/data cleaning, aggregation → `solve-data-task`
   - HTTP API/server/backend → `build-api`
   - Algorithms, scripts, utility functions, CLI → `solve-code-task`
   - Existing bug, failing tests, broken build → `debug-existing-project`
   - Research using supplied material, summary, proposal → `write-work-document`
4. For interface-heavy CRUD tasks, use `build-app-workflow` first and `build-web-ui` as a focused secondary skill. For a data dashboard, solve data correctness first.
5. State in 2–3 lines what must work and why the selected skill fits; start implementation promptly.
6. Once implemented, call `review-result` for actual validation; use `explain-work` only if the user needs to understand the work.
7. If no skill fits, use normal engineering workflow. **Do not force-fit a skill.**

Never run every skill, recursively install dependencies, or contact external services merely to discover skills. The assignment rules and original project requirements take priority.
