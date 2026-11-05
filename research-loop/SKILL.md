---
name: research-loop
description: >-
  Research ideation, problem framing, and academic literature frontier mapping. Use when brainstorming research questions, exploring prior art via OpenAlex and Valyu, verifying if an academic or technical question is already settled or open, and scoping new research directions. Hand off to formal-research-dag when ready for sustained mathematical proofs or formal DAG-verified investigations.
---

# Research loop — Ideation & Literature Frontier

Turn a fuzzy hunch or seed paper into sharp, testable research questions and a
literature-grounded decision surface.

| Phase | Purpose | Output |
|---|---|---|
| **0. Setup** | Configure OpenAlex (open API) and Valyu (semantic search). | Verified search backends. |
| **1. Frame** | Scope assumptions and formulate ≤3 diverse, concrete questions. | Concrete candidate question set. |
| **2. Map** | Query literature, walk citations, and deep-read nearest candidates. | Saturation analysis & residual delta map. |
| **3. Decision Surface** | Pause for the user's take on the mapped frontier. | User-approved research question. |

When the user accepts the framed question and is ready for sustained mathematical
proofs, formal lemma dependency tracking, or LaTeX writeups, hand off to
`formal-research-dag`. For rapid, lightweight notes, the built-in investigation lane
remains available.

## Shared coordinator protocol

Treat the user's invocation as the task statement. Do not ask them to restate
information already present. Infer ordinary details, but ask one concise
question when a missing choice would materially change the research or
authorize a meaningful scope expansion.

1. **Preflight the real context.** Inspect local instructions, the relevant
   workspace, available search or subagent tools, credentials, note location,
   execution constraints, and existing artifacts before consequential work.
   Do not claim a search, experiment, or audit that was not actually run.
2. **Dispatch independent routes.** When multiple subagents are available,
   launch several fresh-context workers on genuinely different mechanisms,
   source paths, proof strategies, or discriminating tests. Use the capacity
   that exists; never assume a fixed agent count. Keep the root agent
   synthesizing while workers run and fill newly available slots with fresh
   routes or audits. If subagents are unavailable, make the passes sequentially
   and disclose that limitation.
3. **Protect independence.** Give workers the task statement and necessary
   evidence, not the root agent's favored answer. Do not repurpose a proposer
   as an auditor or a worker from one approach family as a worker for another
   without a deliberate fresh context. Workers return route-level results or
   isolated artifacts; the root agent owns the synthesis and any main research
   note so concurrent workers do not overwrite one another.
4. **Require inspectable outputs.** Accept a precise claim, derivation,
   construction, counterexample, source-backed status finding, executable
   experiment and measured result, failed argument with its exact failure
   point, or strongest objection with the remaining gap. Reject vague
   optimism, unexplained compatibility claims, and "routine" global steps.
5. **Integrate by mechanism, not by agent.** Merge duplicates at the route
   level, record conflicts and dependencies, and redirect blocked or
   repetitive work toward a materially new check. Cross-pollinate routes only
   after they have exposed their own assumptions and gaps.
6. **Audit the strongest claim.** Use fresh-context adversarial workers during
   the run and before completion. Check scope, quantifiers, hidden assumptions,
   counterexamples, source accuracy, reproducibility, and boundary cases.
   Same-model review is useful, but it is not independent machine verification.

Keep these distinctions explicit throughout both lanes:

- retention or forgetting is not future plasticity or learnability;
- current-task performance or reward is not either of those outcomes;
- correctness is not novelty;
- a correlation is not a sufficiency or causal result;
- a queued or planned experiment is not a measured result.

## Lane 1 — Ideation / Frontier

This lane is a deliberate loop for loading the user's context before they
write a project blueprint. It normally remains in chat and writes no files.
Read the linked reference only as each phase begins:

| phase | read | produces | subagent use |
|---|---|---|---|
| 0. Setup | `references/setup.md` on the first search run | verified or explicitly degraded search mode | root preflight |
| 1. Frame | `references/frame.md` | at most three diverse, concrete questions and surfaced assumptions | usually none; framing stays with the root agent |
| 2. Map | `references/frontier-map.md` | nearest neighbors, per-question residual delta, and saturation status | parallel deep reads and adversarial nearest-neighbor checks |
| 3. Pause | — | the frontier as a decision surface | stop for the user's take |
| 4. Loop | `frame.md` and/or `frontier-map.md` again | revised questions or a saturated frontier | fresh workers for new candidates or checks |

Rules for this lane:

1. Run significance before operational detail. Do not operationalize a
   question that is already settled; name the nearest framing and the possible
   residual angle instead.
2. In Frame, do not search. Emit no more than three questions, and name any
   dropped branches so the user can recover them.
3. In Map, query at mechanism-class grain, harvest terminology from retrieved
   papers, walk both citation directions, and deep-read the nearest candidates.
   Abstracts and snippets route candidates; they do not support strong overlap,
   novelty, or hypothesis claims.
4. After Map, stop. The user's response is a required research input, not a
   courtesy. Reframe when their response changes the question.
5. Loop while the glossary or question set is still gaining new terminology or
   adjacent questions, or while the user's take reframes the problem. Stop when
   the frontier is saturated and the user accepts the questions.

The frontier map must classify each residual as `settled`, `largely done`,
`known-question / unclaimed-measurement`, `open-but-risky`, or `open`; it must
not reduce the result to a bare novel/not-novel verdict. Use the exact deep-read
schema in `references/frontier-map.md`, including one load-bearing quote for
each strong overlap claim.

If the user now wants a proof, counterexample, experiment, or durable research
program, bridge explicitly to Lane 2 and carry the accepted questions,
assumptions, frontier map, and unresolved risks into its task statement.

## Lane 2 — Investigation / Execution

This lane is the end-to-end investigator protocol. Read
`references/investigation.md` at lane entry. It covers adaptive route
selection, durable notes, formal artifacts, experiments, resumption, and
adversarial audits. The compact control flow is:

1. Resolve the task statement, success standard, constraints, workspace, and
   note location; maintain an app-visible plan for a substantial run.
2. Create or reuse one main research note before launching workers when the
   project needs durable state. Keep it organized by routes and research
   logic, not by agent names.
3. Launch independent route workers, then run targeted derivations, searches,
   or experiments only when they discriminate between live hypotheses or test
   a concrete mechanism.
4. Update the affected route after each worker, material experiment, or audit;
   record the artifact, exact result, uncertainty or failure, disposition, and
   next decisive check.
5. Assign fresh-context auditors to the strongest candidate conclusion and
   downgrade or redirect it when they find a valid objection.
6. Finish the durable note before reporting. Stop only on a supported result,
   supported refutation, an honest resource boundary, a lack of a materially
   new check, or unavailable required access or judgment.

Do not label an incomplete investigation complete. Return the strongest
supported result, exact scope, decisive remaining gap, failed routes, changed
files or artifacts, verification performed, and best next action.

## Reference loading

- Read `references/setup.md` only when the Ideation lane needs its search
  backends or when a degraded-mode decision must be made.
- Read `references/frame.md` before every Frame phase.
- Read `references/frontier-map.md` before every Map phase.
- Read `references/investigation.md` before starting or resuming Lane 2.

Do not treat these references as separately triggerable skills. They are the
progressively disclosed operating manual for this single `research-loop`
skill.
