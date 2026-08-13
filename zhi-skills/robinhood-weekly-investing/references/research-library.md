# Ticker Research Library

Keep reusable public company research in `research-library/`, separate from compact strategy state and weekly portfolio reports.

## Layout

```text
research-library/
├── index.json
└── tickers/
    └── SYMBOL/
        ├── dossier.md
        ├── sources.jsonl
        ├── snapshots/YYYY-Www.md
        └── artifacts/                 # create only when an artifact exists
```

Use `research-library/shared/<topic>/` only when one policy, macro, technical, or industry artifact materially applies to several tickers. Store it once and reference it from ticker dossiers rather than copying it.

## Promotion And Retention

Create a ticker folder when the symbol is a current holding, a Wave 2 finalist, explicitly named by the user, or repeatedly survives screening with material reusable research. Do not create folders for every superficial Wave 1 mention.

Update a folder only for material evidence, a completed research lane, a changed thesis or invalidation, a due review, or a durable user question. Price movement alone is not a material research update.

- Keep `dossier.md` as the current public-research synthesis, normally under 1,200 words and never above 2,000.
- Append one `snapshots/YYYY-Www.md` file for a material weekly update; keep it under 600 words and never above 900.
- Keep historical snapshots immutable except for explicit factual corrections. Update the dossier prospectively.
- Mark dormant tickers `archived` in the index; do not delete their research history.
- Store full generated ticker analyses, tables, or user-provided files under `artifacts/` and point to the newest relevant one from the index. Do not store raw subagent transcripts.

## Dossier Contract

Start from `assets/ticker-dossier-template.md`. Include:

- identity, business role, and mandate themes;
- current long-horizon bull, bear, load-bearing assumption, invalidation, and confidence limits;
- technology and product truth;
- owner economics and valuation framework;
- policy, macro, industry, news, and sentiment state;
- unresolved questions and next review trigger;
- links to dated snapshots and source IDs.

Keep the dossier public-only. Never include account identity, ownership status, position size, cost basis, tax lots, buying power, order details, turnover, or approval state. Portfolio conclusions belong in the weekly HTML and compact strategy memory.

## Source Ledger

Store one JSON object per original source in `sources.jsonl`. Use a stable namespaced `source_id`; record symbol, title, URL, publisher, publication and event dates, retrieval date, access state, P0-P3 tier, claim type, disclosed conflict, original-source ancestry, verification state, short note, and optional local artifact path.

- One company release repeated by ten articles is one evidence source.
- A paywalled, login-only, partial, or unavailable item remains a lead unless its relevant claim is independently verified.
- Never bypass access controls or save copied paid articles, screenshots, tables, or long excerpts.
- Save a local source document only when it is user-provided, public-domain, an official public record, or clearly permitted. Record the local path in the ledger.
- Persist original synthesis and citations, not copyrighted source text.

## Stateless Read Order

At startup:

1. run `scripts/validate_research_library.py <workspace-root>`;
2. read `research-library/index.json` without loading every dossier;
3. identify due entries from `next_review_due`;
4. after confirming the Agentic holdings, read only matching dossiers plus due, user-named, and current-finalist dossiers;
5. read only the source-ledger entries needed for the current claims;
6. give subagents only the relevant public ticker folder or sanitized extracts, never strategy memory or account artifacts.

After research, the main agent deduplicates sources, writes the dated snapshot, updates the canonical dossier and index, and validates again. Advance `next_review_due` even when no material thesis change occurred; do not create a content-free snapshot.
