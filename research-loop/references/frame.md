# Phase 1 — Frame

Turn the fuzzy idea (+ optional seed paper/URL/blog) into **≤3 diverse, concrete, searchable questions**, with the assumptions made along the way surfaced so the user can catch bad narrowing. **Do no search in this phase** — it decides *what is worth searching for*.

## Why this phase matters

The commodity tools search whatever query they're handed; none ask whether it's the *right* query, or surface what the user smuggled in. This decomposition is the non-commodity step — and it's where the agent's priors do the most damage, because a fluent, over-specified restatement *feels* like progress and quietly steers the user into the well-trodden version of their question.

## Two stages, gated in order

Run significance first. Do not operationalize a question nobody cares about — a beautiful eval design for a dead question is wasted budget and a false sense of motion.

### Stage 1 — Significance gate (no operational detail yet)
- Is this a real gap, or already settled? If settled, **say so and name where** — do not dress up a non-question.
- Does the field care from first principles, or is it folklore?
- What is the nearest well-known framing this sits next to?

Almost everything has been done in *some* form. The output here is never "novel / not novel" — it is "nearest neighbor, and the angle that might still be unclaimed."

Keep adjacent outcomes separate before judging significance:
- **Forgetting / retention**: how much existing capability survives adaptation.
- **Plasticity / future learnability**: how fast, how far, and how reliably the adapted model learns a later task.
- **Performance / reward**: how well the current task is solved.

Do not let evidence for one outcome silently stand in for another. If prior work shows "low KL predicts less forgetting", it does not automatically settle "low KL is sufficient for future plasticity."

For scalar-predictor hunches ("does X predict Y?"), frame the sharp version as a sufficiency or residual question:
- If two histories are matched on X, do they have the same Y?
- What residual variables would make X fail: path length, local vs endpoint displacement, task order, reward quality, optimizer state, data mixture, intervention channel?
- Which variables are causal instruments or controls, and which are actual axes of the research question?

If the user already offers a hypothesis, pressure-test it rather than adopting it. Say what would make the hypothesis false before proposing experiments.

### Stage 2 — Operationalize the survivors

| dimension | question to answer |
|---|---|
| model / scale | what architecture, what size — is scale itself the variable? |
| data / RL pipeline | what task stream, what reward, what boundaries/resets? |
| credit + eval | how is success measured, on what held-out signal? |
| place in the loop | how does this fit the bigger picture (e.g. continual learning) — is it load-bearing? |
| confounds | what would a skeptic say is doing the real work? |

## Output (emit to chat)

Emit **≤3 questions**. `3` is a cap, not a target: if the idea resolves cleanly to one, emit one; if it fragments into six, emit the three strongest and **name the ones you dropped** so the user can override. The questions must be **diverse** — spanning different mechanisms/assumptions, not three surface variants of one commitment (three questions that all assume optimizer-reset are one question asked three times).

For each question:
- **Question** — the sharp, concretized form.
- **Assumptions injected** — what you *chose* (mechanism, eval, scale) and the alternatives set aside. Mandatory: concretizing silently is the failure mode, because it steers the user into the common/searchable version and away from the naive-but-unclaimed one.
- **Why it might matter** — the contribution it could make if the gap is real.
- **What would falsify it** — the smallest result or nearest prior that would make this question uninteresting or already answered.
- **Starting glossary** — candidate terms/aliases to seed search. Flag as *seeds only*: the real terminology is harvested from retrieved papers in Phase 2, because you cannot pre-name a concept you've never seen named (loss of plasticity = capacity loss = primacy bias = churn = warm-start problem).

Then hand the questions to Phase 2 (or back to the user). Do not search here.

## Worked example

Input: *"Does RL preserve plasticity? I read a Sutton paper on a plasticity-preserving pretraining algorithm."*

Significance gate: loss of plasticity is an established line (Dohare/Sutton, Lyle); the *question* is not novel. Unclaimed angle: plasticity under **RLVR through a task sequence** with **boundary interventions**, which the pretraining literature doesn't cover.

Emitted (1 of ≤3):
- **Question:** Does RLVR over a sequence of verifiable tasks (math → code → instruction-following) with optimizer reset at task boundaries preserve plasticity, measured on a held-out tool-call RL task — and how do other plasticity-preserving methods and LLM-native methods compare?
- **Assumptions injected:** chose optimizer reset as the mechanism (alternatives set aside: no reset, KL-to-base anchor, replay buffer); chose tool-call as the transfer eval (alternative: held-out math split).
- **Why it might matter:** isolates whether plasticity loss in RL is optimizer-state-driven vs weight-driven.
- **What would falsify it:** a prior study already matching task reward and endpoint displacement while showing boundary resets fully explain future learnability.
- **Starting glossary (seeds):** loss of plasticity, capacity loss, churn, task-boundary reset, continual RL, RLVR.
