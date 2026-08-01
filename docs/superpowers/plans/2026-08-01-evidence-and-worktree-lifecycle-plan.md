# Evidence and Worktree Lifecycle Gates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task with review checkpoints.

**Goal:** Prevent candidate or uncommitted repository work from being reported as stable completion, and give every materialized Worktree an auditable integration or retirement decision.

**Architecture:** Keep Git as the source of Worktree, branch, commit, and ancestry facts. Add a focused `integration-readiness.md` reference for lifecycle and responsibility boundaries, wire it into the existing YuanForge inspection/evidence/hand-off flow, and keep project-specific commands in `docs/WORKTREE_GUIDE.md`. Extend contract tests and eval cases to lock the two failure modes without adding a second state database or an automatic merge/delete command.

**Tech Stack:** Markdown Skill/reference documents, JSON eval fixtures, Python `unittest`, Git Worktree commands, `quick_validate.py`.

## Global Constraints

- Natural-language repository guidance remains Chinese; filenames, commands, branch names, and stable status tokens remain unchanged.
- `[Done]` and `READY` require stable-branch inclusion plus fresh applicable verification.
- `READY_FOR_REVIEW` is evidence readiness, not maintainer authorization.
- Dirty Worktrees are preserved; no automatic merge, Stash, branch deletion, or Worktree deletion.
- A clean committed candidate may be parked by removing its Worktree while retaining its branch.
- Do not touch other repositories or their uncommitted Worktrees.

---

### Task 1: Add failing contract and eval coverage

**Files:**
- Modify: `tests/test_repository_contract.py`
- Modify: `evals/cases.json`

**Interfaces:**
- Tests consume the Skill and reference text by repository-relative paths.
- Eval cases expose the stable IDs `candidate-evidence-cannot-be-done` and `worktree-lifecycle-review`.

- [ ] **Step 1: Add the candidate-evidence eval fixture**

Append an `audit`/`software` case whose fixture contains an untracked progress snapshot, dirty experiment code, a candidate branch, and a stable branch without the change. Its expected output must require `READY_FOR_REVIEW` or `CONTINUE`, explicit stable-branch evidence, and rejection of `[Done]`/`READY` claims.

- [ ] **Step 2: Add the Worktree lifecycle eval fixture**

Append an `audit`/`software` case containing a dirty experiment, a clean committed unmerged candidate, an integrated branch, and a superseded branch. Its expected output must require `CONTINUE`, `SPLIT`, `PARK`, `RETIRE`, or `BLOCKED`, preserve dirty work, and separate merge authorization from Git execution.

- [ ] **Step 3: Add contract assertions for the new cases and references**

Add tests that:

```python
def test_integration_readiness_cases_are_recorded(self):
    cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
    by_id = {case["id"]: case for case in cases}
    for case_id in ("candidate-evidence-cannot-be-done", "worktree-lifecycle-review"):
        self.assertIn(case_id, by_id)
        self.assertEqual("audit", by_id[case_id]["operation"])
        self.assertGreaterEqual(len(by_id[case_id]["expected"]), 5)
```

Add a second assertion that the Skill references `integration-readiness.md`, and that the reference includes `READY_FOR_REVIEW`, `PARK`, `RETIRE`, `BLOCKED`, and the prohibition on automatic merge/delete.

- [ ] **Step 4: Run the focused tests and verify RED**

Run:

```powershell
python -m unittest tests.test_repository_contract.RepositoryContractTests.test_integration_readiness_cases_are_recorded -v
```

Expected result before the documentation changes: FAIL because the new cases and reference do not yet exist. If the test errors for a fixture or syntax mistake, correct the test and rerun until it fails for the missing behavior.

- [ ] **Step 5: Commit the RED coverage**

```powershell
git add tests/test_repository_contract.py evals/cases.json
git commit -m "test: guard evidence and worktree promotion claims"
```

### Task 2: Implement the Skill evidence and lifecycle rules

**Files:**
- Create: `skills/yuanforge/references/integration-readiness.md`
- Modify: `skills/yuanforge/SKILL.md`
- Modify: `skills/yuanforge/references/evidence.md`
- Modify: `skills/yuanforge/references/bootstrap.md`

**Interfaces:**
- `SKILL.md` routes inspection and hand-off to `references/integration-readiness.md`.
- `evidence.md` defines the persistence/ownership/verification dimensions used by completion claims.
- `bootstrap.md` requires a unique Worktree objective, stable base, and exit condition before materialization.

- [ ] **Step 1: Add the minimal lifecycle reference**

Create `integration-readiness.md` with these exact sections and stable tokens:

1. `## 适用范围`
2. `## 三维证据模型` — worktree/commit durability, candidate/stable ownership, unverified/verified evidence.
3. `## Worktree 生命周期` — `planned`, `active`, `candidate`, `parked`, `integrated`, `retired`.
4. `## 审计判断` — `CONTINUE`, `SPLIT`, `READY_FOR_REVIEW`, `PARK`, `RETIRE`, `BLOCKED`.
5. `## 集成责任边界` — readiness, maintainer approval, Git execution, stable verification.
6. `## 安全底线` — preserve dirty work; never automatic merge, Stash, branch deletion, or Worktree deletion.
7. `## 交接格式` — source ref, target ref, commit, clean state, validation, unresolved risk, recommended decision.

Use the approved design document as the content source, without adding project-specific examples or paths.

- [ ] **Step 2: Wire the reference into the core Skill**

Update `SKILL.md` so `Inspect` loads the integration reference when Worktrees, branches, progress claims, or merge readiness are in scope; `Verify` checks stable-branch inclusion and fresh validation; `Hand off` reports the lifecycle decision and preserves the distinction between readiness and authorization. Keep the Skill under 180 lines.

