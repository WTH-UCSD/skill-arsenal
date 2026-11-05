---
name: formal-research-dag
description: Rigorous, long-running mathematical or formal theoretical investigation of an unresolved question or conjecture. Coordinates mechanism-distinct approaches, epistemic rounds, independent adversarial audits, a Verified Result DAG, and adaptively scheduled external review consultations within a structured LaTeX workspace (main.tex). Do not use for initial ideation, quick literature surveys, or lightweight markdown investigations (use research-loop instead).
---

# Formal Research DAG

Investigate one unresolved question while keeping strategy, established results, and execution history distinct.

Use this structure as follows:

- **Durable Investigation State** defines the workspace and its parallel state layers, including the definition and role of the Verified Result DAG.
- **Lifecycle** defines the execution order. Within a round, tasks produce candidate work, the principal updates approaches and may admit verified DAG nodes, and a due ChatGPT Pro review occurs only between completed rounds.

## Durable Investigation State

### Workspace Layout

```text
investigations/<question-slug>/
├── index.md
├── main.tex
├── approaches/
│   └── A001.md
├── dag/
│   ├── dag.yaml
│   └── nodes/
│       └── N001/
│           ├── N001.yaml
│           ├── N001.tex
│           └── audits/
│               └── direct-proof/
│                   ├── audit.md
│                   ├── audited-node.yaml
│                   └── audited-node.tex
├── rounds/
│   └── R001/
│       ├── round.md
│       └── tasks/
│           └── T001-001/
│               ├── task.md
│               ├── audit.md
│               └── artifacts/
└── chatgpt-pro/
```

Use stable, never-recycled IDs for approaches (`Axxx`), result nodes (`Nxxx`), rounds (`Rxxx`), and research tasks (`Trrr-ttt`). For task IDs, `rrr` matches the round number and `ttt` is the next research-task number within that round, with both components zero-padded to at least three digits. For example, R001 contains T001-001, T001-002, and later local research-task IDs. Audits and repairs receive no durable IDs of their own. Keep internal paths relative to the investigation root and all Research prose in English.

Keep raw data, caches, build products, checkpoints, and heavy outputs outside the investigation; task artifacts may point to them.

### Record Types

#### Approaches

An approach is a persistent strategy for a concrete target. The target may be the final question or an intermediate lemma, reduction, construction, obstruction, or other part of the reasoning. An approach may span many rounds and tasks. An A-ID identifies one mechanism-target strategy, while `episode` records its current or most recent period of active investigation.

Each `approaches/Axxx.md` file is the canonical record for one approach; the [approach.md template](assets/workspace/approach.md) defines its schema. Its frontmatter stores the approach's current structured state, including a `current_progress` list of material non-DAG results being carried forward; its body records the mechanism rationale and episode history. Each `current_progress` entry contains a `summary`, `verification: unverified | verified`, one artifact `source`, and independent-check paths in `checked_by`. An entry may be marked `verified` only after its current source has been checked with no unresolved material finding; otherwise it remains `unverified` with `checked_by: []`. Verification does not imply DAG admission.

#### Verified Result DAG

The Verified Result DAG is the investigation's global dependency model of important established results across approaches and rounds. Each node represents one exact independently verified theoretical or empirical result, and directed edges record prerequisite relations among those results. Provisional and withdrawn node records may remain in the workspace for provenance, but they are not members of the current Verified Result DAG.

The [Result DAG contract](references/result-dag-contract.md) defines the node, edge, membership, verification, and maintenance rules for the Verified Result DAG.

#### Rounds And Tasks

A round is one epistemic cycle from an incoming frontier through principal synthesis to an outgoing frontier. It may contain as many tasks and worker waves as the evolving frontier requires. The [round.md template](assets/workspace/round.md) defines the round record schema. It records the round's research-task IDs, worker waves, dispatch order, and minimum-task completion; its `Task Plan` is the principal's compact durable record of intended but undispatched work.

Each research task is one concrete assignment executed by a research-worker subagent. The [task.md template](assets/workspace/task.md) defines the task record schema, including its assignment, inputs, acceptance criteria, artifact paths, and disposition. Task artifacts retain or point to the candidate output, and each task-local `audit.md` records the task's independent audit.

#### ChatGPT Pro Consultations

Each Pro consultation is external reviewer input. Its artifacts are stored under `chatgpt-pro/` as a Markdown/LaTeX pair. The initial pair is named `pre-round-001-plan.md` and `pre-round-001-math.tex`; later pairs are named `rounds-NNN-MMM-review.md` and `rounds-NNN-MMM-math.tex`. An accepted Markdown file contains a positive integer `next_review_after_rounds` and its rationale.

The `pro_review` frontmatter in `index.md` is the live review schedule. It records the last accepted pair, `reviewed_through_round`, `next_review_after_rounds`, `next_review_due_after_round`, and the rationale, where `next_review_due_after_round = reviewed_through_round + next_review_after_rounds`. `Unreviewed Durable Changes` in `index.md` is the deduplicated set of investigation-relative durable files not covered by the last accepted Pro review.

### Root Views And Write Boundaries

