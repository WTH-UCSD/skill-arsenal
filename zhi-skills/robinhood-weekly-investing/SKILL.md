---
name: robinhood-weekly-investing
description: Run weekly, long-horizon Robinhood research for an AI-and-technology mandate with proactive screening beyond current holdings, persistent per-ticker public research dossiers, thesis-based sells and staged rotations, compact strategy memory, a five-minute HTML decision cockpit, review-only trade proposals, and explicit user-approved execution. Use for weekly Agentic-account reviews, AI infrastructure, semiconductor, technology, or space equity research, ticker research libraries, strategy outcomes, and trade proposals that must avoid day trading.
---

# Robinhood Weekly Investing

Run one auditable investment-learning cycle per week. Keep research, durable strategy memory, approval, execution, and later evaluation distinct.

## Load The Workflow

Read before acting:

1. `references/research-framework.md` for universe screening, evidence lanes, and decision gates.
2. `references/memory-protocol.md` before reading or writing `strategy-memory/`.
3. `references/research-library.md` before reading or writing `research-library/`.
4. `references/output-contract.md` before creating the weekly HTML report or trade tickets.
5. `$finance-news-research` before running either outside-research/current-news lane.
6. `$xiaohongshu-cli` before running the narrative, emotion, sentiment, and crowding lane.
7. `references/inspirations.md` only when modifying this skill.

When `strategy-memory/index.json` exists, run:

```bash
python3 <skill-dir>/scripts/validate_strategy_memory.py <workspace-root>
```

Stop actionable trade work if validation fails. Repair only an unambiguous structural error and report it.
When `research-library/index.json` exists, also run:

```bash
python3 <skill-dir>/scripts/validate_research_library.py <workspace-root>
```

After validation, identify the latest report from the strategy index and read its same-named `reports/YYYY-Www.notes.json` sidecar, then read the legacy `user_notes_file`, `strategy-memory/task-queue.json`, every week with a due, still-null outcome, and the ticker research index. Identify due ticker reviews without loading every dossier before reading the account or starting new research.

Immediately after those cheap local-only resume checks, run the blocking Robinhood MCP readiness gate before any market research, screening, delegation, dossier analysis, or other substantive work. Require authenticated MCP startup and call `get_accounts` only to resolve the unique eligible `Agentic` account. On any startup, OAuth, transport, tool-enumeration, or identity failure, stop substantive work, preserve the exact error, and create or carry one deduplicated repair task. When the user repairs access or resumes the task, repeat this gate first and reuse completed public analysis that is still fresh; do not restart research merely because the connection failed.

## Hard Boundaries

