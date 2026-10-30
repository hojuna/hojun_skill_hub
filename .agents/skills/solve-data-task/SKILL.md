---
name: solve-data-task
description: Clean, transform, merge, analyze, or aggregate CSV, JSON, JSONL, or tabular files and create accurate summary outputs. Use for small data-processing tasks, data dashboards, reports, deduplication, date normalization, and log analysis.
---

# Correct data first, presentation second

1. Inspect real columns, sample rows, types, encodings, row counts and required output schema. Do not assume a toy sample represents the entire dataset.
2. Write a short transformation contract: accepted inputs; invalid-row policy; duplicate key/priority; missing values; dates/timezone; refunds/negative amounts; sort order; rounding.
3. Select the **simplest available tool**: Python standard library for basic CSV/JSON; pandas only if installed/appropriate; SQL if a database is supplied. Avoid unnecessary large packages and API calls.
4. Implement deterministic parsing and transformations. Never silently drop rows without reporting the policy/count; keep identifiers (zip codes, phone prefix, account-like fields) as strings where needed.
5. Test against a tiny hand-calculated fixture containing at least: normal row, empty/malformed row, duplicate, and one edge case for the main calculation.
6. Produce exactly the required file type, path, encoding and column order. Inspect the generated output and count/reconcile totals.
7. If a dashboard is requested, connect charts/filters to these verified aggregates, not separately hardcoded numbers.

## Important checks

- Number of input rows vs accepted/rejected/deduplicated/output rows.
- Aggregate counts and values reconcile with known sample.
- Date ranges and timezone assumptions explicit.
- Null, NaN, division by zero and negative numbers handled when applicable.
- Running again does not append duplicate results unless expressly required.
- No training/test leakage if a modeling task has data splits.

## Output to user

One-paragraph description of transformation, exact output path, two or three confirmed checks, and unresolved input assumptions. Do not fabricate statistics or claims of testing.