`index.md` is the investigation's complete compact control view; the [index.md template](assets/workspace/index.md) defines its structure. It summarizes the current decision and frontier, approach and DAG state, Pro review state, and round navigation, while canonical approach and node details remain in their local records. Proof bodies and task transcripts remain in their source artifacts. `main.tex` is a coherent, readable overview of research progress; the [main.tex template](assets/workspace/main.tex) defines its structure.

The principal owns the approach portfolio, node admissions, DAG state, root views, scheduling, and cross-approach synthesis. Research-worker subagents write only within their assigned task directories, task auditors only to task-local `audit.md`, and node auditors only within the write boundaries defined by the [Result DAG contract](references/result-dag-contract.md).

## Lifecycle

Start with Stage 1. Run Stage 2 only for a new investigation. After each Stage 3 round, run Stage 4 when due, then use Stage 5 to continue or finish.

### 1. Start Or Resume

Treat the approved question and invocation as the contract: definitions, success standard, inadequate outcomes, source policy, resource bounds, destination, and any domain-specific audit checks.

- On every invocation, resolve `minimum_tasks_per_round` from the user's requested positive integer, defaulting to `4`. Treat it as a research-task minimum, record it in `index.md`, and do not change the recorded minimum of a round that has already dispatched a task.
- For a new investigation, use `<current-project>/investigations/<question-slug>/` unless current instructions specify another destination. Copy only `assets/workspace/index.md` and `assets/workspace/main.tex` into the new or empty directory and replace their placeholders. Create other directories when first needed.
- When resuming, start from index.md and follow its links as needed. Preserve completed historical task and audit paths rather than migrating them to match a newer layout.

### 2. Form The Initial Portfolio

Before forming the initial portfolio, verify the question's current status and relevant prior work with authoritative sources.

Begin with a genuinely diverse, problem-scaled portfolio. Seek substantially different formulations, invariants, reductions, structural or constructive mechanisms, algebraic or extremal viewpoints, and discriminating computation when relevant. Let the problem determine the number of useful approaches; neither worker capacity nor `minimum_tasks_per_round` determines it.

Before R001, dispatch fresh local workers to propose independent portfolios. Give them the formal question, source policy, constraints, and necessary source material, but not other local proposals or a favored approach. When external consultation is permitted, concurrently use `$chatgpt-pro-browser` with the [initial strategy prompt template](references/chatgpt-pro-initial-strategy-prompt.md).

Group proposals by their underlying idea and target, merge superficial duplicates, and check whether the surviving A-records are genuinely distinct. If proposals concentrate in one family while plausible alternatives remain underexplored, dispatch another independent discovery wave. Record and freeze the local portfolio before reading any Pro output.

If Pro consultation is not permitted, continue with the frozen local portfolio. If it is permitted but access is blocked, record the blocker and continue locally; never substitute a local worker and call it ChatGPT Pro.

When the Pro output is available, accept it only when the required Markdown/LaTeX pair and schedule fields are complete. Correct trivial, unambiguous typos directly; require a corrected Pro output for any change that could affect mathematical content, review scope, or schedule. On acceptance, record the pair in `pro_review` as the baseline for the next review and update the schedule from its Markdown file. Then compare the local and Pro portfolios, selectively incorporate Pro suggestions, and add the frozen local portfolio's durable records and every durable file created or materially changed during reconciliation to `Unreviewed Durable Changes`.

### 3. Run A Research Round

#### Open And Dispatch

1. Copy `minimum_tasks_per_round` into the round's `minimum_tasks` before its first dispatch.
2. Formulate useful research tasks from the evolving frontier to seek proofs, refutations, counterexamples, alternative mechanisms, and disconfirming evidence. A task may advance an existing approach, search for and formulate new approaches, combine verified nodes, or run a discriminating experiment.
3. Give each task a concrete assignment, inputs, acceptance criteria, and one expected output: a proof, counterexample, construction, source-backed finding, measured experiment, proposed approach, or exact failure gap.
4. Actually dispatch at least `minimum_tasks` distinct research-task `Trrr-ttt` IDs. Do not count planned placeholders, audits, or repairs. If more tasks are ready than there are subagent slots, dispatch the remainder in later waves.
5. Use a fresh worker for the first exploration of a new approach. Reuse a worker only to continue the same work when retained context is useful.
6. Restrict each research-worker subagent to its assigned task directory and treat all research-worker output as candidate material.

Before relying on an existing node as a task input, read and apply the Result DAG contract.

When an approach depends on an unproved intermediate result, record it as an exact blocker. Open separate approaches only for distinct strategies targeting that result. Treat a reduction whose missing result is comparable in difficulty or strength to its target as an exact blocker, not as near-completion. Do not keep assigning unchanged work to a theorem-strength blocker; revisit it only when new information supplies a materially different invariant, construction, or decisive check.

Before defining any proof task's acceptance criteria, read and apply the complete-proof standard in the Result DAG contract, regardless of whether the result is intended for DAG admission.

Preserve early independence until each approach's assumptions and exact gap are explicit. For independent exploration, do not disclose the principal's favored approach or unrelated approach records unless the task depends on them. Cross-pollinate only after that point.

