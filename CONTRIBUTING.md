# Contributing

## How to contribute

1. Fork the repository
2. Make your changes in a branch
3. Run `python3 scripts/validate_skill.py` to validate locally
4. Open a pull request with a clear description of what changed and why

## What belongs where

- Shared process improvements → `references/vibecode-core.md`
- Lovable-specific improvements → `references/platform-lovable.md`
- Platform choice guidance → `references/archetypes.md`
- Entry point changes → `SKILL.md` (keep it thin — role + load instructions only)

## Version bump

After any meaningful change, update `metadata.json` version and add a row to `CHANGELOG.md`.
