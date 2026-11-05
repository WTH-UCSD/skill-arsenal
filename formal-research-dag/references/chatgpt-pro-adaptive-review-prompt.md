# ChatGPT Pro Adaptive Review Prompt

Use this template at an accepted schedule's due boundary. Replace every bracketed placeholder before sending it.

```text
Independently and adversarially audit the completed research block and identify the strongest
justified next strategy.

Project:
[PROJECT_PATH]

Investigation:
[INVESTIGATION_PATH]

Formal question:
[QUESTION_PATH]

Source policy:
[SOURCE_POLICY]

Current durable views:
[INDEX_PATH]
[MAIN_TEX_PATH]
[DAG_YAML_PATH_OR_NONE]

Completed research block:
[ROUND_START]--[ROUND_END]

Review baseline (both files are mandatory):
[BASELINE_MARKDOWN_PATH]
[BASELINE_MATH_PATH]

Durable files created or materially changed since that baseline:
[UNREVIEWED_DURABLE_FILES]

First read the formal question, every current-view file that exists, both
baseline files, and every file in the changed-file list. Follow the source
policy for any additional literature search. Inspect other relevant project
files and follow node dependencies, citations, approach links, task provenance,
and audit records as needed. List every additional file used in the report.

Verify every approach and node state against its canonical statement, support
source, and source-matched audit or reproduction. Empirical evidence cannot
establish a general theoretical claim.

Treat a node pair with `status: candidate`, a route with `needs_recheck`, or a
reserved N-ID absent from `dag.yaml` as provisional candidate material rather
than an established DAG result. Treat a node audit as accepted only when its
`audit.md` reports no unresolved material finding for the named support key and
its retained copies bind the exact current pair. For every new or changed
admitted node, verify that its accepted node audit inspected the current
YAML/TeX pair rather than only an originating task artifact. For every verified
support route, require its
audit to name its exact support key and retain the inspected pair as
`audited-node.yaml` and `audited-node.tex`; verify that the current substantive
node payload—every YAML field except node status and route status/check
metadata—has the same parsed data as the audited YAML copy after those fields
are omitted, that the current TeX is
byte-for-byte identical to the audited TeX copy, and that its `checked_by`
contains that audit. Accept later
status or check changes on other routes only when each has its own accepted
serial audit; do not invalidate an earlier route solely because another route
was later cleared by its audit.

Review requirements:

1. Reconstruct the actual mathematical and empirical changes in the block.
2. Audit new or changed statements, proofs, citations, experiments,
   assumptions, quantifiers, boundary cases, and limitations. For a DAG node,
   also check its formal statement and assumption environments, faithful
   interpretation and proof or evidence idea, complete readable route, and
   standalone compilation.
3. Audit dependency consequences, including alternative support routes and
   any node withdrawal or approach closure/reopen decision.
4. Evaluate whether the approach portfolio is genuinely mechanism-distinct,
   whether early independence was preserved long enough, and whether work was
   scheduled by readiness rather than worker count.
5. Identify theorem-strength gaps hidden by phrases such as routine, likely,
   essentially complete, or failure to find.
6. Critically evaluate index.md, main.tex, and dag.yaml when present for
   unsupported or inconsistent synthesis.
7. Propose a concrete next frontier: approach, exact task, required inputs,
   decisive output, and audit needs.

Choose a shorter next-review interval when the frontier is difficult,
uncertain, tightly coupled, or likely to change rapidly. Choose a longer
interval when the next work is simple, stable, clearly scoped, and strongly
covered by local checks. Choose anew from current evidence; do not copy the
preceding interval mechanically. Count completed research rounds only.

Additional questions:

[ADDITIONAL_QUESTIONS]

Answer each question directly. Treat questions as requests, not premises or
limits on the independent review; explain mistaken assumptions or needed
reframings.

Write only these two new files:

[REVIEW_OUTPUT_PATH]
[MATH_OUTPUT_PATH]

The Markdown file must contain the complete independent review and next
strategy. End it with a clearly labeled schedule using both field names below:

## Next Pro Review Schedule

- `next_review_after_rounds`: <positive integer>
- `rationale`: <brief substantive rationale>

The LaTeX file must contain substantive candidate derivations, proof attempts,
counterexamples, or experiment formulations rather than duplicating the prose
review.

Do not modify existing files or execute the next research round. Both files and
the schedule block are required.
```
