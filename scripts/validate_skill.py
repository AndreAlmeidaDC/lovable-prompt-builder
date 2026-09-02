#!/usr/bin/env python3
"""Validate the Lovable prompt-builder skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE",
    "metadata.json",
    "framework_prompting.md",
    "security-checklist.md",
    "references/vibecode-core.md",
    "references/platform-lovable.md",
    "references/experience-sites.md",
    "references/accessibility-web.md",
    "references/archetypes.md",
    "references/version-check.md",
    "templates/PROJECT_KNOWLEDGE.md",
    "templates/EXPERIENCE_SPEC.md",
    "templates/ATOMIC_PROMPT.md",
    "templates/PRD.md",
    "templates/DATA_MODEL.md",
    "templates/USER_FLOW.md",
    "examples/exemplo_prompt_lovable.md",
    "examples/exemplo_site_experiencial.md",
]

FORBIDDEN_PATTERNS = {
    "wrong canonical repository": r"harness-engineering-coding-agent",
    "badge CSS workaround": r"#lovable-badge\s*\{",
    "obsolete ANPD incident deadline": r"72\s*h(?:oras)?(?:\s+à|\s+a)\s+ANPD",
    "unsupported vulnerability statistic": r"\b(?:89|34|28|22|18)%\s+dos\s+apps\b",
    "mandatory ai-summary file": r"(?:sempre|obrigat[oó]ri[oa]).{0,80}ai-summary\.md",
    "RLS on every table regardless of exposure": r"RLS\s+(?:ativad[oa]\s+)?em\s+TODAS\s+as\s+tabelas",
    "rigid competitor quota": r"(?:pesquise|pesquisar)\s+2\s+a\s+3\s+concorrentes",
    "accessibility disabled by default": r"acessibilidade.{0,60}(?:desligada|desativada)\s+por\s+padr[aã]o",
}

errors: list[str] = []
warnings: list[str] = []


def bundle_files() -> list[Path]:
    """Return files that would travel with the imported skill package."""

    ignored_parts = {".git", "__pycache__"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not ignored_parts.intersection(path.relative_to(ROOT).parts)
        and path.suffix.lower() != ".pyc"
        and path.name != ".DS_Store"
    ]


def read_text(rel: str) -> str:
    path = ROOT / rel
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"Missing required file: {rel}")
        return ""


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return {}
    try:
        _, block, _ = text.split("---", 2)
    except ValueError:
        errors.append("SKILL.md frontmatter is not closed")
        return {}

    result: dict[str, str] = {}
    current_key: str | None = None
    values: list[str] = []

    for raw in block.strip().splitlines():
        if re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:", raw):
            if current_key:
                result[current_key] = " ".join(values).strip()
            current_key, value = raw.split(":", 1)
            values = [value.strip()] if value.strip() not in {">", "|"} else []
        elif current_key and raw.startswith((" ", "\t")):
            values.append(raw.strip())
    if current_key:
        result[current_key] = " ".join(values).strip()
    return result


for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

metadata_text = read_text("metadata.json")
metadata: dict = {}
if metadata_text:
    try:
        metadata = json.loads(metadata_text)
    except json.JSONDecodeError as exc:
        errors.append(f"metadata.json is invalid JSON: {exc}")

required_metadata = [
    "name",
    "version",
    "origin_url",
    "origin_git_url",
    "update_policy",
    "family",
    "platform",
    "supported_project_modes",
    "execution_modes",
    "confirmation_required_for",
    "declared_capabilities",
]
for key in required_metadata:
    if key not in metadata:
        errors.append(f"metadata.json missing key: {key}")

if metadata.get("name") != "lovable-prompt-builder":
    errors.append('metadata.name must be "lovable-prompt-builder"')
if metadata.get("family") != "vibecode-prompt-builder":
    errors.append('metadata.family must be "vibecode-prompt-builder"')
if metadata.get("platform") != "Lovable":
    errors.append('metadata.platform must be "Lovable"')
if metadata.get("update_policy") != "version-check.md":
    errors.append('metadata.update_policy must be "version-check.md"')

name = str(metadata.get("name", ""))
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or not (1 <= len(name) <= 64):
    errors.append("metadata.name must use 1-64 lowercase letters, numbers and single hyphens")

version_value = str(metadata.get("version", ""))
if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", version_value):
    errors.append("metadata.version must use YYYY.MM.DD")

origin = metadata.get("origin_url", "")
parsed = urlparse(origin)
if parsed.scheme != "https" or parsed.netloc != "github.com":
    errors.append("metadata.origin_url must be an https://github.com URL")
if origin.rstrip("/") != "https://github.com/AndreAlmeidaDC/lovable-prompt-builder":
    errors.append("metadata.origin_url does not match the canonical repository")
if metadata.get("origin_git_url") != f"{origin.rstrip('/')}.git":
    errors.append("metadata.origin_git_url must match metadata.origin_url")

expected_modes = {
    "product-app",
    "experience-marketing-site",
    "existing-project-repair",
    "component-ui",
}
if set(metadata.get("supported_project_modes", [])) != expected_modes:
    errors.append("metadata.supported_project_modes is incomplete or contains drift")
if set(metadata.get("execution_modes", [])) != {
    "manual-prompt-bridge",
    "connected-lovable-tools",
}:
    errors.append("metadata.execution_modes must declare manual and connected operation")
required_confirmations = {
    "publish-or-deploy",
    "destructive-changes",
    "real-data-submission",
    "checkout-or-payment",
    "external-service-mutation",
}
if not required_confirmations.issubset(set(metadata.get("confirmation_required_for", []))):
    errors.append("metadata.confirmation_required_for is missing a safety boundary")

caps = metadata.get("declared_capabilities", {})
if not isinstance(caps, dict):
    errors.append("declared_capabilities must be an object")
else:
    for name in ("network_egress", "subprocess", "dependency_install"):
        entry = caps.get(name)
        if not isinstance(entry, dict):
            errors.append(f"declared_capabilities missing surface: {name}")
            continue
        if not isinstance(entry.get("expected"), bool):
            errors.append(f"declared_capabilities.{name}.expected must be boolean")
        if not str(entry.get("reason", "")).strip():
            errors.append(f"declared_capabilities.{name}.reason is required")

if caps.get("network_egress", {}).get("expected") is not True:
    errors.append(
        "network_egress.expected must be true because the workflow performs "
        "version checks and may research official docs/references"
    )

skill_text = read_text("SKILL.md")
frontmatter = parse_frontmatter(skill_text) if skill_text else {}
if frontmatter.get("name") != metadata.get("name"):
    errors.append("SKILL.md name must match metadata.name")
description = frontmatter.get("description", "")
if not description.lower().startswith("use when"):
    errors.append('SKILL.md description must start with "Use when"')
if "## Origin version check" not in skill_text:
    errors.append("SKILL.md must include Origin version check")
if "never self-update" not in skill_text.lower():
    errors.append("SKILL.md must forbid silent self-update")
if len(skill_text.splitlines()) > 180:
    warnings.append("SKILL.md is long; keep the entry point thin")
if len(skill_text) > 100_000:
    errors.append("SKILL.md exceeds Lovable's 100,000-character limit")

version = str(metadata.get("version", ""))
for rel in ("SKILL.md", "CHANGELOG.md"):
    text = read_text(rel)
    if version and version not in text:
        errors.append(f"{rel} does not mention metadata version {version}")

version_check = read_text("references/version-check.md")
if origin and origin not in version_check:
    errors.append("version-check.md must contain canonical origin fallback")
if "metadata.json" not in version_check:
    errors.append("version-check.md must derive canonical source from metadata.json")
if "Never execute" not in version_check and "never execute" not in version_check:
    errors.append("version-check.md must forbid executing downloaded code")

core = read_text("references/vibecode-core.md")
for phrase in (
    "Experience/Marketing Site",
    "Project Knowledge",
    "Ponte manual",
    "Execução conectada",
    "aceite humano",
):
    if phrase.lower() not in core.lower():
        errors.append(f"vibecode-core.md missing required concept: {phrase}")

platform = read_text("references/platform-lovable.md")
for phrase in (
    "Plan mode",
    "Agent mode",
    "Project Knowledge",
    "Design Guidance",
    "browser testing",
    "frontend-only",
    "submissão inicia o build",
):
    if phrase.lower() not in platform.lower():
        errors.append(f"platform-lovable.md missing current Lovable concept: {phrase}")

accessibility = read_text("references/accessibility-web.md")
for phrase in ("WCAG 2.2", "prefers-reduced-motion", "Canvas", "WebGL"):
    if phrase.lower() not in accessibility.lower():
        errors.append(f"accessibility-web.md missing: {phrase}")

security = read_text("security-checklist.md")
for phrase in ("3 dias úteis", "art. 19", "perfis", "RLS", "cinco anos"):
    if phrase.lower() not in security.lower():
        errors.append(f"security-checklist.md missing: {phrase}")

package_files = bundle_files()
all_text = "\n".join(
    p.read_text(encoding="utf-8")
    for p in package_files
    if p.suffix.lower() in {".md", ".json", ".yml", ".yaml"}
)
for label, pattern in FORBIDDEN_PATTERNS.items():
    if re.search(pattern, all_text, flags=re.IGNORECASE | re.DOTALL):
        errors.append(f"Forbidden pattern found: {label}")

# Validate repository-local Markdown references written as inline code.
local_ref_pattern = re.compile(
    r"`((?:references|templates|examples)/[^`\n]+\.md|"
    r"(?:security-checklist|framework_prompting|metadata)\.(?:md|json))`"
)
for doc in ROOT.rglob("*.md"):
    text = doc.read_text(encoding="utf-8")
    for rel in local_ref_pattern.findall(text):
        if not (ROOT / rel).is_file():
            errors.append(
                f"Broken local reference in {doc.relative_to(ROOT)}: {rel}"
            )

file_count = len(package_files)
total_size = sum(p.stat().st_size for p in package_files)
for p in package_files:
    if p.stat().st_size > 1_000_000:
        errors.append(f"Bundled file exceeds 1 MB: {p.relative_to(ROOT)}")
if file_count > 200:
    errors.append(f"Skill has {file_count} files; Lovable limit is 200")
if total_size > 10_000_000:
    errors.append(f"Skill is {total_size} bytes; Lovable package limit is 10 MB")

if warnings:
    print("Warnings:")
    for warning in warnings:
        print(f"- {warning}")

if errors:
    print("Validation failed:")
    for error in dict.fromkeys(errors):
        print(f"- {error}")
    sys.exit(1)

print(
    f"Validation passed. version={version} files={file_count} "
    f"size={total_size} bytes"
)