When several viable, incompatible approach families have ready checks, keep more than the currently favored family alive across rounds. If assignments concentrate in one family, redirect subsequent tasks toward underexplored ready families or fresh-formulation search. Do not impose equal quotas.

#### Integrate Returned Work

As tasks return:

1. Record the return and confirm that the declared output and artifact paths are present and readable.
2. Have a fresh auditor independently and adversarially audit the complete output against its original assignment and stated claims before assigning a final disposition. Give the auditor the complete current output, relevant dependencies, and applicable checks without suggesting a verdict. Scale the audit to the output's stated epistemic scope, actively seek hidden assumptions, missing steps, circularity, counterexamples, boundary cases, source errors, and failed calculations, compilation, or reproduction where relevant, and record the review in the task-local `audit.md`.
3. Return repairable findings to the original worker, then have the same auditor recheck the complete current output in the same `audit.md`. Record any deliberately unresolved issue as an exact gap, not as a refutation or near-completion.
4. After the task-local audit reflects the complete current output, use that output and audit to record one disposition for each material result in the task's Integration Note: admit it after required verification; carry it forward through the relevant approach's `current_progress` with its verification state and artifact or check paths, while updating the approach-level exact gap, next check, and status when affected; or do not carry it forward, with the substantive reason. When updating `current_progress`, set an entry to `unverified` and clear `checked_by` if its source changes; remove it when it is admitted, superseded, or deliberately dropped.
5. If a material result merits DAG admission, materialize its provisional node pair and follow the Result DAG contract through node audit before admitting it. Apply the contract before changing or withdrawing an existing node. Use the [node audit prompt template](references/node-audit-prompt.md) when a support route first enters audit. A task-local audit does not replace the node audit.
6. Close an approach only with a precise basis and reopening condition, not merely because one task failed. When reopening an approach, retain its A-ID and increment `episode` if its mechanism and target remain unchanged; otherwise create a new A-ID.
7. Update the current round delta, `index.md`, and `main.tex` when its overview changed. When Pro review is enabled, add every durable file created or materially changed by the integration to `Unreviewed Durable Changes`; include provisional node pairs as candidates, never as established DAG results.
8. Repeat Open And Dispatch from the updated frontier without waiting for an entire worker wave. Put every reused candidate artifact and its task-local audit in the new task's `inputs`.

#### Complete The Round

Keep the round open until every dispatched research task has completed the integration procedure above or been explicitly cancelled. Then:

1. Write the principal synthesis, approach and DAG changes, outgoing frontier, and exit reason, carrying every still-useful unstarted Task Plan item into the outgoing frontier.
2. Check that all non-DAG IDs, paths, and references resolve.
3. Apply the Result DAG contract's completion checks to every admitted node, verified support route, and compact DAG view.
4. Check that `index.md` contains every approach and reflects the current investigation state, and that `main.tex` remains a coherent, readable overview of current research progress.
5. Check that every material result has a recorded disposition and every carried-forward candidate is linked, with its verification state, from the relevant approach's `current_progress` and the compact approach snapshot in `index.md`.
6. Check that the round's qualifying research-task IDs meet `minimum_tasks` and that its recorded deltas match the canonical records.
7. Check that the Pro schedule and `Unreviewed Durable Changes` are current and internally consistent.
8. Mark the round completed and dispatch no further tasks under that R-ID.

### 4. Pass The Pro Review Gate When Due

Count completed research rounds only. At the due boundary, snapshot `Unreviewed Durable Changes` and use `$chatgpt-pro-browser` with the [adaptive review prompt template](references/chatgpt-pro-adaptive-review-prompt.md) before starting another round or making final confirmation.

Apply the same pair, schedule, and correction requirements as for the initial consultation. Accept the adaptive review only if it covers the preceding accepted pair, the completed research block, the durable views and DAG supplied at dispatch, and every path in the dispatched snapshot. On acceptance, replace the baseline in `pro_review` with the accepted pair, update the schedule from its Markdown file, and remove the snapshot paths from `Unreviewed Durable Changes`.

Incorporate the review and update the root views. Add every durable file created or materially changed by that incorporation, including root-view changes, to `Unreviewed Durable Changes`, then reapply the round-completion consistency checks to any affected durable state.

Do not create extra rounds merely to reach a future review date. If the investigation reaches a stopping condition before the due boundary, proceed to Stage 5.

### 5. Continue Or Finish

After each completed round and any due review, either open the next round from the outgoing frontier or stop when:

- an audited result or decisive refutation meets the question's success standard;
- the agreed budget is exhausted, or
- required evidence, access, permission, or user judgment is unavailable.

Do not conclude that no materially new mechanism remains merely because the current approaches failed; first perform an explicit fresh-formulation search from the full question.

Before handoff, record the final decision in the root views. Return either the audited result or the strongest supported progress, exact scope, decisive gap, informative failed approaches, and best next action. Separate correctness from novelty and verify prior art before claiming novelty. Link the important approach, node, round, task, and Pro artifacts.
