---
name: build-web-ui
description: Build or improve a usable, responsive website, landing page, dashboard view, or frontend form. Use when a task requires an actual web UI, visual layout, interaction, accessibility, and browser-based verification.
---

# Build a working web UI

Use for **visual/front-end deliverables**. If the core problem is records, workflows, or persistence, pair with `build-app-workflow`.

## Workflow

1. Inspect the existing app, framework, package scripts, styles, assets and exact assignment deliverables. **Preserve the supplied stack.** Do not start an unnecessary rewrite.
2. Translate requirements into visible sections, navigation and essential interactions. Distinguish **real functionality** from presentational decoration. Use supplied brand/content assets when provided.
3. Choose a concise visual system: background/surface/accent, readable typography, spacing rhythm, layout widths and mobile breakpoint. Prefer coherent simple UI over an elaborate untested design.
4. Build a functioning first pass: proper headings, information hierarchy, functional buttons/links/forms and explicit loading/success/error/empty states where relevant.
5. Wire interactions to the actual state and data source. Never leave a fake submit, inert CTA or hardcoded success state unless the task explicitly asks for a static mockup.
6. Verify: run the prescribed build command; start the local server; open the actual page in the provided preview; test the main action, bad input, a narrow viewport, and navigation. If browser automation is already available and permitted, use it for repeated interactions.
7. Fix critical bugs before polishing nonessential details.

## Quick verification checklist

- Primary path reaches a meaningful end state.
- No broken navigation or fake action controls.
- Labels, keyboard focus, contrast, and basic mobile layout work.
- Values/data visible in charts or cards are derived from actual required source.
- Build/runtime errors addressed, page opens at the **actual** server port.
- Report what was tested and what could not be tested.

For preview environments requiring it, bind the server to `0.0.0.0` using the real port. Use the platform's embedded browser. Do not expose private data or open public tunnels.

## Avoid

- Replacing an existing framework just for appearance.
- Using generic placeholder copy instead of user-provided requirements.
- Spending all time on animation while essential interactions are unfinished.
- Claiming responsive/browser validation if only a build check ran.
