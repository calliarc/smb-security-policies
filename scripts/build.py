#!/usr/bin/env python3
"""Fill policy template placeholders from a company config and export them.

Usage:
    python3 scripts/build.py --config company.yml
    python3 scripts/build.py --config company.yml --formats md,docx,pdf --combined
    python3 scripts/build.py --list-placeholders

Reads policies/*.md, replaces {{KEY}} placeholders with values from the
config (YAML), strips "TEMPLATE NOTE" comments, and writes the results to
dist/. Markdown is always written. DOCX and PDF are written when Pandoc
(and, for PDF, a PDF engine) is installed; otherwise they are skipped with
a warning.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SRC = REPO_ROOT / "policies"
DEFAULT_OUT = REPO_ROOT / "dist"

PLACEHOLDER_RE = re.compile(r"\{\{\s*([A-Z0-9_]+)\s*\}\}")
TEMPLATE_NOTE_RE = re.compile(r"<!--\s*TEMPLATE NOTE:.*?-->\n*", re.DOTALL)
PDF_ENGINES = ("xelatex", "lualatex", "pdflatex", "wkhtmltopdf", "weasyprint", "typst")


class BuildError(Exception):
    """Raised for configuration or template problems."""


def _parse_simple_yaml(text: str) -> dict[str, str]:
    """Minimal fallback parser for flat `KEY: value` files (no PyYAML)."""
    data: dict[str, str] = {}
    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise BuildError(f"line {lineno}: expected 'KEY: value', got {raw!r}")
        key, value = line.split(":", 1)
        value = value.strip()
        if value and value[0] in "\"'":
            quote = value[0]
            end = value.rfind(quote)
            if end <= 0:
                raise BuildError(f"line {lineno}: unterminated quoted value")
            value = value[1:end]
            if quote == '"':
                value = value.replace('\\"', '"')
        else:
            value = value.split(" #", 1)[0].strip()
        data[key.strip()] = value
    return data


def load_config(path: Path) -> dict[str, str]:
    """Load a flat mapping of placeholder names to string values."""
    if not path.is_file():
        raise BuildError(f"config file not found: {path}")
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
    except ImportError:
        raw = _parse_simple_yaml(text)
    else:
        raw = yaml.safe_load(text) or {}
        if not isinstance(raw, dict):
            raise BuildError("config must be a mapping of KEY: value pairs")
    config: dict[str, str] = {}
    for key, value in raw.items():
        if isinstance(value, (dict, list)):
            raise BuildError(f"config key {key!r} must be a single value, not a list or mapping")
        config[str(key)] = "" if value is None else str(value)
    return config


def find_placeholders(text: str) -> set[str]:
    return set(PLACEHOLDER_RE.findall(text))


def strip_template_notes(text: str) -> str:
    return TEMPLATE_NOTE_RE.sub("", text)


def fill(text: str, config: dict[str, str]) -> tuple[str, set[str]]:
    """Replace known placeholders. Returns (new_text, unresolved_names)."""
    unresolved: set[str] = set()

    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        value = config.get(name)
        if value is None or value == "":
            unresolved.add(name)
            return match.group(0)
        return value

    return PLACEHOLDER_RE.sub(repl, text), unresolved


def pdf_engine() -> str | None:
    for engine in PDF_ENGINES:
        if shutil.which(engine):
            return engine
    return None


def pandoc_convert(src: Path, dest: Path, fmt: str, title: str, engine: str | None) -> None:
    # The first H1 becomes the document title, so drop it from the body to
    # avoid printing the title twice.
    body = re.sub(r"\A\s*# [^\n]*\n", "", src.read_text(encoding="utf-8"), count=1)
    cmd = ["pandoc", "--from", "markdown+task_lists-yaml_metadata_block", "--standalone",
           "--metadata", f"title={title}", "--output", str(dest)]
    if fmt == "pdf":
        cmd += ["--pdf-engine", engine or "pdflatex", "-V", "geometry:margin=2cm"]
    subprocess.run(cmd, input=body, check=True, capture_output=True, text=True)


def policy_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def build(config_path: Path, src_dir: Path, out_dir: Path, formats: list[str],
          strict: bool = False, combined: bool = False) -> dict[str, list[Path]]:
    config = load_config(config_path)
    sources = sorted(src_dir.glob("*.md"))
    if not sources:
        raise BuildError(f"no policy files found in {src_dir}")

    out_resolved, src_resolved = out_dir.resolve(), src_dir.resolve()
    if out_resolved in (REPO_ROOT, src_resolved) or out_resolved in src_resolved.parents:
        raise BuildError(f"refusing to use {out_dir} as output folder; it would delete sources")
    if out_dir.exists():
        shutil.rmtree(out_dir)
    md_dir = out_dir / "md"
    md_dir.mkdir(parents=True)

    written: dict[str, list[Path]] = {"md": [], "docx": [], "pdf": []}
    unresolved_all: dict[str, set[str]] = {}
    filled_docs: list[tuple[str, str]] = []

    for src in sources:
        text = strip_template_notes(src.read_text(encoding="utf-8"))
        filled, unresolved = fill(text, config)
        if unresolved:
            unresolved_all[src.name] = unresolved
        dest = md_dir / src.name
        dest.write_text(filled, encoding="utf-8")
        written["md"].append(dest)
        filled_docs.append((src.name, filled))

    if unresolved_all:
        lines = [f"  {name}: {', '.join(sorted(keys))}" for name, keys in unresolved_all.items()]
        msg = "unresolved placeholders (add them to your config):\n" + "\n".join(lines)
        if strict:
            shutil.rmtree(out_dir)
            raise BuildError(msg)
        print(f"warning: {msg}", file=sys.stderr)

    if combined:
        company = config.get("COMPANY_NAME", "Company")
        parts = []
        for _, doc in filled_docs:
            # Demote headings one level so each policy becomes a chapter.
            parts.append(re.sub(r"^(#+) ", r"#\1 ", doc, flags=re.MULTILINE))
        handbook = f"# {company} Information Security Policies\n\n" + "\n\n".join(parts)
        dest = md_dir / "security-policy-handbook.md"
        dest.write_text(handbook, encoding="utf-8")
        written["md"].append(dest)

    wanted = [f for f in formats if f in ("docx", "pdf")]
    if wanted:
        if not shutil.which("pandoc"):
            print("warning: pandoc not found; skipping DOCX/PDF (Markdown written to "
                  f"{md_dir})", file=sys.stderr)
            return written
        engine = pdf_engine()
        for fmt in wanted:
            if fmt == "pdf" and engine is None:
                print("warning: no PDF engine found (install a LaTeX distribution, "
                      "wkhtmltopdf, weasyprint or typst); skipping PDF", file=sys.stderr)
                continue
            fmt_dir = out_dir / fmt
            fmt_dir.mkdir(exist_ok=True)
            for md_file in written["md"]:
                title = policy_title(md_file.read_text(encoding="utf-8"), md_file.stem)
                dest = fmt_dir / (md_file.stem + "." + fmt)
                try:
                    pandoc_convert(md_file, dest, fmt, title, engine)
                except subprocess.CalledProcessError as exc:
                    print(f"warning: pandoc failed for {md_file.name} ({fmt}): "
                          f"{exc.stderr.strip()}", file=sys.stderr)
                    continue
                written[fmt].append(dest)
    return written


def list_placeholders(src_dir: Path) -> set[str]:
    names: set[str] = set()
    for src in sorted(src_dir.glob("*.md")):
        names |= find_placeholders(strip_template_notes(src.read_text(encoding="utf-8")))
    return names


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", type=Path, default=REPO_ROOT / "company.yml",
                        help="YAML file with placeholder values (default: company.yml)")
    parser.add_argument("--src", type=Path, default=DEFAULT_SRC, help="policy template folder")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output folder (replaced on each run)")
    parser.add_argument("--formats", default="md,docx,pdf",
                        help="comma-separated list from md,docx,pdf (default: all available)")
    parser.add_argument("--strict", action="store_true",
                        help="fail if any placeholder is left unresolved")
    parser.add_argument("--combined", action="store_true",
                        help="also produce a single handbook containing every policy")
    parser.add_argument("--list-placeholders", action="store_true",
                        help="print every placeholder used in the templates and exit")
    args = parser.parse_args(argv)

    if args.list_placeholders:
        for name in sorted(list_placeholders(args.src)):
            print(name)
        return 0

    formats = [f.strip().lower() for f in args.formats.split(",") if f.strip()]
    bad = [f for f in formats if f not in ("md", "docx", "pdf")]
    if bad:
        parser.error(f"unknown format(s): {', '.join(bad)}")

    try:
        written = build(args.config, args.src, args.out, formats,
                        strict=args.strict, combined=args.combined)
    except BuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    for fmt, files in written.items():
        if files:
            print(f"{fmt}: {len(files)} file(s) in {files[0].parent}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
