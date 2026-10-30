---
name: build-app-workflow
description: Implement small working business applications such as booking, to-do, inventory, inquiry, admin board, or CRUD workflows. Use when state transitions, validation, persistence, filtering, and end-to-end user actions matter more than appearance.
---

# Build an end-to-end workflow

**The primary output is a working user flow**, not a pretty static mockup.

1. List entities and actions from the actual requirement (e.g. record → create/edit/cancel/list/search). Note invariants and what data must persist.
2. Identify the existing stack, routes, storage mechanism and tests. Reuse them; do not invent a backend if client-side state is explicitly sufficient.
3. Implement one vertical slice first: input → validate → change data → persist as required → update UI → observe result.
4. Then add the remaining required actions and filters. Keep a single source of truth so badges/counts/tables update consistently.
5. Handle typical exceptions relevant to the spec: empty or invalid field, duplicate item, nonexistent ID, out-of-range quantity/time, canceled/deleted state.
6. Verify one successful end-to-end case plus at least one negative case per critical rule. Reload only if persistence is required. Use actual state rather than prefilled examples to demonstrate functionality.
7. Apply `build-web-ui` if visual quality or responsive layout is a substantial part of requirements.

## Decision points

- **Persistence:** memory, browser storage or server DB? Follow the task. Never silently replace required shared persistence with localStorage.
- **Concurrency:** if double-booking or conflicts matter, enforce at the authoritative update point, not by a disabled button alone.
- **Time/number:** state boundaries explicitly, e.g. whether adjacent reservations conflict, tax/rounding rules, inclusive/exclusive ranges.
- **Validation:** avoid inconsistent rules between forms and server-side actions.

## Ready-to-submit evidence

Mention actual successful and failed user actions, where the state is stored, and any rule not fully implemented. For a small assignment, a compact implementation plus working demonstrations beats optional architecture.
