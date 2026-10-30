---
name: task-router
description: Select relevant local skills after reading the assignment README and project. Use for web pages, CRUD apps, CSV/JSON, APIs, debugging, CLI logic or document work, and route unsupported or incompatible tasks to resolve-skill-gap.
---

# Task router: small and useful

1. Read the actual task README, file tree, existing code, tests and completion criteria **before choosing skills**.
2. Identify the main deliverable and required operations. Assess skill fit by capabilities, output format, stack and permitted tools, not task-name similarity alone.
3. Use this routing table (read the selected SKILL.md, not all files):
   - Visual website, landing page, form → `build-web-ui`
   - CRUD, booking, dashboard interactions, saved state → `build-app-workflow`
   - CSV/JSON/data cleaning, aggregation → `solve-data-task`
   - HTTP API/server/backend → `build-api`
   - Algorithms, scripts, utility functions, CLI → `solve-code-task`
   - Existing bug, failing tests, broken build → `debug-existing-project`
   - Research using supplied material, summary, proposal → `write-work-document`
4. Decide the route:
   - **Suitable match:** read one primary solving skill. Add one complementary skill only if necessary.
   - **Partial match, no match, or incompatible/unavailable tool:** read `../resolve-skill-gap/SKILL.md` relative to this file, then follow its decision. Do not force-fit a skill or stop at 'no matching skill'.
5. For interface-heavy CRUD tasks, use `build-app-workflow` first and `build-web-ui` as a focused secondary skill. For a data dashboard, solve data correctness first.
6. State in 2–3 lines what must work, the chosen route and first validation; start implementation promptly. A no-skill DIRECT route is valid.
7. Once implemented, use `review-result` for actual validation; use `explain-work` when the user needs to understand the work.

Resolve sibling skill paths from the directory containing this SKILL.md, not blindly from the current working directory. Never run every skill, force a stack migration, or recursively install dependencies. Public reference discovery is conditional and bounded by `resolve-skill-gap`; it must not export task content. Do not re-enter routing for the same gap.
