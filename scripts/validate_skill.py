from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    'SKILL.md',
    'README.md',
    'CHANGELOG.md',
    'CONTRIBUTING.md',
    'GOVERNANCE.md',
    'metadata.json',
    'references/version-check.md',
]
REQUIRED_SKILL_TERMS = [
    'Origin version check',
    'Never perform silent self-update',
]
REQUIRED_README_TERMS = [
    'Verificação de versão com consentimento',
]


def fail(message: str) -> None:
    print(f'FAIL: {message}')
    sys.exit(1)


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail('Missing required files: ' + ', '.join(missing))

    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    metadata_path = ROOT / 'metadata.json'

    if not skill.lstrip().startswith('---'):
        fail('SKILL.md must start with YAML frontmatter delimiter ---')

    if not re.search(r'^name:\s*.+$', skill, flags=re.MULTILINE):
        fail('SKILL.md frontmatter must include name')

    if not re.search(r'^description:\s*.+', skill, flags=re.MULTILINE):
        fail('SKILL.md frontmatter must include description')

    for term in REQUIRED_SKILL_TERMS:
        if term not in skill:
            fail(f'SKILL.md missing required term: {term}')

    for term in REQUIRED_README_TERMS:
        if term not in readme:
            fail(f'README.md missing required term: {term}')

    try:
        metadata = json.loads(metadata_path.read_text(encoding='utf-8'))
    except Exception as exc:
        fail(f'metadata.json is not valid JSON: {exc}')

    for key in ['name', 'version', 'origin_url', 'default_branch', 'update_policy']:
        if key not in metadata:
            fail(f'metadata.json missing key: {key}')

    policy = metadata.get('update_policy', {})
    if policy.get('requires_user_consent') is not True:
        fail('metadata.json update_policy.requires_user_consent must be true')

    if policy.get('silent_self_update_allowed') is not False:
        fail('metadata.json update_policy.silent_self_update_allowed must be false')

    print('Validation passed')


if __name__ == '__main__':
    main()
