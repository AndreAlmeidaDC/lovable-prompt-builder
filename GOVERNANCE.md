# Governance

This repository is maintained as an update-aware Agent Skill by **André Almeida**.

## Maintenance model

The skill is public and reusable, but changes should be treated as changes to agent behavior. The maintainer decides what enters the default branch and when a change should be released, tagged or documented as breaking.

## Consent and self-update policy

The skill may instruct an agent to check the upstream repository before meaningful use. That check is informational until the user approves an update.

The following actions require explicit user consent:

| Action | Consent required? |
|---|---:|
| Reading upstream README/CHANGELOG | No, if public and task-relevant. |
| Comparing local and upstream versions | No, if non-destructive. |
| Summarizing available changes | No. |
| Pulling, copying or overwriting local skill files | Yes. |
| Discarding local edits | Yes, and should normally be avoided. |
| Changing the user's target project because of a skill update | Yes, as a separate action. |

## Versioning

Use `CHANGELOG.md` as the human-readable source of release notes. Use Git tags when a version should be cited, installed or compared by other agents.

Recommended version labels:

| Label | Meaning |
|---|---|
| `draft` | Experimental and not recommended for broad reuse. |
| `beta` | Usable, but behavior may still change frequently. |
| `stable` | Suitable for recurring use. |
| `archived` | Preserved for history, not actively recommended. |

## Breaking changes

A change is breaking when it changes activation conditions, non-negotiable rules, user-consent behavior, required artifacts, output format, safety boundaries or update behavior in a way that may surprise existing users.

Breaking changes should be called out in `CHANGELOG.md` and, when appropriate, released with a new tag.

## Change history

| Date | Time | Reason |
|---|---|---|
| 2026-06-02 | 09:02 GMT-3 | Added governance rules for update-aware skill maintenance, explicit consent and release discipline. |