- Robinhood MCP readiness is a hard, repeatable gate, not a late diagnostic. Run it after minimal local resume checks and before substantive research; repeat it after repair/resumption and immediately before broker review or placement. A prior pass never authorizes a later broker action.
- Resolve the unique active cash brokerage account named `Agentic` with `agentic_allowed=true` using `get_accounts`. Use that call only for identity resolution.
- Never read, display, or interact with another account. Stop on ambiguity. Never expose or persist a full account number.
- Review every existing equity holding, even when it falls outside the new-buy mandate, because it may warrant a hold, trim, or exit.
- Proactively screen beyond current holdings every week.
- Treat the company as a business before treating it as a security. For every holding and finalist, explain its history, the niche it earned, the customer job, why customers choose it, the strongest substitute, how replaceable it really is, the moat's evidence and likely half-life, management and capital-allocation behavior, and why the business should still operate and grow in five to ten years. Do not use financial ratios as a substitute for this work.
- Synthesize with a long-term-owner and technical-builder mindset: distinguish a clever technology, a durable company, and an attractive investment at today's price. Be open to bounded technical and execution risk when the edge, milestones, financing path, and falsification tests are explicit; do not require every technology business to resemble a mature consumer franchise.
- Test whether valuation can be earned rather than merely reporting a P/E. State the revenue, margin, reinvestment, dilution, cash-conversion, and terminal-expectation path the current price requires; compare it with company history, industry structure, technical runway, and credible substitutes. If those inputs are unknowable, mark valuation realizability `unresolved`.
- Before interpreting any holding or candidate, build a dated top-down market and AI-complex regime. Show the exact S&P 500 and Nasdaq benchmark used, current index/volatility levels, consistent 1-, 4-, and 12-week performance, a transparent cross-sector AI-stock breadth sample, material market and sector news since the prior run, and separate broad-market, Nasdaq, and AI sentiment states. Label proxies and timestamps; never call a custom sample an index.
- Make that market, news, breadth, and sentiment layer visible near the top of the HTML report. Do not bury it in the audit or leave the reader to infer it from isolated ticker sections. Every holding and finalist must state the relevant sector/regime read-through or explicitly say there is none.
- Restrict new buys to liquid U.S.-listed equities with a material thesis in technology, AI compute or infrastructure, semiconductors, data-center power/cooling/networking, or space. Use broad-market securities only as benchmarks, never as proposals.
- Exclude crypto, options, futures, margin, shorts, ETFs, OTC securities, penny stocks, and illiquid names from proposals.
- Produce at most one weekly plan containing zero to three ideas.
- Permit at most one exploratory cash-funded buy or add per weekly plan when the long-horizon thesis, mandate, liquidity, portfolio role, current regime, and broker mechanics pass but exactly one named non-safety evidence gate remains unresolved. Cap it at the lesser of 3% of current portfolio value, verified buying power, the remaining daily cash-buy cap, and any tighter concentration limit. State the missing evidence, event risk, falsification test, and next review; do not add again until the evidence is reviewed. Never apply this exception to MCP/account identity, mandate, liquidity/tradability, leverage or derivatives, buying power, a blocking broker alert, or exact user approval.
- Require a thesis horizon of at least three months; default to twelve months or longer when supported.
- Never use an intraday move, chart pattern, social-media excitement, analyst-target change, or single headline as the thesis. Use intraday data only for execution quality.
- Analyze sentiment, crowding, and outside commentary as evidence about what the market believes, never as proof that the belief is true or as a standalone reason to trade.
- Require the narrative, emotion, sentiment, and crowding subagent to sample Xiaohongshu through `$xiaohongshu-cli`. Xiaohongshu access is permanently read-only: allow only a suppressed `xhs status --yaml` authentication check followed by `xhs search` and `xhs read`. Never call any other `xhs` command, including login, comments, feed, hot, user or account browsing, like or undo, favorite or unfavorite, comment or reply, follow or unfollow, post, delete, or any future operation outside the allowlist.
- Diagnose Xiaohongshu failures instead of collapsing them into `authentication unavailable`. A DNS, sandbox, or network-permission error gets one normal-network retry when available; `not_authenticated` or `session_expired` gets a visible user action asking the user to run `xhs login`; captcha, IP block, signature, and upstream errors each retain their actual code and remedy. Never execute login. If access remains unavailable, show the missing lane and exact repair in the visible report, continue with other public sentiment sources, and create or carry one deduplicated unresolved task until a later status/search/read succeeds. Do not silently omit the lane.
- Treat disclosed fund holdings as lagged and incomplete. Never copy a fund trade or infer its cost basis, hedge, horizon, or rationale from a 13F filing.
- Never force activity or use same-day round trips.
- Do not make a new buy actionable when the top-down market and AI-complex snapshot is missing, stale, or too thin to assess sector breadth and crowding. On a non-trading day, use the latest completed session and say so.
- Permit a sell for a broken thesis, excessive valuation, concentration reduction, or mandate cleanup. A sell may fund an in-scope buy only when the sell independently passes its own decision gates.
- Cap weekly sell turnover at the configured percentage of starting portfolio value. Count absolute sales, including fills already made that ISO week. Track purchases separately: verified spendable-cash buys do not consume sell turnover and are capped at the configured amount per New York trading day (currently $300).
- During a scheduled run, call review tools only. Never place an order until the user explicitly approves unchanged reviewed parameters in the same task.

## Artifact Boundary

