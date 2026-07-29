---
name: yuanforge
description: "Establish, audit, repair, or evolve a trustworthy repository baseline for sustained Agent collaboration. Use when a Git-backed project needs six information responsibilities, a concise AGENTS.md/progress.txt/lessons.md context loop, verified Worktree guidance, or user-confirmed target intent before canonical documents are written. Do not use it for routine project work, domain execution, product design, or projects whose durable source of truth lives mainly outside the repository."
---

# YuanForge

Turn a Git repository into a maintainable operating baseline for people and Agents.

## Keep the promise finite

Use YuanForge for four operations:

- **Bootstrap:** create or map a missing repository baseline.
- **Audit:** compare the baseline with repository evidence and confirmed intent.
- **Repair:** fix confirmed baseline drift or missing ownership.
- **Evolve:** promote reviewed project evidence into durable guidance.

YuanForge governs the baseline. It does not perform domain work, implement features, design a product for the user, or infer desired behavior from code. When evidence requires capabilities YuanForge does not have, recommend a suitable Skill combination and continue in an accurately reduced mode.

Use YuanForge only when important artifacts, decisions, constraints, and verification evidence can be stored in or referenced from the repository. After bootstrap, let the repository's own guidance govern routine work.

## Build the baseline

Read [references/roles.md](references/roles.md) and [references/bootstrap.md](references/bootstrap.md) completely before creating or changing baseline artifacts.

Produce or map these information responsibilities:

```text
intent
workflow
methods
interaction
structure
delivery

AGENTS.md
progress.txt
lessons.md
docs/WORKTREE_GUIDE.md
```

Treat responsibilities as requirements, not filenames or empty templates. Reuse one canonical home for each lasting fact. Plan Worktree roles, but materialize only those needed by the current operation.

## Choose the project path

Read [references/intent-discovery.md](references/intent-discovery.md) whenever target intent is missing, incomplete, disputed, or still emerging.

- **New project:** treat links, slides, prototypes, notes, and conversation as inputs for discovering target intent. They do not prove current project behavior. Help the user surface intent, then record only confirmed decisions.
- **Existing project:** use code, tests, runtime results, data, artifacts, and Git history to establish current facts. Compare them with confirmed target documents and user decisions; do not infer the target from the implementation.
- **Mixed project:** classify each claim separately. Do not let abundant current evidence outweigh missing target authority.

The user does not need to know the complete intent in advance. Help it emerge through focused questions, alternatives, examples, or low-cost prototypes. The user retains authority over consequential choices and acceptance.

## Run the operation

### 1. Inspect

1. Run `git worktree list`, `git branch --show-current`, and `git status --short`.
2. Read repository instructions, `docs/WORKTREE_GUIDE.md`, `lessons.md`, `progress.txt`, and applicable stable specifications.
3. Search relevant code, tests, contracts, data, sources, artifacts, history, and user-provided materials.
4. Map evidence to the six responsibilities.
5. Separate current facts, confirmed target intent, proposed options, and unresolved questions.
6. Identify conflicts, dirty changes, path collisions, unsupported claims, and language drift.

Do not stop because expected filenames are absent. Recover facts from evidence and reuse existing canonical documents.

### 2. Resolve consequential unknowns

Read [references/readiness.md](references/readiness.md) when an answer could change scope, behavior, architecture, safety, authorization, data handling, acceptance, or Worktree topology.

Inspect before asking. Ask one high-value question at a time. Start from the user's situation, goal, and completion signal rather than asking them to pre-design documents or screens.

Do not write a proposed answer as confirmed target intent. When the user requests an early draft, label unresolved content `To confirm` and return `PARTIAL` or `BLOCKED` as appropriate.

### 3. Create or repair

Use [references/bootstrap.md](references/bootstrap.md) to:

- populate stable documents from current evidence and confirmed decisions;
- keep `AGENTS.md` concise and route details outward;
- maintain `progress.txt` as the current snapshot;
- record only reusable prevention rules in `lessons.md`;
- keep `docs/WORKTREE_GUIDE.md` aligned with actual topology;
- preserve dirty work and avoid duplicate sources of truth.

Present destructive or consequential choices before acting. Do not create target documents that encode unresolved consequential guesses.

### 4. Handle capability gaps

Read [references/capability-combinations.md](references/capability-combinations.md) only when required evidence cannot be inspected with current repository access.

- Recommend the smallest useful combination of existing Skills or tools.
- Do not make optional capabilities a YuanForge dependency.
- Do not claim installation or availability without verification.
- If the capability remains unavailable, state the missing evidence and continue as `PARTIAL` when safe.
- When another capability returns evidence, normalize it with [references/domain-evidence.md](references/domain-evidence.md); YuanForge keeps readiness and document-ownership authority.

### 5. Verify

Read [references/evidence.md](references/evidence.md) before claiming readiness.

Verify that:

- each lasting fact has one canonical home;
- document claims trace to repository evidence or confirmed intent;
- current facts, target intent, and proposals remain distinct;
- unresolved consequential questions are visible;
- relative links, commands, language, and defaults are valid;
- `AGENTS.md`, `progress.txt`, `lessons.md`, and Worktree guidance form a usable loop;
- actual Worktrees match documented materialized topology;
- dirty state and external unknowns are disclosed.

### 6. Hand off

Report artifacts changed or reused, Worktree state, verification, unresolved questions, capability gaps, and the normal start sequence for later tasks. Use `READY`, `PARTIAL`, or `BLOCKED`. A plan or plausible draft is not completion evidence.

## Evolve without drifting

Read [references/evolution.md](references/evolution.md) when promoting a correction or preference.

- Put current state in `progress.txt`.
- Put reusable failure prevention in `lessons.md`.
- Put stable intent, workflow, method, interaction, structure, or delivery decisions in the matching canonical specification.
- Put concise execution routing in `AGENTS.md` and Worktree behavior in `docs/WORKTREE_GUIDE.md`.

Do not mutate the global Skill from one project's preferences. Change the Skill kernel only through explicit review supported by cross-project evidence or a confirmed maintainer decision.
