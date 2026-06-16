# Version check protocol

This reference defines how the skill checks its upstream source before meaningful use. It keeps local skill copies current without allowing silent or unsafe self-update. This is version 2 of the shared protocol used across this author's skills.

## Purpose

The skill may check whether a newer upstream version exists, read the public documentation, summarize the relevant changes and ask the user whether to update. The skill must never update itself silently.

## Canonical source

```text
https://github.com/AndreAlmeidaDC/harness-engineering-coding-agent
```

Default branch: `main`

## Version sources

Determine the local version using the first available source:

1. The `version` field in `metadata.json` inside the skill directory.
2. The Git commit hash of the local copy, when the local copy is a Git clone.
3. If neither is available, treat the local version as unknown and say so when asking about updates.

## Required behavior

At the start of a meaningful use, when network access and HTTP or Git tooling are available, perform the lightest safe check:

1. Read the local version from the sources above.
2. Retrieve the upstream version using the first check method that works (see below).
3. If the versions match, proceed silently. Do not mention the check.
4. If upstream is newer, read the upstream `CHANGELOG.md` and `README.md` when available.
5. Summarize the relevant changes in plain language.
6. Explain whether the changes may affect the current task.
7. Ask the user whether to update the local skill package before proceeding.

## Check methods

Use the first method that works in the current environment, in this order:

1. Plain HTTPS retrieval of the upstream `metadata.json`. Works in any environment with HTTP access and does not require Git:

```text
https://raw.githubusercontent.com/AndreAlmeidaDC/harness-engineering-coding-agent/main/metadata.json
```

2. GitHub API for the latest commit on the default branch:

```text
https://api.github.com/repos/AndreAlmeidaDC/harness-engineering-coding-agent/commits/main
```

3. `git ls-remote` when Git is available and only the remote commit hash is needed.
4. `git fetch` plus comparison when the local copy is a Git clone. Prefer non-destructive fetch. Never reset or pull without consent.

## Session cooldown rule

Run at most one upstream check per session or conversation. If the user declines an update, continue with the local version and do not raise the topic again in the same session unless the user asks.

## Consent rule

The agent must not overwrite local files, run update scripts, pull changes, reset branches, delete files or change the local skill package without explicit user approval.

A safe update question looks like this:

> Encontrei uma versão mais nova desta skill no repositório de origem. As principais mudanças são: [resumo]. Isso pode impactar a tarefa atual porque [impacto]. Você quer que eu atualize a cópia local da skill antes de continuar?

## Local changes rule

If the local skill directory has uncommitted changes, local-only files or a dirty working tree, the agent must report that before any update and ask for guidance. It must never discard local changes silently.

## Regression-free update rule

Treat the skill and its support files as an operational harness. Before recommending or applying an approved update, assess whether the upstream change preserves or improves explicit consent, transparency, verification quality and safety boundaries.

Flag any update as risky when it removes gates, weakens checks, reduces transparency, expands autonomy or changes this update protocol itself. Risky updates require an explicit user decision after the risk is explained in plain language.

## Update scope

When the user approves an update, update only the skill package and its support files. Do not modify the user's target project as part of the skill update unless the user separately approves that work.

## Failure modes

If the repository cannot be reached, network access is unavailable, no suitable tooling exists, rate limits block the check or the task is too small to justify the check, continue using the local version. When relevant, mention the limitation in the final response or handoff. The check is best effort and must never block the main task.

## Change history

| Date | Time | Protocol | Reason |
|---|---|---|---|
| 2026-06-10 | 19:15 GMT-3 | v2 | Unified protocol v2 across all skills: version source priority, HTTP and API check methods that work without Git, session cooldown rule, generalized regression-free update rule. |
| 2026-06-04 | 12:17 GMT-3 | v1.1 | Added regression-free improvement rule for update recommendations and approved self-updates (harness only). |
| 2026-06-02 | 09:02 GMT-3 | v1 | Added shared origin version check protocol requiring upstream comparison, summary of changes and explicit user consent before local skill updates. |
