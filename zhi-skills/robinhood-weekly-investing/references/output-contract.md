# Weekly Output Contract

Create one self-contained HTML decision cockpit at `reports/YYYY-Www.html`. Start from `../assets/weekly-report-template.html` and preserve its visual system unless the user requests a redesign. Its core path must be readable in five minutes, with audit detail available without crowding the decision.

## HTML Cockpit

Keep the primary reading path around 1,400 words or fewer, excluding the note-entry controls, verbatim broker disclosures, and collapsed source notes. Use plain language, responsive layout, visible focus states, and no external network dependencies; the loopback report-notes service is the only local runtime dependency. Keep three to six decision-relevant primary-source links visible inline; put the complete source list in collapsed audit detail.

Show, in order:

1. **Verdict and decision requested:** what the user must decide now.
2. **Learn first:** one concise concept tied directly to this week's decision.
3. **User notes response:** when the inbox is non-empty, answer its comments and questions without treating them as approval.
4. **Market and AI-complex regime:** a visible, dated top-down view of the S&P 500, Nasdaq, volatility, AI-value-chain breadth, current news, and separate sentiment states. Do not bury this in audit details.
5. **Business-quality and technical-moat view:** history, earned niche, customer job, strongest substitute, replaceability, moat evidence and half-life, management, reinvestment runway, five-to-ten-year durability, and valuation realizability. Organize the conclusion around ownership quality; use finance as supporting evidence.
6. **Portfolio at a glance:** value, buying power, weights, concentration, open orders, current-week sell turnover, and current-day cash-funded purchases.
7. **What changed:** only thesis-relevant company, technology, policy, macro, industry, and news changes; distinguish event date from publication date.
8. **Holding decisions:** hold, add, trim, or exit for every current holding. Each holding card must include its owner-quality conclusion and sector/regime read-through or explicitly say neither applies.
9. **Proactive theme screen:** universe size, Wave 1 coverage, finalists, and why key alternatives lost. Each finalist card must distinguish technology quality, business durability, and investment attractiveness at current expectations.
10. **Research coverage and dissent:** a compact visible summary or collapsed section showing the seven Wave 2 lenses for each potentially actionable finalist, source ancestry, missing evidence, material disagreements, narrative and crowding context, and whether cross-examination changed a candidate's status.
11. **Plan:** zero to three ideas, including thesis-based sells and staged rotations.
12. **Bull versus bear:** the load-bearing claim, strongest evidence on each side, and `survived`, `failed`, or `unresolved` status.
13. **Risk and mechanics:** proposed sell turnover, daily cash-funded purchase total, post-trade weights, event risk, tax uncertainty, and staging constraints.
14. **Decision control:** exact approval or next-review instruction.

The visible market section must state an exact as-of time or latest completed session; the exact SPX/S&P 500 and NDX/Nasdaq benchmark or clearly labeled proxies; VIX or another named volatility measure; consistent 1-, 4-, and 12-week SPY/QQQ or benchmark returns; and a disclosed 15-to-25-name liquid U.S. AI-value-chain sample with equal-weight mean, median, breadth above 20- and 50-session averages, and dispersion. Show three to five dated market/sector news deltas, separate S&P 500, Nasdaq, and AI sentiment states, limitations, and the portfolio read-through. Put sample membership and detailed method in the audit; never call the custom sample an index.

The visible owner section must answer, in plain language: how the business reached its niche; who pays and why; what customers would use instead; what is actually hard to reproduce; how long the edge may last; how management reinvests; why the company should still operate and grow in five to ten years; and what operational path must occur for today's P/E or other valuation to be realized. `Great technology`, `durable business`, and `attractive investment` are separate judgments. For pre-profit companies, show milestones and financing needs rather than forcing mature-company ratios.

Include one report-specific message field near the end of the page. It must load and save `reports/YYYY-Www.notes.json` through the loopback-only report-notes service at `127.0.0.1:43129`, debounce writes briefly, and show `Loading`, `Saving`, `Saved`, or a specific unavailable state. Do not use file pickers, clipboard handoffs, browser storage, or browser automation. Treat the sidecar as user-owned and never overwrite it while generating or revising the report.

