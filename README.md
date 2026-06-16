# lovable-prompt-builder

Vibecode skill for **Lovable** — part of the `vibecode-prompt-builder` family.

## What it does

Vibecode skill for building full-stack web apps with Lovable.dev. Guides the user through intake, branding, LGPD compliance and atomic prompt generation with feedback loop.

## How to use

1. Load this skill in your LLM chat (Claude, ChatGPT, etc.)
2. The skill will guide you through: intake → data modeling → branding → validation → prompt generation → feedback loop
3. Each prompt is delivered one at a time; paste it into Lovable and return the result

## Structure

```
SKILL.md                        # Entry point: role and how to use
references/
  vibecode-core.md              # Shared process (all vibecode skills)
  platform-lovable.md                 # Lovable-specific details
  archetypes.md                 # Platform choice guide
  version-check.md              # Auto-update protocol
templates/
  PRD.md                        # Product requirements template
  DATA_MODEL.md                 # Data model template
  USER_FLOW.md                  # User flow template
scripts/
  validate_skill.py             # Local validation script
```

## Family

This skill is part of the `vibecode-prompt-builder` family:
- [lovable-prompt-builder](https://github.com/AndreAlmeidaDC/lovable-prompt-builder)
- [bolt-prompt-builder](https://github.com/AndreAlmeidaDC/bolt-prompt-builder)
- [v0-prompt-builder](https://github.com/AndreAlmeidaDC/v0-prompt-builder)
- [a0-prompt-builder](https://github.com/AndreAlmeidaDC/a0-prompt-builder)
- [base44-prompt-builder](https://github.com/AndreAlmeidaDC/base44-prompt-builder)

The shared process lives in `references/vibecode-core.md`.

## License

MIT — André Almeida
