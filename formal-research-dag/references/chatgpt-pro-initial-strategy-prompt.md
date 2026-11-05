# ChatGPT Pro Initial Strategy Prompt

Use this template for the independent pre-Round-1 consultation. A separate Pro-facing subagent may run it in parallel with local portfolio formation, but the principal must freeze the local portfolio before reading the Pro output. Replace every bracketed placeholder before sending it, and do not attach or expose the local portfolio.

```text
Independently design a research strategy for the unresolved question below.
Do not assume the desired conclusion is true. Seek proof and refutation routes,
counterexamples, alternative formulations, and discriminating experiments as
appropriate.

Project:
[PROJECT_PATH]

Investigation:
[INVESTIGATION_PATH]

Formal question:
[QUESTION_PATH]

Source policy:
[SOURCE_POLICY]

Material constraints:
[CONSTRAINTS]

Read the formal question and all question-level references or source files
supplied with it. Follow the source policy for any additional literature
search.

To preserve strategy independence, do not inspect index.md, main.tex, approach
records, task artifacts, or any local strategy output, even if they are
visible. Do not infer or ask for the local approach portfolio.

Develop a problem-scaled portfolio of genuinely mechanism-distinct approaches.
Do not manufacture one approach per worker or treat literature search,
experimentation, auditing, or worker roles as distinct mechanisms. For each
approach:

1. State its mechanism, exact target, and necessary assumptions.
2. Identify dependencies and the strongest likely theorem-strength gap.
3. Give the next decisive proof, counterexample, source check, or experiment.
4. State likely failure modes and what evidence would close or reopen it.
5. Explain how it differs from the other proposed approaches.

Then prioritize the initial frontier, identify work that should remain
independent before cross-pollination, propose adversarial checks for material
candidate conclusions, and choose the positive integer number of completed
research rounds that should elapse before the first Pro review. Choose a short
interval for difficult, uncertain, tightly coupled, or rapidly changing work
and a longer interval for simple, stable, clearly scoped work with strong local
checks. Base the interval on this question rather than a default cadence.

Additional questions:

[ADDITIONAL_QUESTIONS]

Answer each question directly. Treat questions as requests, not premises; call
out mistaken assumptions or useful reframings.

Write exactly these two new files:

[PLAN_OUTPUT_PATH]
[MATH_OUTPUT_PATH]

The Markdown file must contain the complete independent portfolio and
prioritized strategy. End it with a clearly labeled schedule using both field
names below:

## Next Pro Review Schedule

- `next_review_after_rounds`: <positive integer>
- `rationale`: <brief substantive rationale>

The LaTeX file must contain substantive candidate statements, derivations,
proof attempts, counterexamples, or experiment formulations that could support
the proposed strategy. It must not merely duplicate the prose plan.

Do not modify an existing file, create any other output, or execute a research
round. A chat-only answer, missing companion file, or Markdown file without a
valid scheduling block is incomplete.
```
