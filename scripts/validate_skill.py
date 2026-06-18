#!/usr/bin/env python3
"""
Local validator for vibecode-prompt-builder family skills.

Checks structural integrity before a commit or PR:
- required files exist
- SKILL.md has valid frontmatter, the expected name, a description and the
  origin version check section
- metadata.json is valid JSON with the expected keys and values for this family
- the platform reference declared in metadata is present

Run from the repo root or via: python3 scripts/validate_skill.py
Exits 0 when valid, 1 when any check fails.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "LICENSE",
    "metadata.json",
    "references/vibecode-core.md",
    "references/archetypes.md",
    "references/version-check.md",
    "templates/PRD.md",
    "templates/DATA_MODEL.md",
    "templates/USER_FLOW.md",
]

errors = []
warnings = []

metadata_path = ROOT / "metadata.json"
skill = ROOT / "SKILL.md"
readme = ROOT / "README.md"

# metadata.json
metadata = {}
if metadata_path.exists():
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"metadata.json is not valid JSON: {exc}")
else:
    errors.append("Missing metadata.json")

expected_name = metadata.get("name", "")

if metadata:
    for key in ["name", "version", "origin_url", "update_policy",
                "family", "platform", "declared_capabilities"]:
        if key not in metadata:
            errors.append(f"metadata.json missing key: {key}")

    if metadata.get("family") != "vibecode-prompt-builder":
        errors.append('metadata.json family must be "vibecode-prompt-builder"')

    if metadata.get("update_policy") != "version-check.md":
        errors.append('metadata.json update_policy must be "version-check.md"')

    caps = metadata.get("declared_capabilities", {})
    if isinstance(caps, dict):
        for surface in ["network_egress", "subprocess", "dependency_install"]:
            entry = caps.get(surface)
            if not isinstance(entry, dict):
                errors.append(f"declared_capabilities missing surface: {surface}")
            elif entry.get("expected") is not False:
                errors.append(
                    f"declared_capabilities.{surface}.expected must be false "
                    "(this is a prompt-generation skill)"
                )
    else:
        errors.append("declared_capabilities must be an object")

# SKILL.md
if not skill.exists():
    errors.append("Missing SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    if expected_name and f"name: {expected_name}" not in text:
        errors.append(
            f"SKILL.md frontmatter name must match metadata name ({expected_name})"
        )
    if "description:" not in text:
        errors.append("SKILL.md frontmatter must include description")
    if "## Origin version check" not in text:
        errors.append("SKILL.md must include the Origin version check section")
    if "never self-update" not in text.lower():
        warnings.append("SKILL.md should state that it never self-updates silently")
    if len(text.splitlines()) > 200:
        warnings.append(
            "SKILL.md is over 200 lines; vibecode entry points are meant to be thin "
            "(process lives in references/vibecode-core.md)"
        )

# platform reference declared in metadata must exist
platform = metadata.get("platform", "")
platform_map = {
    "Lovable": "platform-lovable.md",
    "bolt.new": "platform-bolt.md",
    "v0 (Vercel)": "platform-v0.md",
    "a0.dev": "platform-a0dev.md",
    "Base44": "platform-base44.md",
    "emergent.sh": "platform-emergent.md",
}
expected_ref = platform_map.get(platform)
if expected_ref:
    if not (ROOT / "references" / expected_ref).exists():
        errors.append(f"Missing platform reference for {platform}: references/{expected_ref}")
else:
    refs = list((ROOT / "references").glob("platform-*.md")) if (ROOT / "references").exists() else []
    if not refs:
        errors.append("No platform-*.md reference found in references/")

if not readme.exists():
    errors.append("Missing README.md")

for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file: {rel}")

if warnings:
    print("Warnings:")
    for w in warnings:
        print(f"- {w}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