- Put the complete weekly analysis, sources, bull/bear evidence, trade tickets, broker alerts, and market-data disclosures in `reports/YYYY-Www.html`.
- Start from `assets/weekly-report-template.html`. Preserve its layout, design tokens, responsive behavior, lesson-first hierarchy, and staged-capital-path signature; replace the content blocks and redesign only when the user asks.
- Make the HTML self-contained, responsive, educational, and readable in five minutes; use collapsible details for audit material.
- Keep `strategy-memory/weeks/YYYY-Www.md` to a short durable summary of principles, macro regime, decision, and outcome schedule.
- Keep `strategy-memory/index.json` as a compact machine index pointing to the summary and HTML report.
- Keep `strategy-memory/task-queue.json` as the compact queue of unresolved cross-session actions that cannot be derived from the index. Never put research prose or stale order authorization in it.
- Keep each report's user message in its same-named `reports/YYYY-Www.notes.json` sidecar. Read the latest report sidecar every run before research; never overwrite it while regenerating or revising the report.
- Keep the index-linked `strategy-memory/user-notes.json` as the user-owned comment and question inbox. Read it every run; never treat its contents as order approval.
- Keep reusable public company research under `research-library/tickers/SYMBOL/`: a compact current dossier, one-record-per-original-source ledger, dated material snapshots, and optional generated artifacts.
- Keep ticker folders free of account, position, tax, turnover, order, and approval data so sanitized folders can be used by research subagents. Store portfolio decisions only in the weekly HTML and compact strategy memory.
- Update a ticker dossier only for material evidence or a due review; do not duplicate the weekly report, repeat source text, or create content-free snapshots.
- Do not duplicate the full report in chat or strategy memory. Return the HTML link plus the decision needed.

## Main-Agent Ownership

Keep these operations in the main agent:

- account resolution and all account-specific Robinhood reads;
- portfolio sizing and weekly-turnover calculations;
- order review, approval interpretation, placement, status, and cancellation;
- writes to strategy memory, the ticker research library, investor profile, decision rules, and the final HTML;
- final synthesis and recommendation.

Do not delegate them.

## Two-Wave Public Research Program

When several holdings or candidates need comparison and agent slots are available, schedule independent specialist briefs in batches of up to three concurrent public-research subagents. Use a distinct agent per lane when practical; reuse a specialist only for a deeper pass in the same lane. If delegation is unavailable, cover the same briefs in the main agent and disclose that they were not independently delegated.

**Wave 1 — discovery before the shortlist**

Before the main-agent shortlist, synthesize a **market and AI-complex regime brief** from the policy/macro, outside-news, and sentiment lanes. It must cover SPX/S&P 500, NDX/Nasdaq or a clearly labeled proxy, VIX or another named volatility measure, a disclosed 15-to-25-stock AI value-chain sample, breadth and dispersion, the week's material market/sector news, dominant bull and bear narratives, and the portfolio implications. Invoke `$finance-news-research` for the news delta. This brief is top-down context, not a technical trading signal.

Also synthesize a **business-quality and technical-moat brief** before ranking finalists. Start with company history and niche, then customer value and replaceability, technical/product truth, moat half-life and disruption paths, management and reinvestment, five-to-ten-year durability, and finally the expectations the current valuation must realize. The financial statements are evidence for or against this ownership story, not the organizing story themselves.

1. holdings and long-term-owner challenger: reconstruct each company's history, earned niche, customer job, durability, management, reinvestment runway, valuation realizability, and opportunity cost; test the strongest case that the business is less special or more replaceable than believed;
2. technology and value-chain mapper: search the full mandate, explain where technical value accrues, compare real substitutes and switching paths, estimate moat half-life, and surface under-covered liquid U.S.-listed candidates and obvious rejects;
3. government-policy and macro scout: map export controls, tariffs, subsidies, tax credits, procurement, energy and permitting, rates, currencies, and geopolitical exposure;
4. outside-research and news scout: invoke `$finance-news-research` to find original filings, reporting, technical research, independent analysis, newsletters, and podcast transcripts; trace recycled claims to their source and return its sanitized intelligence packet;
5. narrative, emotion, and crowding analyst: measure what bulls and bears currently believe, how that changed, and where price expectations look euphoric, fearful, or divided.

The main agent applies mandate, liquidity, tradability, and evidence gates and selects the finalists.

**Wave 2 — diligence after the shortlist**

Every candidate that may become actionable receives all seven finalist briefs; a watch candidate may stop early only with the failed gate recorded:

