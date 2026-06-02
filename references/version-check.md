# Version check protocol

This reference defines how the skill checks its upstream source before meaningful use. It exists to keep local skill copies current without allowing silent or unsafe self-update.

## Purpose

The skill may check whether a newer upstream version exists, read the public documentation, summarize the relevant changes and ask the user whether to update. The skill must never update itself silently.

## Canonical source

```text
https://github.com/AndreAlmeidaDC/lovable-prompt-builder
```

## Required behavior

At the start of a meaningful use, when internet access and Git or HTTP tooling are available, the agent should perform the lightest safe check:

1. Identify the local skill directory and read `metadata.json` when present.
2. Consult the upstream repository default branch.
3. Read upstream `README.md` and `CHANGELOG.md` when available.
4. Compare local and upstream versions using commit hash, release tag, changelog entry or file diff.
5. Summarize relevant changes in plain language.
6. Explain whether the changes may affect the current task.
7. Ask the user whether to update the local skill package before proceeding.

## Consent rule

The agent must not overwrite local files, run update scripts, pull changes, reset branches, delete files or change the local skill package without explicit user approval.

A safe update question looks like this:

> Encontrei uma versão mais nova desta skill no repositório de origem. As principais mudanças são: [resumo]. Isso pode impactar a tarefa atual porque [impacto]. Você quer que eu atualize a cópia local da skill antes de continuar?

## Local changes rule

If the local skill directory has uncommitted changes, local-only files or a dirty working tree, the agent must report that before any update and ask for guidance. It must never discard local changes silently.

## Failure modes

If the repository cannot be reached, network access is unavailable, Git is unavailable, rate limits block the check or the task is too small to justify the check, the agent may continue using the local version. When relevant, it should mention the limitation in the final response or handoff.

## Recommended check methods

Use the smallest method available for the environment:

| Method | When to use | Notes |
|---|---|---|
| `git fetch` + comparison | Local copy is a Git clone. | Prefer non-destructive fetch; never reset without consent. |
| `git ls-remote` | Need only remote commit hash. | Safe and lightweight. |
| Raw file retrieval | Need to read README/CHANGELOG without clone. | Use public raw URLs where possible. |
| Repository metadata | Need release or tag information. | Useful when GitHub CLI/API is available. |

## Update scope

When the user approves an update, update only the skill package and its support files. Do not modify the user's target project as part of the skill update unless the user separately approves that work.

## Change history

| Date | Time | Reason |
|---|---|---|
| 2026-06-02 | 09:02 GMT-3 | Added a shared origin version check protocol requiring upstream comparison, summary of changes and explicit user consent before local skill updates. |
