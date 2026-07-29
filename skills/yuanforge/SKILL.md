---
name: yuanforge
description: "Create, audit, repair, or evolve a repository-specific development baseline: six core specification roles, the persistent AGENTS.md/progress.txt/lessons.md context loop, a worktree guide, and role-based Git worktrees. Use when starting a project, onboarding an existing codebase, recovering missing context, correcting documentation drift, restructuring worktrees, or promoting evidence-backed project preferences and lessons into durable agent guidance. Do not use as the default workflow for routine feature implementation, bug fixing, or refactoring after the baseline is established."
---

# YuanForge

Turn a repository into a self-governing development environment. Build the baseline, verify it against repository evidence, then let the generated repository documents govern daily work.

## Keep the boundary

Use this skill for four operations:

- **Bootstrap:** create a missing baseline for a new or existing repository.
- **Audit:** compare an existing baseline with code, tests, contracts, migrations, Git state, and actual worktrees.
- **Repair:** update canonical documents or worktree structure when the baseline has drifted.
- **Evolve:** promote evidence-backed project preferences and lessons into the correct canonical documents.

Do not use this skill to accompany every feature, bug fix, refactor, or review. After bootstrap, agents should follow `AGENTS.md`, `progress.txt`, `lessons.md`, the stable specifications, and `docs/WORKTREE_GUIDE.md` directly.

## Build the baseline

Read [references/bootstrap.md](references/bootstrap.md) completely before creating or changing baseline artifacts.

Produce or map these information roles:

```text
docs/PRD.md
docs/APP_FLOW.md
docs/TECH_STACK.md
docs/FRONTEND_GUIDELINES.md
docs/BACKEND_STRUCTURE.md
docs/IMPLEMENTATION_PLAN.md

AGENTS.md
progress.txt
lessons.md
docs/WORKTREE_GUIDE.md

main
experiment
writing
agent-debug
```

Treat the filenames as defaults and the information roles as requirements. Reuse a canonical equivalent when one already exists; do not create duplicate sources of truth.

Preserve project individuality. Infer existing conventions from repository evidence before applying defaults. When asked to learn preferences or evolve the baseline, read [references/evolution.md](references/evolution.md) completely.

## Match the repository language

Choose the language of created or substantially rewritten project documents before writing them. Use this priority:

1. the user's explicit language instruction for the current operation;
2. an explicit repository language rule;
3. the dominant language of maintained canonical documents such as `AGENTS.md`, the README, and current specifications;
4. the language used by the user in the current conversation;
5. English only when no stronger signal exists.

Keep filenames, commands, code identifiers, protocol fields, and established technical terms unchanged when translation would reduce precision. Do not translate existing canonical documents merely for consistency unless the user requests it. When a repository intentionally uses different languages for different audiences, preserve that division.

Record an explicit, durable language preference in the appropriate concise project guidance; do not create a standalone language settings file. If evidence conflicts and the choice would cause a broad rewrite, ask one informed question before changing documents.

## Run the operation

### 1. Inspect

1. Run `git worktree list`, `git branch --show-current`, and `git status --short`.
2. Read applicable repository instructions and existing context files.
3. Determine the output language from explicit instructions and maintained repository evidence.
4. Search code, tests, contracts, schemas, migrations, configuration, documentation, and relevant history.
5. Map current evidence to every baseline role.
6. Identify conflicts, dirty changes, path collisions, unsupported claims, and unintended language drift.

Do not stop because expected filenames are absent. Recover facts from the repository, then create the requested canonical structure.

### 2. Resolve consequential unknowns

Read [references/readiness.md](references/readiness.md) when an unknown affects product scope, architecture, public behavior, safety, authorization, data, the stable baseline, or the worktree topology.

Inspect before asking. Ask one informed question at a time only when the answer is required to avoid encoding a consequential guess into the baseline.

### 3. Create or repair

Use [references/bootstrap.md](references/bootstrap.md) to:

- populate stable documents from current evidence;
- mark unsupported claims as `To confirm`;
- keep `AGENTS.md` concise and link outward;
- maintain `progress.txt` as a current snapshot;
- record only reusable prevention rules in `lessons.md`;
- make `docs/WORKTREE_GUIDE.md` match the actual topology;
- create or reuse worktrees without overwriting paths, moving dirty changes, or deleting branches.

Present conflicts or destructive choices before acting. Perform reversible, unambiguous creation that the user explicitly requested.

### 4. Verify

Read [references/evidence.md](references/evidence.md) before claiming the baseline is ready.

Verify:

- every baseline role has one canonical home;
- document claims trace to current repository evidence;
- relative links, commands, versions, and defaults are valid;
- `AGENTS.md`, `progress.txt`, and `lessons.md` form a usable reading and update loop;
- `git worktree list` matches `docs/WORKTREE_GUIDE.md`;
- all dirty states, unresolved conflicts, and external unknowns are disclosed.
- newly created prose follows the selected repository language without translating precision-sensitive identifiers.

### 5. Hand off

Report:

1. artifacts created, reused, updated, or left unresolved;
2. worktrees created or reused with exact paths and branches;
3. verification performed;
4. remaining `To confirm` items and blockers;
5. the normal start sequence for subsequent coding tasks.

Use `READY`, `PARTIAL`, or `BLOCKED`. A plan to create the baseline is not evidence that the baseline exists.

## Evolve without drifting

Do not mutate this global skill from one project's preferences. Evolve the repository baseline instead.

Classify new information before storing it:

- current task state belongs in `progress.txt`;
- reusable failure prevention belongs in `lessons.md`;
- stable product, technology, frontend, backend, or planning preferences belong in the matching specification;
- concise agent execution rules may be promoted to `AGENTS.md`;
- worktree behavior belongs in `docs/WORKTREE_GUIDE.md`.

Require evidence and an explicit, reviewable change before promoting a preference that alters future agent behavior. See [references/evolution.md](references/evolution.md).
