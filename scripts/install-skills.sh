#!/usr/bin/env bash
set -euo pipefail

# Copy-only installer: no network, no deletion, no overwrite.
SOURCE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)/.agents/skills"
TARGET_PROJECT="${1:-$PWD}"
TARGET_DIR="${TARGET_PROJECT%/}/.agents/skills"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Missing source skills directory: $SOURCE_DIR" >&2
  exit 1
fi
if [[ ! -d "$TARGET_PROJECT" ]]; then
  echo "Target project does not exist: $TARGET_PROJECT" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
for skill in "$SOURCE_DIR"/*; do
  [[ -d "$skill" ]] || continue
  name="${skill##*/}"
  if [[ -e "$TARGET_DIR/$name" ]]; then
    echo "SKIP (already exists): $name"
  else
    cp -R "$skill" "$TARGET_DIR/$name"
    echo "INSTALLED: $name"
  fi
done
echo "Skills copied to: $TARGET_DIR"
echo "If not auto-discovered, ask your agent to read START_HERE.md and the selected SKILL.md directly."
