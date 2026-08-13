# Strategy Memory Protocol

Treat `strategy-memory/` as compact durable strategy state, not a report archive. The complete weekly analysis belongs in `reports/YYYY-Www.html`.

Reusable public company research belongs in `research-library/tickers/SYMBOL/`, not in strategy memory. Strategy memory records why the portfolio acted and when to revisit it; the ticker library records what is known about the company. Keep account, position, order, tax, and approval context out of the ticker library.

## What To Persist

Keep each weekly Markdown summary under roughly 350 words and record only:

- week, lifecycle, and links to the HTML report;
- principles and mandate applied;
- short macro/regime assumptions that affected the decision;
- decision, maximum proposed sell turnover, and same-day cash-funded purchase total;
- exact approved/submitted/filled state when applicable;
- invalidation conditions and next review dates;
- due 1-, 4-, 12-, and 52-week outcomes;
- one durable process lesson.

Do not copy research lanes, candidate tables, source digests, broker disclosures, or the HTML narrative into strategy memory.

When a weekly decision relies on a ticker dossier, store only the decision consequence and review date here. Keep the reusable evidence, source ledger, open company questions, and public research history in the ticker folder.

Keep `index.json` as a compact machine index linking the summary and report. Never store a full account number.

## User Notes Inbox

Keep each report's message in a same-named sidecar: `reports/YYYY-Www.notes.json`. The report's single text area loads and saves that sidecar through the loopback-only report-notes service. The sidecar contains `schema_version`, `report_id`, `report_file`, `updated_at`, and `message`. It belongs to the user: never overwrite it while generating or revising a report.

At the start of every interactive or scheduled run, identify the latest report from `strategy-memory/index.json` and read its sidecar before the task queue, account, or research. When `message` is non-empty, acknowledge and answer it visibly near the top of the new HTML report. Preserve the user's words; do not clear, rewrite, or mark them consumed. The user controls replacement or clearing through that report's text area.

Keep the index-linked `strategy-memory/user-notes.json` as a legacy inbox and read it after the latest report sidecar. Treat all notes as research preferences and questions, never as broker authorization. `go`, `yes`, or order-like language stored in either notes file does not approve a trade because approval must follow a fresh exact review in the same Codex task.

## Stateless Resume Queue

Keep `strategy-memory/task-queue.json` as a compact queue of unresolved work that a later stateless session cannot safely reconstruct from dates alone. Store only identifiers, status, trigger, next action, dependency, report link, and timestamps. Do not store research prose, account numbers, credentials, or broker previews as durable authorization.

At the start of every interactive or scheduled run:

1. validate the strategy memory;
2. read and address the latest report's sidecar, then the legacy index-linked user notes;
3. load every `open`, `blocked`, or `scheduled` queue task;
4. derive outcome work from each null `outcomes` entry whose `review_due_dates` value is today or earlier;
5. check triggered order-state or staged-leg tasks before beginning a new weekly screen;
6. advance, close, or explicitly carry every triggered task with a fresh timestamp and evidence link.
7. before substantive research, run the authenticated Robinhood MCP readiness gate and resolve only the unique eligible `Agentic` account with `get_accounts`.

Treat that MCP check as blocking and repeatable. An OAuth, startup, transport, tool-enumeration, or identity failure stops new research and broker work, records the exact failure in one deduplicated repair task, and leaves completed public analysis intact. After repair or task resumption, repeat the gate first; reuse still-fresh research instead of recomputing it. Repeat the gate again immediately before broker review or placement.

Create separate tasks for separate rotation legs. A later buy stays `blocked` until the funding sell is verified filled and buying power refreshes. A stale broker preview never completes a task and never survives as approval; keep the task open with `requires_fresh_review=true`.

When a task finishes or is cancelled, first record its final state in the linked weekly summary and index, then remove it from the active queue. Outcome review dates stay only in the index to avoid duplication and queue bloat.

## Historical Boundary

Once an approval request is displayed, preserve the decision-time report and summary. Append or create a timestamped report revision for:

- factual corrections;
- changed or stale order reviews;
- approvals and exact order parameters;
- submitted, filled, rejected, or cancelled states;
- outcome checkpoints.

Never rewrite the original thesis after seeing results. Layout migrations requested by the user may move analysis between files, but preserve the decision, timestamps, sources, and report link.

## Outcome Review

At each due horizon, record:

- affected-investment return from a verified fill or decision-time reference;
- SPY return over the same dates as a benchmark only;
- excess return when reliable;
- whether thesis evidence strengthened, weakened, or stayed unresolved;
- process quality independent of profit;
- whether an invalidation condition triggered.

Do not infer causality from one observation. Propose rule changes with sample size and uncertainty; activate them only after user approval.

## Behavioral Drift

Check for rising turnover without stronger evidence, unintended concentration, post-loss thesis rewriting, shorter holding periods, inconsistent approval language, execution slippage, and selective recall. Report drift as a question or proposed rule, not an automatic rewrite.
