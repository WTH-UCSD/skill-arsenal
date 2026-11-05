# Lane 2 — Investigation / Execution

Investigate one unresolved research question end to end. Preserve the
multi-agent search protocol without hard-coding a conclusion, agent count,
wall-clock duration, or closed-book policy.

## Progress UI

For a substantial run, maintain an app-visible `update_plan` checklist with
these phases:

1. Resolve the task statement, working context, note location, and material constraints.
2. Explore independent approach families and gather concrete evidence.
3. Run targeted derivations, searches, or experiments and synthesize the results.
4. Adversarially audit the strongest candidate conclusion.
5. Update the durable research note and report the result or exact gap.

For one small bounded research question, omit the persistent checklist. Keep
preflight separate from experiment or implementation work; do not show an
experiment as active before the invocation has authorized it or its scope has
been resolved.

## Use the invocation as the task statement

Treat the user's invocation as the source of the problem-specific content: the
question, definitions, success standard, insufficient outcomes, source policy,
resource constraints, experiment expectations, note destination, and
domain-specific audit checks.

- Do not impose a form or ask the user to restate information already present.
- Infer ordinary details when the intent is clear. Ask one concise question
  only when a missing choice would materially change the research or authorize
  a meaningful scope expansion.
- Do not assume the desired conclusion is true. Search for proofs, refutations,
  alternative mechanisms, and disconfirming evidence as appropriate.
- Default to real-research mode: verify current status and prior work with
  authoritative sources. Use closed-book mode only when the user explicitly
  requests a benchmark or independent-reasoning constraint.

## Maintain a hierarchical live record

Follow the nearest workspace and domain instructions before editing code,
running experiments, or writing notes.

For a WTH Research project:

- Use the nearest `Research/projects/<project>/` as the research context.
- Before launching the first workers, locate or create one main Markdown note
  under `notes/`, reusing an existing relevant note or creating
  `notes/YYYY-MM-DD-<short-question>.md`. Record the task statement, success
  standard, material constraints, and initial approach families.
- Treat the main note as the research control layer, not an agent transcript.
  Organize it by research logic with a light hierarchy, omitting empty
  sections:
  - `Current State`: strongest supported conclusion, exact gap, live next
    moves, and major uncertainty.
  - `Approach Registry`: one subsection per approach family, with nested routes
    distinguished by mechanism. For each route keep its status, concrete
    result, evidence or artifact links, audit findings, exact failure point or
    uncertainty, disposition, and next decisive check.
  - `Cross-route Synthesis`: shared facts, conflicts, dependencies, and
    promising combinations.
  - `Experiments And Artifacts`: an index of linked proof files, code,
    configurations, jobs, outputs, and substantial experiment notes.
  - `Round Ledger`: a short chronological record of what changed and why; do
    not duplicate the route details here.
- Integrate each worker's output into its route rather than creating sections
  named after agents. Merge duplicate work at the route level and attach an
  audit to the claim or route it checks.
- As work that may outlive the current turn or is costly to repeat is launched,
  checkpoint whether it is a session-local worker or durable external job, its
  route objective, material inputs and configuration, acceptance criterion,
  task or job identifier when available, artifact destination, last-known
  state, and how to poll or relaunch it. On resumption, mark each pending entry
  `running`, `completed`, `failed`, or `unrecoverable` before launching
  duplicate work.
- After each completed worker, material experiment, or audit, update the
  affected route as `concrete result -> evidence or artifact -> uncertainty or
  failure -> disposition or next check`. Refresh `Current State` whenever a
  result materially changes the conclusion or next move, and add one concise
  ledger entry after each round.
- Keep the note sufficient for a new session to resume from it and its linked
  artifacts without relying on prior chat context.
- Split out a directly linked child Markdown note only when a route or
  experiment becomes substantial; do not pre-create files or build a deep note
  tree.
- Follow local rules for any required project index or Research log updates.

If no durable research workspace or note destination can be inferred, ask where
to write before creating files.

## Use Markdown and TeX by role

- Use Markdown for the live research state, approach registry, synthesis,
  experiment records, audit decisions, evidence links, exact gaps, and next
  actions.
- Use TeX math inside Markdown for short formulas, definitions, and result
  statements.
- Put a substantive proof, counterexample proof, or long formal derivation in
  a linked `.tex` source when correctness depends on exact notation,
  quantifiers, multiple formal results, long equation chains, macros,
  numbering, cross-references, or line-by-line audit. Before treating such an
  argument as a candidate conclusion or sending it for adversarial audit, put
  its exact statement and full argument in TeX.
- Keep the Markdown route entry as the status and navigation layer; summarize
  the TeX artifact's scope, audit state, exact gap, and link. Treat the TeX file
  as the source of truth for the formal argument and do not maintain a
  duplicate full proof in Markdown.
- Follow the project's local artifact location and build rules. Otherwise keep
  the TeX artifact with the project notes and link it directly from the main
  note.

## Run an adaptive research loop

Scale the loop to the question. A small decisive investigation may use one or
two routes and one appropriately independent audit; expand only when a
material gap, conflict, or uncertainty warrants it. Do not create workers,
routes, or artifacts merely to fill the structure.

### 1. Start with genuinely different approaches