Place the full source list, detailed evidence, rejected-screen notes, and compact research-coverage audit inside accessible `<details>` sections. The coverage audit must state which lanes were independently delegated; show lane, as-of date, strongest signal, strongest counterevidence, source class, and status; identify common source ancestry and unresolved evidence gaps; and summarize only decision-relevant dissent. Include a concise outside-intelligence ledger with author, date, access status, disclosed conflict or position, and `fact`, `estimate`, `opinion`, `rumor`, or `sentiment` tag. Do not copy raw subagent transcripts or paid research into the report or durable memory. Keep a few load-bearing primary-source links inline. Preserve broker alerts and market-data disclosures verbatim; never hide a blocking alert.

If Xiaohongshu is unavailable, the visible sentiment section must show the actual error class and exact user repair. Distinguish network/sandbox failures from authentication, captcha, IP block, signature, and upstream errors; do not silently omit the lane. When it works, show only the sampled belief divergence and limitations in the visible report, with search terms, sample details, and note identifiers in the audit. Xiaohongshu remains `P3 social discovery/sentiment`, never a factual or trade-confirmation source.

Link the public ticker dossier for each holding and finalist when one exists. The weekly HTML remains the portfolio decision artifact; a ticker dossier is the reusable company-research artifact and must not contain account or order context.

## Trade Ticket

For every actionable order include:

- numbered action, symbol, and portfolio role;
- exact side, quantity or dollar amount, type, price, market-hours setting, and time in force;
- estimated and maximum notional;
- current and proposed weight;
- weekly sell-turnover percentage and daily cash-purchase cap consumed;
- plain-language thesis, strongest bull and bear evidence, valuation assumption, horizon, invalidation, and next review;
- when the bounded exploratory rule is used, label the ticket `exploratory`, name its single unresolved non-safety evidence gate, show the 3% portfolio cap, and state that no further add is allowed before review;
- company, macro, concentration, liquidity, event, and tax risks;
- source dates and as-of time;
- every Robinhood alert;
- `market_data_disclosure` verbatim.

Do not call a proposal actionable when Robinhood reports a blocking alert. For a staged cash-account rotation, label the later buy `pending sell fill and fresh review`; never imply the sell approval also approves the buy.

## Compact Durable Artifacts

- `strategy-memory/weeks/YYYY-Www.md`: roughly 350 words or fewer.
- `strategy-memory/index.json`: compact index with summary and report links.
- `strategy-memory/task-queue.json`: unresolved cross-session actions only; derive dated outcome grading from the index rather than duplicating it here.
- `reports/YYYY-Www.notes.json`: user-owned message about that report; read the latest report sidecar before research and never interpret it as trade approval.
- `strategy-memory/user-notes.json`: tiny user-owned comment and question inbox; read every run and never interpret as trade approval.
- The HTML report is the analysis artifact. Do not duplicate it into either memory file.

## Ticker Research Library

- `research-library/index.json`: compact lookup table with status, themes, coverage, material-update date, next review due, and current file links.
- `research-library/tickers/SYMBOL/dossier.md`: current public long-horizon synthesis, normally under 1,200 words.
- `research-library/tickers/SYMBOL/sources.jsonl`: one stable record per original source or relevant site; add new sources and revise only corrected metadata or verification state.
- `research-library/tickers/SYMBOL/snapshots/YYYY-Www.md`: material dated research delta, not a copy of the weekly report.
- `research-library/tickers/SYMBOL/artifacts/`: full generated ticker analyses or permitted/user-provided supporting files, created only when needed.

Update only materially changed tickers. Preserve historical snapshots, deduplicate source ancestry, record unread or paywalled work as a lead, and never save copied paid content or raw subagent transcripts.

Each current dossier must keep the reusable business story ahead of the weekly market story: causal company history, niche and customer job, competitive map and strongest substitute, technical/product truth, moat components and half-life, management and capital allocation, durability and reinvestment runway, owner economics, valuation-realizability requirements, falsification tests, and open evidence gaps. Weekly price action, exact portfolio context, and trade mechanics do not belong in the dossier.

## Chat Handoff

Return only:

- one-sentence verdict;
- a clickable absolute link to the HTML report;
- the exact decision requested.

Do not repeat the full report in chat.

## Approval Footer

When actionable reviewed orders exist, state exactly:

- Reply `go` or `yes` to approve all actionable orders exactly as previewed.
- Reply `go 2` or a comma-separated list to approve selected order numbers.
- Questions and vague acknowledgments are not approval.
- Stale or changed orders require a new review and approval.
