# Phase 2 — Map

Locate, for each question, **the nearest prior work and the specific delta the question still owns**. This is not a novelty check — "has this been done" is a negative-existence claim search is structurally bad at, and for a PhD student it is the wrong question anyway (the contribution is rarely the novelty of the *question*; it's the measurement/design). Output a frontier map, not a verdict.

## Sources and their roles

Not interchangeable — they cover different things.

| source | role |
|---|---|
| **OpenAlex** | Citation-graph spine. Walk **both** directions: `referenced_works` (backward) and `cited_by_api_url` (forward). Forward cited-by catches work *newer* than the seed paper — where false-novelty hides. Also gives concept/topic tags and stable IDs. Keyless; append `&mailto=$OPENALEX_MAILTO` if set. |
| **Valyu** | Semantic recall. Being semantic (not keyword) it's robust to terminology fragmentation — good first-pass recall + backward references, but it does **not** do forward citation traversal, so it does not replace OpenAlex. Needs `$VALYU_API_KEY`. |
| **arXiv / fetch** | Pull abstracts/full text for the verification step. |

Prefer connected MCP tools if present; otherwise call the HTTP APIs directly with the contracts below. Use `curl`, not Python's `urllib` — the local Python cert bundle often fails HTTPS verification; `curl` and `jq` are the reliable path.

## Call contracts

**OpenAlex** (keyless). Search, forward-citation walk, single record:
```bash
# search
curl -s 'https://api.openalex.org/works?search=<terms>&per-page=10&mailto='"$OPENALEX_MAILTO"
# forward citations (papers citing work W...): use the cites filter, NOT cited_by_api_url (often null)
curl -s 'https://api.openalex.org/works?filter=cites:W4399425460&sort=publication_date:desc&per-page=25'
# one record + its references
curl -s 'https://api.openalex.org/works/W4399425460' | jq '{title, cited_by_count, referenced_works, related_works}'
```
Note: abstracts come back as `abstract_inverted_index` (word→positions), not plain text — reconstruct if needed.

**Valyu** (`x-api-key`, not Bearer). Semantic recall, academic-scoped:
```bash
curl -s -X POST 'https://api.valyu.ai/v1/deepsearch' \
  -H "x-api-key: $VALYU_API_KEY" -H 'Content-Type: application/json' \
  -d '{"query":"<natural-language question>","search_type":"proprietary","included_sources":["valyu/valyu-arxiv"],"max_num_results":10}' \
  | jq '.results[] | {title, url, content}'
```
`search_type`: `all` | `web` | `proprietary`. Drop `included_sources` and use `"all"` for broad recall; keep `valyu/valyu-arxiv` (and/or `valyu/valyu-pubmed`) for academic. `max_num_results` 1–20. Results are in `.results[]`.

## Procedure, per question

1. **Query at mechanism-class grain — deliberately coarser than the concretized question.** A fully-instantiated query ("RLVR over math/code/instruction-following with optimizer reset at boundaries, held-out tool-call eval") returns nothing and the agent reports "looks novel" — manufactured false novelty from over-specification. Search the *mechanism* ("optimizer reset plasticity sequential RL", "task-boundary reset continual RL"), then compare hits back against the fine question. **Decompose fine, query coarse, compare fine.**

2. **Terminology-harvest loop.** After each retrieval, extract the vocabulary *those authors* use for the phenomenon, add novel terms to the working glossary, re-query with them. Do **not** rely on a static synonym list — you cannot pre-generate the alias for a concept you've never seen named, so harvest it from the literature itself. This loop *is* how the terminology problem gets solved.

3. **Walk the graph.** From strong hits, expand via OpenAlex backward (references) and forward (cited-by). Cluster.

4. **Dispatch deep-read subagents** on the **nearest N candidates by semantic proximity** to the question. Trigger on proximity, **not** on a pre-guessed "this is 90% done" — doneness is the subagent's *output*, not its entry condition (if you could cheaply tell it was done, you'd already have done the read). Subagents fit here: a deep read is a fat context chunk best isolated, and candidates fan out in parallel. If the active tool policy does not allow subagents, do the same deep reads sequentially in the main context and say so; never replace this step with abstract-only summaries.

5. **Run an adversarial nearest-neighbor check.** For each promising delta, search for the paper that would most likely kill it. In the synthesis, distinguish:
   - prior work that already answers the exact outcome,
   - prior work that answers an adjacent outcome,
   - prior work that uses the same intervention but for a different causal question,
   - prior work that creates a confound the proposed project must control.

6. **For scalar-predictor projects, test sufficiency rather than correlation.** Require the map to say whether prior work only reports a monotone correlation, or whether it actually matches the scalar and tests residual effects. Look specifically for endpoint-vs-path distinctions, local-vs-cumulative metrics, matched-reward controls, and held-out future-learning probes.

### Deep-read subagent — return this exact schema
```
- citation: <title, authors, arXiv/DOI id>
- what they actually did: <2–3 sentences>
- overlap with the target question: <what of the question this paper already answers>
- residual gap: <what the target question still owns that this paper does not cover>
- closest-to-killing result: <the result that most threatens the target question, if any>
- evidence: "<ONE load-bearing quoted sentence from the abstract/paper, under 15 words>"
```
Every "this was mostly done in [X]" claim **must** carry the quoted sentence + id. An overlap claim without a backing quote is a hallucinated cite — drop it.

## Stopping criterion (saturation) — defined here

A further round is warranted while a round is still surfacing **new terminology** or **new adjacent questions** not yet decomposed. **Stop when the glossary and question-set saturate** (a round adds nothing new). The loop references this definition; do not redefine it elsewhere.

## Synthesis output (emit to chat, then pause)

Present as the user's decision surface — this is what makes their chime-in informed rather than reactive:

- **Frontier map** — nearest neighbors; established vs contested.
- **Your delta, per question** — classify as *settled*, *largely done*, *known-question / unclaimed-measurement*, *open-but-risky*, or *open*. Never a bare yes/no. "Genuinely new" is only appropriate after this classification and a forward-citation walk; otherwise say "not killed by nearest neighbors" or "the residual delta appears unclaimed."
- **Assumptions the framing injected** — carried from Phase 1, so the user can catch narrowing.
- **Saturation status** — saturated, or what a next round would chase.
- **Candidate next-round questions** — the reframes the search surfaced.

Then stop and hand back to the user.
