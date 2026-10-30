#!/usr/bin/env python3
"""Package trusted HTML body + browser-ready CSS/JS; no installs or network.

Not a React/TS compiler, module bundler, sanitizer, or dependency resolver.
Referenced images/fonts/imports/APIs are not embedded or verified automatically.
"""
import argparse
import html
from pathlib import Path
import re
import sys


def package(body: Path, css: list[Path], js: list[Path], output: Path,
            title: str = "Web Artifact", lang: str = "ko") -> Path:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]{0,34}", lang):
        raise ValueError("Use a language tag such as ko or en-US.")
    content = body.read_text(encoding="utf-8")
    if not content.strip():
        raise ValueError("HTML body must not be empty.")
    if re.search(r"<!doctype\b|<\s*(?:html|head|body)\b", content, re.I):
        raise ValueError("--body expects an HTML body fragment, not a full document.")
    blocks = []
    for path in css:
        value = path.read_text(encoding="utf-8")
        if re.search(r"</style", value, re.I):
            raise ValueError(f"Unsafe closing style sequence in {path}; rewrite it first.")
        blocks.append("<style>\n" + value + "\n</style>")
    scripts = []
    for path in js:
        value = path.read_text(encoding="utf-8")
        if re.search(r"</script", value, re.I):
            raise ValueError(f"Unsafe closing script sequence in {path}; escape it first.")
        scripts.append("<script>\n" + value + "\n</script>")
    document = "\n".join([
        "<!doctype html>", f'<html lang="{lang}">', "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>" + html.escape(title) + "</title>", *blocks,
        "</head>", "<body>", content, *scripts, "</body>", "</html>", "",
    ])
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation: preserve any existing file, directory, or symlink.
    with output.open("x", encoding="utf-8") as stream:
        stream.write(document)
    return output.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--body", type=Path, required=True)
    parser.add_argument("--css", type=Path, action="append", default=[])
    parser.add_argument("--js", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", default="Web Artifact")
    parser.add_argument("--lang", default="ko")
    args = parser.parse_args()
    try:
        result = package(args.body, args.css, args.js, args.out, args.title, args.lang)
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created: {result}")
    print("Packaging only. Verify browser behavior and resource loading separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
