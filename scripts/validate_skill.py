from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
required_files = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "metadata.json",
    "references/product-engineering-discovery.md",
    "references/prd-specification-builder.md",
    "references/semantic-system-design.md",
    "references/version-check.md",
    "references/release-measurement-loop.md",
    "references/squad-mode.md",
    "docs/academic-foundations.md",
    "templates/AGENTS.md",
    "templates/CONTRACT.md",
    "templates/SEMANTIC_SPEC.md",
    "templates/DECISION_GRILL.md",
    "templates/ACCEPTANCE_CRITERIA.md",
    "templates/TEST_PLAN.md",
    "templates/EVALUATION_REPORT.md",
    "templates/HANDOFF.md",
    "templates/STATE.md",
]

errors = []

skill = ROOT / "SKILL.md"
readme = ROOT / "README.md"
metadata_path = ROOT / "metadata.json"

if not skill.exists():
    errors.append("Missing SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    if "name: harness-engineering-coding-agent" not in text:
        errors.append("SKILL.md frontmatter must include the expected name")
    if "description:" not in text:
        errors.append("SKILL.md frontmatter must include description")
    if "## Origin version check" not in text:
        errors.append("SKILL.md must include Origin version check")
    if "Never perform silent self-update" not in text:
        errors.append("SKILL.md must explicitly prohibit silent self-update")
    if len(text.splitlines()) > 550:
        errors.append("SKILL.md should stay under 550 lines")

if readme.exists():
    readme_text = readme.read_text(encoding="utf-8")
    if "## Verificação de versão com consentimento" not in readme_text:
        errors.append("README.md must include consent-based version check section")
else:
    errors.append("Missing README.md")

if metadata_path.exists():
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"metadata.json is not valid JSON: {exc}")
    else:
        for key in ["name", "version", "origin_url", "default_branch", "update_policy"]:
            if key not in metadata:
                errors.append(f"metadata.json missing key: {key}")
        policy = metadata.get("update_policy", {})
        if policy.get("requires_user_consent") is not True:
            errors.append("metadata.json update_policy.requires_user_consent must be true")
        if policy.get("silent_self_update_allowed") is not False:
            errors.append("metadata.json update_policy.silent_self_update_allowed must be false")
else:
    errors.append("Missing metadata.json")

for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file: {rel}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
