---
name: web-artifacts-builder
description: Create and deliver interactive web artifacts with Codex, including standalone HTML tools, dashboards, calculators, visual reports, and React app prototypes. Use when the user asks for a Claude-style artifact, browser-openable deliverable, interactive demo, or single-file HTML export. Preserve existing project requirements.
---

# Web Artifacts Builder — Codex

Create **real files the user can open and interact with**, not just code blocks or screenshots. This is a local web-artifact workflow, not a Claude API integration or an extension that adds a proprietary artifact panel to Codex.

## Choose the smallest suitable output

- **Existing project:** preserve its framework, package manager, lockfile, components and required output paths. Modify it in place; do not replace a required app with a separate HTML demo.
- **New small interactive tool/report:** prefer a self-contained `artifact.html` with inline CSS and browser-ready JavaScript. No npm install is needed for this path.
- **Complex app:** use the existing React/TypeScript/Vite setup when present, or initialize only the stack actually needed and permitted. Reuse installed Tailwind/shadcn components; do not install a full UI library by default.
- **Required backend/shared data/authentication:** implement that requirement. Browser storage or fake data is not a substitute. Label mock data as mock only when the task allows it.
- This skill is for **web artifacts**. It is not a PDF/DOCX/XLSX/PPTX exporter. For a normal page update where packaging is irrelevant, `build-web-ui` may be enough.

Skill paths below are relative to the directory containing this `SKILL.md`, not the user's working directory. Keep all generated output in the actual task/practice project, never in the public skill hub.

## 1. Define the result briefly, then implement

Read the task, existing source and runtime. Identify the intended user, essential interactions, data source, storage requirements and exact deliverable. Pick single HTML or the existing app; do not write a long design plan or ask for cosmetic approval before starting.

Build one complete flow first: input → validation → calculation/state update → visible result. Then complete remaining mandatory behavior. Use real values and derived totals, not hardcoded outputs presented as working features.

## 2. Make the artifact usable and presentable

- Choose a coherent typography, spacing and color system that fits the task and existing design. Use deliberate information hierarchy rather than a generic grid of decorative cards.
- Keep primary actions obvious; implement buttons, forms, tabs, filters and reset/export actions that are actually displayed.
- Include relevant empty, invalid-input, loading, success and error states. Ensure labels, keyboard focus, readable contrast and narrow-screen layouts.
- For interactive charts, maintain consistent data across charts, filters and summaries. Provide readable labels or a table when necessary.
- Prefer local assets/system fonts for offline or restricted environments. Avoid CDN scripts, remote fonts, analytics and external API dependencies unless explicitly permitted and needed.
- Handle imported/user data as data, not executable HTML; use safe text rendering. Catch storage failures where persistence is used and state its scope.

For a larger business workflow, use `build-app-workflow` only if its guidance is genuinely helpful. Do not force extra skills.

## 3. Produce the actual artifact

### A. Single HTML (no build dependency)

Write a complete HTML file directly, or keep a body fragment, stylesheet and **browser-ready classic JavaScript** separate during development and package them with the included utility:

```bash
# Set SKILL_DIR to the directory containing this SKILL.md.
python3 "$SKILL_DIR/scripts/package-artifact.py" \
  --body ./src/body.html --css ./src/styles.css --js ./src/app.js \
  --title "도구 이름" --lang ko --out ./dist/artifact.html
```

Paths are examples; use the task's actual paths. `--css` and `--js` are optional and may be repeated in execution order. The utility uses Python's standard library, does not contact the network, and **refuses to overwrite an existing output**. To revise, edit the artifact directly or write a new versioned output after reviewing the prior one. Do not blindly delete existing files.

**Utility limits:** it only wraps/inlines the supplied text. It does not compile JSX/TypeScript, resolve JavaScript imports, embed linked images/fonts, sanitize untrusted markup, or prove offline operation. Supply already browser-ready code; inspect resource requests separately. A complete HTML input should be used directly rather than passed as a body fragment.

### B. Existing React / framework app

Use the project's actual dev/build scripts and existing package manager. Implement components and real interactions first, then build. Keep source and the declared build output. Do not install Parcel or rewrite the build configuration merely because Anthropic's reference workflow does so.

If a **single-file export is specifically required**, use an available, compatible bundler/export method and verify the exported HTML separately from the dev server. A copied `dist/index.html` that still depends on JS/CSS files is **not** self-contained. If no suitable exporter is available, report the limitation rather than claim a single-file deliverable; keep working toward the actual requirement using permitted tools.

## 4. Preview and verify before declaring completion

For static HTML, serve only the output directory:

```bash
python3 -m http.server 3000 --bind 127.0.0.1 --directory ./dist
```

Use an available port. In a platform preview that requires it, use `--bind 0.0.0.0` and the platform's built-in preview with that exact port. Do not create public tunnels or expose the repository root, secrets, or unrelated files. Keep the server terminal alive while previewing.

For a framework app, use its prescribed dev/preview command and actual port.

Check the primary interaction, a failure/boundary case, reset/undo if present, narrow layout, keyboard access, and browser errors/resource failures. Where installed and permitted, use Playwright or another existing browser tool; do not install an MCP solely to follow this skill. If browser access is unavailable, state that limit: a successful build or packaging check is not UI verification.

For claimed standalone/offline output, open the **final artifact**, not only the dev app, and verify that its required resources and actions do not rely on missing files or forbidden network requests. Preserve backend requirements when offline is not the goal.

## 5. Deliver in Korean unless asked otherwise

Keep the handoff short:

```text
결과물: 실제 생성된 파일/프로젝트 경로
열기: 실제 실행 명령 + 포트/경로 또는 파일 열기 방법
사용법: 핵심 조작 1~3개
검증: 실제 실행한 테스트·브라우저 조작과 결과
한계: 미검증 항목, 외부 의존성, 저장 범위
```

Use file attachments or clickable local links only when the host actually supports them. Never invent sandbox links, hosted URLs, deployment success, or a native artifact preview. Use `review-result`/`explain-work` when useful, before any phase that prohibits AI.

## Reference and differences

Workflow reference: Anthropic's public `web-artifacts-builder`:
https://github.com/anthropics/skills/blob/main/skills/web-artifacts-builder/SKILL.md
Reviewed upstream blob: `8b39b19f259b4216ecb07574741dd8eaa9863a07`.

This skill and utility are newly authored for this hub, not copies of Anthropic's scripts or component archive. The upstream workflow uses React/TypeScript and single-HTML bundling; this version adds a zero-install HTML path, preserves existing stacks, and requires evidence before reporting success. No Claude account, personal API key, agent upgrade, remote MCP, or public upload is required by this skill.