- For a broad or uncertain question, begin with a diverse portfolio of
  mechanisms, formulations, hypotheses, proof strategies, evidence sources, or
  experimental tests.
- Distinguish approaches by their underlying idea, not by agent names or
  superficial wording.
- Preserve early independence: give most workers the task statement and
  necessary evidence without telling them the root's favored approach.
- When several routes are warranted, keep incompatible ones alive long enough
  to reveal their real strengths and gaps.

### 2. Use the available subagent capacity dynamically

- Never assume 64 concurrent agents or any fixed worker count.
- Use only the worker slots actually available in the current Codex session.
  In the local Codex App this will often mean a small number of concurrent
  workers; launch a few independent routes, then fill each newly freed slot
  with a fresh-context worker for the next route or round.
- Treat every new route, new round, and adversarial audit as a fresh subagent by
  default. Use a follow-up turn on an existing subagent only to continue
  exactly the same route when its prior context is deliberately required; never
  repurpose a worker across approach families or from proposer to auditor.
- Do not allocate a fixed number of agents to each strategy. Redirect workers
  as evidence, duplication, blocked routes, and underexplored ideas become
  visible.
- Continue useful root-agent work while workers run.
- If parallel capacity is unavailable, use fresh sequential workers for any
  portfolio that still needs independent passes and disclose the degradation.

### 3. Require concrete research outputs

Ask each worker to return concrete, inspectable work such as:

- a precise claim, lemma, derivation, construction, or counterexample;
- source-backed evidence or a status/prior-art finding;
- executable code, an experimental design, or measured results;
- a failed argument with the exact failure point;
- the strongest objection and the exact remaining gap.

Reject vague optimism, status-only reports, unexplained compatibility claims,
and assertions that an unproved global step is routine.

### 4. Synthesize and redirect by mechanism

- Group worker outputs by the underlying approach family and recognize
  duplicates.
- Do not let an approach dominate merely because it gives an elegant
  reformulation or reduction.
- Treat a route that ends at an equally strong missing result as blocked, not
  nearly complete. Record the exact blocking gap in the live note.
- Reopen a blocked route only when a materially new mechanism, invariant,
  construction, source, or experiment appears.
- Redirect duplicate or stalled effort toward underexplored formulations and
  decisive checks.
- Cross-pollinate concrete results only after independent routes have developed
  enough to expose their assumptions and gaps.

### 5. Run discriminating experiments when useful

- Use experiments to distinguish live hypotheses, test a claimed mechanism,
  find counterexamples, or validate a construction; do not run experiments
  merely to create activity.
- State what result would support or weaken each hypothesis before running a
  material experiment.
- Follow the project's execution rules. For WTH Research, do not run
  experiments on the local Mac; use the configured cluster through Slurm and
  keep heavy artifacts under the approved `/data` project paths.
- Inspect local repository instructions before editing or running code.
- Record the code or commit, configuration, data, seeds when relevant, job
  identifiers, outputs, interpretation limits, and failures in the matching
  route or a linked Markdown experiment note.
- Ask before a materially costly, risky, externally visible, or scope-expanding
  run that the invocation did not authorize.

### 6. Adversarially audit candidate conclusions

- Assign fresh-context workers to attack the strongest candidate result
  throughout the investigation, not only at the end.
- Give auditors the original task statement, primary evidence or artifacts,
  candidate result, and relevant problem-specific checks. Do not give them a
  desired verdict.
- For a formal proof or counterexample, require the auditor to inspect the
  linked TeX source directly. Bind the verdict to an immutable repository
  commit when versioned, otherwise to SHA-256 hashes of the TeX source and any
  directly included proof-relevant files. Verify that binding on resumption and
  before final reliance; any mismatch or material change resets the argument to
  unaudited until a fresh audit checks the new version.
- Check the exact scope and quantifiers, hidden assumptions, circular reasoning,
  equally strong missing steps, counterexamples, conflicting evidence, source
  accuracy, reproducibility, and boundary cases.
- Prefer deterministic checking, formal verification, independent
  recomputation, or reproduction when available. Same-model adversarial review
  is useful but is not independent machine verification.
- Feed every valid finding back into the next research round or downgrade the
  conclusion.

### 7. Repeat with new information

The root agent should repeatedly synthesize, challenge, redirect, and launch
new rounds. Do not stop merely because the first wave fails. Do not continue by
repeating a blocked mechanism without new information.

Stop when one of these conditions holds:

- the requested result satisfies the invocation's success standard and survives
  the required audit;
- a refutation or decisive negative result survives audit;
- the stated resource budget is reached without a defensible complete result;
- further work lacks a materially new mechanism or decisive check;
- required data, access, permission, or user judgment is unavailable.

Do not substitute a minimum wall-clock time for evidence or coverage. Never
label an incomplete result as complete.

## Finish honestly

- Return the complete audited result when one exists.
- Otherwise return the strongest rigorously supported progress, its exact scope,
  the decisive remaining gap, the most informative failed routes, and the best
  next step.
- Separate correctness from novelty. Do not claim a result is new unless
  prior-art checking supports that claim.
- Finish the durable research note before reporting completion and link the
  user to the note and important artifacts.
- Summarize files changed, experiments run, verification performed, unresolved
  uncertainty, and the recommended next action.