1. business history, earned niche, customer job, replaceability, management, durable economics, and five-to-ten-year owner quality;
2. product, architecture, benchmarks, roadmap, ecosystem, substitutes, switching paths, technical moat, and moat half-life;
3. financial statements, accounting quality, owner earnings, cash conversion, balance sheet, dilution, and reinvestment capacity;
4. valuation realizability: expectations embedded in price, required growth/margins/cash conversion, capital structure and financing needs, historical and industry feasibility, and bull/base/bear paths;
5. company-specific policy, macro, industry structure, supply chain, and dated catalysts;
6. outside research and current news: invoke `$finance-news-research` for the strongest independent bull and bear work, material news delta, transcript intelligence, access failures, verification queue, and source ancestry;
7. narrative, emotion, sentiment, and crowding, with data lags, sampling limits, and divergence from verified fundamentals.

Keep first-pass work independent: do not reveal the intended trade, preferred winner, or another lane's report. For an idea that may become actionable, run one short sanitized cross-examination round on the most important disagreement. Require dated sources, claim and counterevidence, missing facts, the load-bearing assumption, strongest disconfirming fact, and `advance`, `avoid`, or `watch` with a confidence reason. An unresolved load-bearing conflict remains non-actionable; the exploratory-risk rule applies only to one explicitly bounded non-safety evidence gap, never a known thesis break. The sentiment specialist is the exception: it returns only sentiment state, crowding state, narrative-versus-fundamentals divergence, data limitations, and timing risk; it never recommends or supplies fundamental confidence. Repeated citations to the same underlying release are one evidence source, not independent confirmation.

Official filings and regulators remain the factual backbone. The outside-research lanes must follow `$finance-news-research`, including its source-specific access states, cookie and paywall boundaries, rate-limit discipline, transcript treatment, quotation limit, and newsletter-mail privacy boundary. Specialist sources such as SemiAnalysis may add technical context; independent platforms such as Seeking Alpha, Yahoo Finance, X, newsletters, podcasts, and fund letters or holdings may surface hypotheses and sentiment. Record author, date, original-source ancestry, disclosed conflicts or positions, and access limits. Never bypass a paywall, reproduce paid analysis, or promote an unverified secondary claim into the thesis.

Give subagents only public tickers, themes, neutral questions, sanitized public dossier content, and approximate exposure bands when essential. Direct them only to the relevant public ticker folder, never strategy memory or reports containing account context. Never provide account identifiers, balances, exact holdings or dollars, tax lots, broker screenshots, credentials, order parameters, or write access. The main agent owns the shortlist, conflict resolution, research-library writes, sizing, final recommendation, artifacts, and every broker action. An unresolved load-bearing conflict makes the idea non-actionable.

## Weekly Cycle