- [ ] **Step 3: Extend the evidence gate**

Add to `references/evidence.md` a completion-claim checklist requiring:

```text
持久性：工作区 | 已提交
归属：候选分支 | 稳定分支
验证：未验证 | 已验证
```

State that `[Done]`/`READY` in a stable snapshot requires stable-branch inclusion and fresh applicable validation; candidate branches and uncommitted changes must be scope-labeled.

- [ ] **Step 4: Add creation and hand-off prerequisites**

Update `references/bootstrap.md` to require a unique objective, base ref, exit condition, and owner/authority before creating a Worktree. Clarify that a clean committed candidate can be parked by removing only the Worktree, while branch deletion remains separate.

- [ ] **Step 5: Run the focused tests and verify GREEN**

Run:

```powershell
python -m unittest tests.test_repository_contract.RepositoryContractTests.test_integration_readiness_cases_are_recorded -v
```

Expected result: PASS with no warnings. Then run the full repository contract suite before moving to project-baseline synchronization.

- [ ] **Step 6: Commit the Skill implementation**

```powershell
git add skills/yuanforge/SKILL.md skills/yuanforge/references/evidence.md skills/yuanforge/references/bootstrap.md skills/yuanforge/references/integration-readiness.md
git commit -m "feat: add evidence and worktree promotion gates"
```

### Task 3: Synchronize YuanForge’s own baseline

**Files:**
- Modify: `docs/WORKTREE_GUIDE.md`
- Modify: `AGENTS.md`
- Modify: `lessons.md`
- Modify: `progress.txt`
- Modify: `README.md`
- Modify: `docs/YUAN_LAYER.md`
- Modify: `docs/IMPLEMENTATION_PLAN.md`
- Inspect only: `skills/yuanforge/agents/openai.yaml`

**Interfaces:**
- Project documents reuse the Skill’s stable tokens and do not create another lifecycle registry.
- `AGENTS.md` remains a concise router; detailed lifecycle rules remain in the Worktree guide/reference.

- [ ] **Step 1: Update the Worktree guide**

Document the actual two-Worktree topology (`main` and `codex/writing`) and mark experiment/debug roles `按需`. Add the lifecycle, decision matrix, merge responsibility boundary, and safe parking/retirement rules. Do not list unmaterialized roles as actual Worktrees.

- [ ] **Step 2: Add the reusable lesson**

Record the observed failure as a reusable rule: progress claims must name their evidence scope; untracked/dirty candidate state cannot support `[Done]`; a Worktree is not required to preserve a clean committed branch. Do not include real external repository names, absolute paths, or commit hashes.

- [ ] **Step 3: Update the current snapshot**

Rewrite `progress.txt` as a current snapshot stating that the gates are implemented on `codex/writing`, pending stable integration and fresh verification. Keep existing baseline facts and mark any new claim as candidate until it reaches `main`.

- [ ] **Step 4: Synchronize public and concept documents**

Add a concise README explanation that YuanForge assesses integration readiness but does not autonomously merge/delete. Add the same ownership distinction to `docs/YUAN_LAYER.md` and the validation/integration gate to `docs/IMPLEMENTATION_PLAN.md`. Inspect `openai.yaml` for trigger wording; change it only if it fails to mention repository evidence or Worktree drift.

- [ ] **Step 5: Run text and link checks**

Run:

```powershell
git diff --check
python -m unittest discover -s tests -v
```

Expected result: zero whitespace errors and all contract tests passing.

- [ ] **Step 6: Commit the baseline synchronization**

```powershell
git add AGENTS.md README.md docs/YUAN_LAYER.md docs/IMPLEMENTATION_PLAN.md docs/WORKTREE_GUIDE.md lessons.md progress.txt
git commit -m "docs: adopt promotion and worktree lifecycle gates"
```

### Task 4: Validate, integrate, and update local/remote branches

**Files:**
- No new source files; verify all files changed by Tasks 1–3.

- [ ] **Step 1: Run the complete fresh verification on `codex/writing`**

Run all commands:

```powershell
python -m unittest discover -s tests -v
python C:/Users/ystg_/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/yuanforge
git diff --check
git worktree list
```

Also run a UTF-8/relative-link check through the repository tests and inspect `git status --short`. Do not claim readiness if any command fails.

- [ ] **Step 2: Push the writing branch**

Confirm the remote and upstream branch, then push only `codex/writing`:

```powershell
git remote -v
git push -u origin codex/writing
```

If no `origin` is configured, stop and report the exact blocker instead of inventing a remote.

- [ ] **Step 3: Integrate locally with explicit fast-forward**

From the clean `main` Worktree, fetch the pushed branch and fast-forward `main` to the verified writing tip. Do not use a destructive reset:

```powershell
git fetch origin codex/writing
git merge --ff-only codex/writing
```

If fast-forward is unavailable, stop and report the divergence for review.

- [ ] **Step 4: Re-run stable-branch verification**

On local `main`, rerun the full test, Skill validation, diff check, and Worktree topology check. This post-integration run is required before changing the stable snapshot to `[Done]`.

- [ ] **Step 5: Push the updated stable branch**

```powershell
git push origin main
```

Verify `git status --short`, `git log -1 --oneline --decorate`, and `git worktree list` for both Worktrees. Leave `codex/writing` as a clean, retained branch unless the user separately authorizes branch deletion.

- [ ] **Step 6: Update the stable snapshot and commit if needed**

Only after the post-integration verification, update `progress.txt` from candidate wording to stable wording, run the full verification again, commit the snapshot update, and push `main` once more. If the snapshot was already correctly phrased as integrated and verified, do not create a no-op commit.
