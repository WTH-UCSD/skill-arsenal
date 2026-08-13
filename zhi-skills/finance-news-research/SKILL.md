---
name: finance-news-research
description: Research financial news, specialist reports, newsletters, opinion platforms, and podcast transcripts with source-specific access rules, paywall and cookie handling, rate-limit discipline, provenance, claim extraction, deduplication, and primary-source verification. Use for public-company news intelligence, per-ticker research updates, or an investing subagent lane involving SemiAnalysis, Seeking Alpha, Yahoo Finance, Podscripts, fund letters, podcasts, or similar sources.
---

# Finance News Research

Build a compact, source-traced intelligence packet. This is a public-information research lane, not a portfolio decision, recommendation, sizing exercise, or broker workflow.

## Load The Source Contract

Read `references/source-access.md` before opening specialist reports, newsletters, aggregators, or transcripts. Re-check the live page and publisher terms when access behavior may have changed.

## Hard Boundaries

- Never access a brokerage account, portfolio artifact, strategy memory, order, credential, or unrelated private data.
- Never bypass a paywall, login, bot challenge, robots rule, or publisher restriction. Do not inspect, export, store, or replay cookie values or session tokens.
- A search result, feed entry, cached copy, or page source may expose text that the publisher's normal interface does not render. Do not read, quote, summarize, or persist that hidden body. A global `Paid` label or visible sign-in button does not make the visibly rendered article sections unreadable; stop only at the actual rendered paywall boundary.
- Do not bulk crawl, mirror, or save full articles, newsletters, or transcripts. Save original synthesis and source metadata only.
- Treat a search snippet as discovery metadata, not as proof that the article was read.
- Keep quotations exceptional and short: at most 25 words from any one non-lyrical source. Prefer paraphrase with a direct link.
- Treat every outside claim as a lead until its factual core is verified against an appropriate primary source.

## Research Procedure

1. **Frame the delta.** State the ticker or theme, decision-relevant questions, search cutoff from the prior run, current timestamp, and a wider 90-day thesis window. Inspect the existing ticker dossier and source ledger first when provided.
2. **Discover broadly.** Search company filings, regulators, technical papers, named specialist work, original reporting, analytical opinion, transcripts, and narrative sources. Search both the bull and bear formulation of the question.
3. **Use the access ladder.** Prefer an official public page or publisher-provided discovery feed. Use a normal browser only for a small number of material pages. Use subscriber content only through the user's legitimate signed-in session or explicitly authorized newsletter message; never handle the credential itself.
4. **Classify access honestly.** Use the ticker-library values `public`, `partial`, `paywalled`, `login_only`, `unavailable`, or `user_provided`. Classify at the section level: a mostly readable article with a later paywall is `partial`, and the note must name the first blocked heading. Put details such as preview-only, metadata-only, subscriber-visible, `403`, `429`, or bot challenge in the note. Never imply review of content beyond that state.
5. **Extract claims, not prose.** For each material item record publisher, author or speaker, title, URL, publication date, underlying event date, retrieval time, source role, access state, disclosed position or incentive, original-source ancestry, the paraphrased claim, cited support, strongest counterevidence, and the next primary check.
6. **Trace and deduplicate.** Syndicated copies, articles repeating the same filing, and podcasts discussing one report are one evidence lane. Link them to the earliest accessible original and retain later items only when they add independent evidence or a distinct attributable interpretation.
7. **Verify.** Test load-bearing facts against filings, regulators, customer or supplier evidence, standards, recognized benchmarks, original data, or direct company materials. A transcript proves what a speaker said, not that the statement is true.
8. **Synthesize without voting.** Explain what changed, what bulls and bears believe, which assumptions remain unresolved, and which claims deserve primary verification. Stop once the material delta, strongest accessible bull and bear, access failures, and up to three primary checks are covered; do not chase every article. Do not average opinions or turn source volume into confidence.

## Authentication And Rate Limits

- Search and publisher-provided discovery metadata come first; direct raw HTTP scraping is not a default access method. For authenticated publisher pages, prefer the user's designated Chrome extension session; use authorized newsletter mail only as a fallback.
- If a material page requires login, use only a browser session in which the user has legitimately signed in. If no such session exists, mark it inaccessible and continue unless the source is indispensable.
- If a subscribed newsletter is available through an explicitly authorized mail connector, the main agent—not a public-research subagent—should locate only the relevant message, extract the minimum claim summary, and pass a sanitized note into this lane. Never scan unrelated mail or persist the newsletter body.
- On `403`, a bot challenge, or a request for JavaScript/cookies, stop automated fetching and use the permitted browser or metadata path. On `429`, honor `Retry-After` when visible, do not retry in a loop, and switch to the original publisher or another evidence lane.
- Record access failures. Missing access reduces confidence; it is not permission to reconstruct the article from snippets or reposts.

## Source Roles

Assign the role to the item, not permanently to the publisher:

- `P0 primary`: filings, regulators, government records, court records, original papers, standards, and recognized benchmark results.
- `P1 independent`: named original reporting, teardown, interview, supply-chain work, or specialist analysis with visible methods and independently collected evidence.
- `P2 analytical`: newsletters, platforms, fund letters, podcasts, and commentary whose factual inputs require tracing.
- `P3 narrative`: attributable discussion used only for discovery, expectations, disagreement, or sentiment.
- `reject`: unattributed aggregation, copied stories, promotional work without disclosure, inaccessible snippets presented as reviewed work, or claims with no verification path.

## Subagent Output Contract

Return a concise packet to the main agent with these sections:

1. `Scope and coverage`: ticker/theme, windows searched, sources attempted, and access failures.
2. `Material news delta`: only developments that could change thesis, valuation inputs, timing, or falsification.
3. `Strongest outside bull and bear`: independent arguments, their evidence, incentives, and unresolved assumptions.
4. `Transcript intelligence`: speaker, timestamp, attributable claim, why it matters, and verification state.
5. `Claim ledger`: claim, counterevidence, original ancestry, access, source role, and the ticker-library verification state: `primary`, `verified`, `corroborated`, `unverified`, `conflicted`, or `stale`.
6. `Primary verification queue`: up to three next checks, ordered by decision importance.
7. `Source rows`: JSONL-ready metadata for the main agent to write. Never write directly to a ticker folder.

Each source row should contain `source_id`, `symbol`, `title`, `url`, `publisher`, `published_at`, `event_date`, `retrieved_at`, `access`, `tier`, `claim_type`, `disclosed_position_or_conflict`, `original_source_id`, `verification_status`, `note`, and `local_artifact_path`. Use only the access and verification enums above; use `fact`, `estimate`, `interpretation`, `opinion`, `rumor`, or `sentiment` for `claim_type`; format all dates as `YYYY-MM-DD`; and keep `local_artifact_path` null unless the main agent created a permitted artifact.

End with `coverage_sufficient`, `coverage_partial`, or `coverage_blocked`, followed by one sentence explaining the largest remaining evidence gap. Do not make a trade recommendation.