1. **Resume user context and durable work.** Validate compact strategy memory and the ticker research library; read the latest report's same-named notes sidecar, then the legacy user-notes inbox, and visibly answer any non-empty message or question; load every active task; derive due 1-, 4-, 12-, or 52-week outcomes; and identify due ticker reviews from the research index. Advance, close, or explicitly carry every triggered task before starting a new weekly screen. Never rewrite a pre-decision thesis after seeing results.
2. **Load confirmed context.** Apply the AI/technology mandate and active rules. Ask at most one focused question only when no conservative, rule-based size is defensible.
3. **Pass the blocking MCP readiness gate.** Require authenticated Robinhood MCP startup and resolve only the unique eligible `Agentic` account with `get_accounts`. Stop before substantive research on any startup, OAuth, transport, tool-enumeration, or identity failure; preserve the exact error and one deduplicated repair task. After repair or resumption, repeat this gate first and reuse still-fresh completed public analysis.
4. **Build the top-down regime and read the account.** Before interpreting individual stocks, capture the latest public S&P 500, Nasdaq, volatility, AI-breadth, sector-news, and sentiment context using the consistent methodology in `references/research-framework.md`. Then gather current Agentic value, buying power, positions, sellable shares, open/recent orders, current-week fills, tax lots, and realized P&L when available.
5. **Review all holdings first.** Read each matching public ticker dossier and due snapshot before new web research, then reconstruct the business history and niche, test customer value and replaceability, technical truth, moat half-life, management, reinvestment, durability, owner earnings, and whether the current valuation can be realized. Only then classify hold, add, trim, or exit. Connect each conclusion to the top-down regime without letting market sentiment replace the company thesis. Do not exempt an off-mandate holding from review.
6. **Discover before shortlisting.** Search a current, liquid in-theme universe beyond the portfolio. Reuse existing dossiers for recurring candidates and run Wave 1 independently across holdings and owner quality, technology and value chain, policy and macro, outside research and news, and sentiment and crowding. The main agent records why finalists survived, why obvious candidates were rejected, and how the sector regime changed those comparisons.
7. **Research finalists.** Apply all seven Wave 2 briefs to every potentially actionable finalist using the primary-source and outside-research policy. Create a ticker folder for a holding, Wave 2 finalist, user-named ticker, or repeat survivor with material reusable research. Stop early only when a gate fails and record why.
8. **Challenge each thesis.** Produce bull and bear briefs, deduplicate common source ancestry, and run at most one sanitized cross-examination round for a potentially actionable idea. Require the bear to identify the strongest credible replacement, disruption path, management failure, and valuation assumption that cannot be earned; require the bull to show evidence of customer dependence, moat durability, and a feasible per-share value-creation path. Mark the load-bearing claim `survived`, `failed`, or `unresolved`.
9. **Build the plan.** Consider buys, sells, and rotations. Include current-week fills, maximum notionals, post-trade weights, concentration, buying power, sellable shares, and tax uncertainty.
10. **Handle cash-account rotations.** Zero buying power does not end the analysis. A justified sale consumes weekly sell turnover; after proceeds become verified buying power, a later purchase consumes the separate daily spendable-cash purchase cap. Review the sell first, then refresh buying power before reviewing the buy and requesting separate approval. Never call a blocked, unreviewed buy actionable.
11. **Review exact actionable orders.** Preserve every broker alert and the required market-data disclosure verbatim. Treat blocking alerts as non-actionable.
12. **Write artifacts before approval.** Reuse `assets/weekly-report-template.html` for the HTML report; update only materially changed ticker dossiers, source ledgers, snapshots, and optional artifacts; create the compact weekly summary and index entry; then validate both durable stores.
13. **Present the cockpit.** Return the HTML link, one-sentence verdict, and exact decision requested.

## Approval And Execution

- Immediately before an exact broker review and again before placement, repeat the Robinhood MCP readiness and unique-Agentic identity gate. If it fails, stop; keep any still-fresh public analysis and exact error, but do not infer account state or reuse a stale preview.
- Bare `yes` or `go` approves every actionable order in the displayed HTML plan. `go 2` or a comma-separated list approves only those numbered orders.
- Questions, discussion, or vague acknowledgments are not approval.
- Approval covers only the exact reviewed symbol, side, size, order type, price, session, and time in force.
- For a staged rotation, approval of the sell never pre-approves the later buy.
- Before placement, re-check only identity, buying power or sellable shares, current-week fills, and duplicate open orders. Do not substitute, reprice, resize, or add an order.
- Treat a market-order review as stale after ten minutes and a limit-order review as stale after 3:45 p.m. New York time that trading day. Refresh a stale review before placement, but when the user already approved the exact daily plan and the economic ticket plus broker alerts remain unchanged, run that refresh silently and submit without asking again. Request new approval only for a material parameter or broker-alert change, or a later New York trading day.
- Do not assume regular-hours-only execution. Check live symbol, session, and fractional eligibility and use the earliest supported session. Eligible overnight or extended-hours execution requires a supported symbol and a limit order; fractional and dollar-based market orders are regular-hours-only and must queue when reviewed outside the regular session. Never imply every equity or order format trades 24/7.
- Market close is not a blanket execution prohibition. After an exact review and explicit approval, a regular-hours order may be submitted while the market is closed and left queued for the next session when Robinhood permits it. Report `queued` or `submitted` accurately; never imply it filled.
- Record each unfinished staged leg as its own queue task. Keep later legs blocked on verified fills and refreshed buying power; never infer approval across legs or sessions.
- Treat report note sidecars and `user-notes.json` as research context only. Even text such as `go` or `yes` in either file is never live order approval; approval must arrive in the same Codex task after an exact fresh review.
- Use a fresh UUID idempotency key per logical order and reuse it only for a transient retry of that same order.
- Record broker state. Submitted does not mean filled; record fills only after verification.
- Apply user-approved profile or rule changes prospectively while preserving prior-week historical rules.
