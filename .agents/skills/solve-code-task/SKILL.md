---
name: solve-code-task
description: Solve standalone coding logic, algorithms, small CLI tools, Python or JavaScript utility functions, parsing, validation, or file conversions. Use when the output is a correct function, script, or command rather than a UI or full service.
---

# Solve the contract, verify the boundaries

1. Identify input format, output format, constraints, required function signature and available runtime. Read any starter code/tests.
2. Build the simplest correct approach; state the core invariant or rule in a sentence. Consider runtime and memory only relative to actual constraints.
3. Implement while preserving the required interface and dependencies. Do not replace supplied entrypoints or test harnesses.
4. Check at least: normal sample, empty input, minimum/maximum or boundary value, duplicates/ties, invalid input if specified.
5. For tricky logic, compare small cases against a slow reference method or hand-worked examples. Prefer exact tests over 'looks right' assertions.
6. Run the project’s actual tests/CLI, inspect exit status/output, fix mismatches and rerun.
7. Explain the algorithm with the input→processing→output chain; mention complexity only when useful.

## Stop conditions

- Correct entrypoint and exact output shape.
- No debug prints corrupting machine-readable output.
- Test evidence available; untested cases explicitly labeled.
- No unnecessary framework, network dependency or speculative optimization.
