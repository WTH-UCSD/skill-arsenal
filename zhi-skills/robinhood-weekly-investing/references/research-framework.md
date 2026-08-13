# Research Framework

Prefer explicit uncertainty to false precision.

## Universe And Candidate Order

1. Establish the same-date S&P 500, Nasdaq, volatility, AI-value-chain breadth, news, and sentiment regime before interpreting individual securities.
2. Review every current holding, whether or not it fits the new-buy mandate, through the business-history, technical-moat, long-term-owner, and valuation-realizability tests below.
3. Proactively screen liquid U.S.-listed equities across:
   - technology and applied AI;
   - AI compute, networking, data-center power, cooling, and electrical infrastructure;
   - semiconductors, manufacturing equipment, memory, and foundry supply chains;
   - launch, satellites, communications, and other space infrastructure.
4. Restrict new buys to that mandate. Use broad-market securities only as benchmarks.
5. Narrow the screen to candidates with a durable business thesis, a defensible technical or customer niche, current primary evidence, adequate liquidity, Robinhood tradability, and a one-sentence explanation.
6. Compare finalists with both current holdings and the strongest rejected alternatives. Do not stop after researching the portfolio.

Reject crypto, ETFs, options, futures, OTC securities, leveraged or inverse products, penny stocks, illiquid names, and businesses whose connection to the mandate is merely promotional.

## Two-Wave Subagent Research

Use independent public-research subagents to widen the search before shortlisting and deepen it afterward. Schedule specialist briefs in batches of up to three concurrent agents. Prefer a distinct agent per lane and reuse a specialist only for a deeper pass in the same lane. The main agent remains the sole portfolio decision-maker and keeps all account, sizing, artifact, and broker work private.

### Wave 1 — Discovery And Challenge

Run before the main agent chooses finalists:

1. **Holdings and long-term-owner challenger**
   - Reconstruct the company's relevant history, how it earned its niche, the customer job, the strongest substitute, switching path, and evidence that the product or relationship is difficult to replace.
   - Test the public thesis, moat half-life, durable economics, reinvestment runway, management and capital allocation, valuation realizability, falsification evidence, and opportunity cost for every holding.
   - State the strongest independent case to hold, add, trim, or exit.
   - Use only qualitative exposure bands such as high, medium, or low when concentration context is necessary.
2. **Technology and value-chain mapper**
   - Map applied AI and software; compute, chips, and equipment; networking, memory, and storage; data-center power, electrical systems, and cooling; nuclear or other relevant power; and launch, satellites, and space communications.
   - Explain where measurable technical and customer value accrues, which alternatives can displace it, and how quickly the edge may decay; propose under-covered liquid U.S.-listed candidates and identify obvious rejects.
3. **Government-policy and macro scout**
   - Examine export controls, sanctions, tariffs, subsidies, tax credits, defense and space procurement, spectrum and launch rules, energy regulation, permitting and interconnection, rates, currencies, commodities, talent policy, and geopolitical dependencies.
   - Distinguish enacted law, final rule, award, proposal, political statement, and litigation. Record jurisdiction, effective date, direct versus second-order exposure, beneficiaries, losers, and what would reverse the effect.
4. **Outside-research and news scout**
   - Search new filings, company and customer disclosures, credible reporting, technical benchmarks and papers, specialist research, independent investor analysis, newsletters, podcasts, fund letters and filings, and relevant X threads since the prior run.
   - Label each item `fact`, `estimate`, `opinion`, `rumor`, or `sentiment`; record author, publication date, event date, original-source ancestry, disclosed position or conflict, and access status.
   - Separate genuinely new information from recycled narratives, corrections, and old events republished as news.
5. **Narrative, emotion, and crowding analyst**
   - Sample both bullish and bearish narratives and state how they changed over the week and over a longer comparison window.
   - Invoke `$xiaohongshu-cli` and follow the parent skill's permanent Xiaohongshu command allowlist. Record the search terms and time, sample size, note IDs or URLs, available publication dates, and ranking or selection limits; treat the sample as `P3 social discovery/sentiment`.
   - If status, search, or read fails, preserve the actual structured error. Retry a network/sandbox failure once with normal network access when available. Otherwise show the exact user repair in the visible report, create or carry one deduplicated unresolved task, and continue with other sources. Never report a network failure as an authentication failure or silently omit Xiaohongshu.
   - Use price response to good and bad news, longer-window price and volume, volatility, short interest, estimate dispersion or revisions, and social or news attention only when reliable and dated.
   - Classify sentiment as euphoric, optimistic, balanced, skeptical, fearful, or capitulating, with confidence and sample limitations. Treat it as expectation and staging context, never business value.

The main agent then applies mandate, liquidity, Robinhood tradability, and evidence gates and selects three to five finalists. The final weekly plan still contains zero to three ideas.

### Wave 2 — Finalist Diligence

Assign seven distinct lenses after the main agent creates the shortlist. Every potentially actionable candidate must receive all seven; a watch candidate may stop early only when the failed gate and missing lanes are recorded.

1. **Business history, niche, and long-term-owner quality:** how the company reached its current position; the customer job and buying reason; strongest substitute and switching path; evidence of irreplaceability rather than assertion; understandable earnings engine; pricing power; recurring or replacement demand; return on incremental capital; management incentives and capital allocation; reinvestment runway; and why the business should still matter and be more valuable in five to ten years. Label pre-profit economics `unresolved` rather than forcing a mature-company conclusion.
2. **Technology and product truth:** architecture, measurable performance and total cost of ownership, benchmarks, roadmap credibility, standards and ecosystem, switching costs, substitutes and open-source risk, manufacturing or supply dependencies, technical kill tests, and moat half-life. A technical edge matters only when it creates durable customer and economic value.
3. **Financial statements and accounting quality:** revenue composition and quality, margins, owner earnings, cash conversion, working capital, balance sheet, debt, dilution or buybacks, customer concentration, maintenance versus growth investment, and GAAP versus adjusted measures. Use finance to test the ownership thesis, not replace it.
4. **Valuation realizability and capital structure:** expectations embedded in the current price; the revenue growth, margins, cash conversion, dilution, reinvestment, and terminal multiple needed to earn today's P/E or other valuation; relevant company history and industry structure; peers with structural differences; bull, base, and bear paths; financing and acquisition needs; no forced price target.
5. **Policy, macro, industry, and catalysts:** company-specific effect of current rules and policy paths, geography and supply chain, rates and currencies, industry structure and competition, customer funding, and dated catalysts with reversal conditions.
6. **External intelligence and current news:** use `$finance-news-research` to collect the strongest bullish, bearish, and technically neutral outside work; what materially changed since the prior run; transcript intelligence; access failures; a source and news ledger; recycled claims; unresolved paywalled leads; strongest falsification; and conditions to avoid, trim, or exit.
7. **Narrative, emotion, sentiment, and crowding:** dominant bull and bear stories, change over consistent 1-, 4-, and 12-week windows, divergence from verified fundamentals, attention and positioning proxies with their lags, and timing or volatility risk.

Each research lane must return:

- dated sources with primary-source ancestry;
- the material claim, supporting evidence, and counterevidence;
- `fact`, `estimate`, `opinion`, `rumor`, or `sentiment` tags for outside claims;
- missing or unknown facts;
- the strongest disconfirming fact and load-bearing assumption;
- `advance`, `avoid`, or `watch`, with a confidence reason;
- at least one concession to supported opposing evidence.

The sentiment lane is the exception: it returns `sentiment_state`, `crowding_state`, `narrative_vs_fundamentals`, `data_lags_and_sampling_limits`, and `timing_assessment`. It must not return `advance`, `avoid`, `buy`, `sell`, or a fundamental confidence score.

### Independence And Cross-Examination

- Do not tell a subagent the intended trade, preferred winner, or desired conclusion. Do not show agents one another's first-pass work.
- Deduplicate evidence by the underlying source. Three articles repeating one company release remain one evidence lane.
- For any candidate that may become actionable, send the relevant lane one short sanitized conflicting claim for a single rebuttal round. A rebuttal must add evidence or concede uncertainty.
- Resolve conflicts against filings, regulators, and other primary evidence. An unresolved load-bearing conflict makes the idea non-actionable. An unresolved secondary issue may remain a watch item or justify a smaller idea only if every decision gate still passes.
- Do not appoint a decision-manager subagent. The main agent owns the shortlist, conflict resolution, portfolio effect, sizing, final synthesis, and broker workflow.
- Give subagents only public tickers, themes, neutral questions, and approximate exposure bands when necessary. Never share account identifiers, balances, exact holdings or dollar amounts, tax lots, broker screenshots, credentials, order parameters, or write access.
- If subagents are unavailable, the main agent must cover the same questions and disclose that the lanes were not independently delegated.

## Evidence Lanes

### Business History, Niche, And Durability

- Give the short causal history: which product, customer, regulation, technical breakthrough, distribution choice, acquisition, or capital cycle created today's position. Avoid a generic corporate timeline.
- Explain who pays, what job they hire the product to do, what failure costs the customer, how the sale is won, and whether demand is recurring, replacement, cyclical, project-based, or subsidized.
- Name the strongest credible substitute, including in-house development, open source, an adjacent architecture, or doing nothing. Describe switching time, qualification, integration, retraining, reliability, regulatory, and total-cost barriers with evidence.
- Decompose the moat into technical/process know-how, IP, data, ecosystem, standards, scale, cost, distribution, customer relationships, regulation, or capital access. State what is genuinely rare, what is merely competent, and the likely half-life of each edge.
- Test five-to-ten-year survival and growth through customer concentration, cyclicality, supply dependence, capital needs, technological discontinuity, regulation, and management succession. A company may be durable without being fast-growing, or technically impressive without being durable.

### Business And Fundamentals

- Explain how the business makes money and what must persist.
- Check revenue composition and growth, margins, free cash flow, working capital, balance-sheet strength, debt, dilution, buybacks, and capital allocation.
- Tie theme-specific metrics—accelerator demand, wafer capacity, data-center megawatts, backlog, launch cadence, or constellation deployment—to cash generation.
- Distinguish GAAP figures from adjusted figures and identify one-time items.

### Valuation And Scenarios

- Use methods appropriate to the business.
- State bull, base, and bear assumptions without inventing a price target.
- Compare with relevant history and peers while explaining structural differences.
- Treat pre-profit or pre-commercial valuation as unresolved unless credible milestones and funding needs support a bounded scenario.
- Reverse the current valuation into operational requirements. State the per-share revenue or earnings growth, margin, reinvestment, dilution, cash conversion, and terminal multiple required over a named horizon, then test whether company history, industry capacity, customer economics, and the technical roadmap make that path plausible. Do not say a P/E is cheap or expensive without explaining how it can or cannot be earned.

### Technology And Product Truth

- Explain the customer problem and the product's role in the technical stack without marketing language.
- Compare measurable performance, total cost, energy use, reliability, roadmap, ecosystem, and switching costs with real substitutes.
- Cross-check vendor claims with customers, suppliers, technical papers, open benchmarks such as [MLCommons](https://mlcommons.org/benchmarks/), standards bodies, and credible domain specialists when available. Require like-for-like workload, hardware, software, batch, power, date, and submitter context for benchmark comparisons.
- Map technical advantage to pricing power, retention, margin, or reinvestment opportunity. Jargon or benchmark leadership alone is not a moat.
- State the moat's likely half-life, three technical kill tests, and the strongest technically credible substitute.

### Long-Term-Owner Quality

- Ask whether an owner could understand the earnings engine, trust management, and hold through a cycle for five to ten years.
- Use Berkshire's [owner-related business principles](https://www.berkshirehathaway.com/2001ar/2001ar.pdf) as questions about economics, management, and per-share value, not as a label or a reason to force mature-company heuristics onto semiconductors, infrastructure, or space.
- Test durability, pricing power, incremental returns, owner earnings, reinvestment runway, capital intensity, dilution, incentives, and capital allocation.
- Distinguish a great technology, a great company, and a great investment at the current price; they are not interchangeable.
- Normalize accounting earnings toward per-share owner economics, including maintenance investment, stock-based dilution, acquisitions, and working-capital needs.
- For pre-profit or pre-commercial companies, state which owner-economics questions remain unknowable.
- Conclude with three separate judgments: `technology quality`, `business durability`, and `investment attractiveness at current expectations`. Do not let strength in one silently stand in for the others.

### Government Policy, Industry, Catalysts, And Macro

- Separate thesis-changing developments from attention.
- Give exact dates for earnings, product ramps, regulatory decisions, launches, debt maturities, and other known catalysts.
- Explain rate, currency, export-control, power, commodity, policy, supply-chain, and cycle exposure when material.
- For government action, record jurisdiction, legal status, effective date, implementation path, direct versus second-order effect, and reversal risk.
- Distinguish award ceiling, obligated amount, cash outlay, backlog, and recognized revenue. Do not forecast elections or offer legal conclusions; scenario-test confirmed policy states.
- Treat a catalyst as timing context, not business value.

Start policy discovery with operative and official sources such as the [Federal Register](https://www.federalregister.gov/), [Regulations.gov](https://www.regulations.gov/), [Congress.gov](https://www.congress.gov/), [BIS](https://www.bis.gov/regulations/ear), [Treasury's outbound-investment program](https://home.treasury.gov/policy-issues/international/outbound-investment-program), [CHIPS for America](https://www.nist.gov/chips), [DOE's data-center resource hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub), [USAspending](https://www.usaspending.gov/), [FRED](https://fred.stlouisfed.org/), and the relevant FCC, FAA, FERC, NASA, NOAA, state utility, court, or procurement record.

### Outside Intelligence And News

- Invoke `$finance-news-research` and follow its source-access contract for specialist reports, newsletters, opinion platforms, aggregators, podcasts, subscriber sessions, mail intake, cookies, paywalls, rate limits, provenance, and its sanitized output packet.
- Search from the prior-run timestamp through the current timestamp, a 90-day thesis window, and older canonical work when relevant. Compare publication date with the date the underlying event occurred.
- Use specialist work such as [SemiAnalysis](https://newsletter.semianalysis.com/about) for technical hypotheses, independent platforms such as [Seeking Alpha](https://about.seekingalpha.com/about) for competing theses, X and other social sources for discovery and narrative sampling, and fund letters or filings such as [Situational Awareness](https://situational-awareness.ai/) for scenario and positioning clues.
- Build a source ledger with author, date, link, access status, disclosed position or incentive, claim type, and original-source ancestry. Never bypass a paywall or imply access to unread material.
- Treat a fund's 13F as a lagged, incomplete long-position snapshot. Never infer cost basis, current ownership, shorts, hedges, horizon, or rationale without separate evidence.
- Extract verifiable claims and test them against filings, regulators, customers, suppliers, benchmarks, or other primary evidence. Do not copy conclusions.
- Return a compact news delta, the strongest independent bull and bear analyses, three leads worth primary verification, and recycled stories that add no evidence—not a link dump.

### Narrative, Sentiment, And Crowding

- Report the dominant bull and bear stories, dispersion, change over consistent 1-, 4-, and 12-week windows, and confidence rather than a single synthetic score.
- Separate narrative evidence from measured market context and identify sample bias, bots, paid promotion, stale reposts, and engagement-driven selection.
- Distinguish short interest from short-sale volume; do not treat fails-to-deliver as proof of abusive shorting, options volume as directional without structure and trade-side context, or delayed fund and insider filings as current positioning.
- Use sentiment to reveal expectations, crowding, emotional risk, and execution sensitivity. It may generate a verification question, monitoring task, or staging warning after fundamental gates pass, but cannot independently make a buy or sell actionable.
- A popular narrative and a repeated source are not independent confirmation.

Use official mechanics references when interpreting positioning, including [FINRA's short-interest explainer](https://www.finra.org/investors/insights/short-interest), [OCC volume and open-interest data](https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/volume-query), the [SEC Form 13F FAQ](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f), and the SEC's [social-media investing warning](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/social-media-stock-scams).

### Market Context

- Timestamp the snapshot. On non-trading days, use the latest completed session and say so.
- Show the exact S&P 500 and Nasdaq benchmarks used, their levels or clearly labeled ETF proxies, VIX or another named volatility measure, and consistent 1-, 4-, and 12-week returns. State whether each benchmark is above or below its 20- and 50-session averages as breadth context, not a signal.
- Maintain a transparent 15-to-25-name liquid U.S.-listed AI value-chain sample spanning semiconductors/compute, networking/power/data centers, and cloud/platform/applied AI. Name every constituent in the audit; report equal-weight mean and median returns, share above 20- and 50-session averages, and cross-sectional dispersion. Never call a custom sample an index.
- Use `$finance-news-research` for material market and AI-sector news since the prior run plus a 90-day thesis window. Cover at least macro/liquidity, demand and supply, policy/competition, and crowding; separate event date from publication date and new evidence from recycled narrative.
- Give separate sentiment states for the S&P 500, Nasdaq, and AI complex using volatility, breadth, dispersion, price response to good and bad news, and explicitly limited public narrative samples. Label inferences and missing positioning data.
- For every holding and finalist, state the relevant sector/regime read-through or explicitly say there is none. The regime may raise or lower the evidence, valuation, and staging bar, but never replaces the company thesis.
- Use weekly or longer price, volume, relative-strength, and drawdown context only to assess regime and execution risk.
- Never turn technical indicators into the thesis.
- Use current bid, ask, spread, and tradability only for reviewed order parameters.

### Portfolio And Personal Finance

- Calculate current and proposed weights, concentration, cash, weekly sell turnover, and same-day cash-funded purchases separately.
- State which existing exposure a buy duplicates or diversifies.
- Surface tax and liquidity unknowns without guessing.
- Classify every sale as broken thesis, valuation trim, concentration rebalance, mandate cleanup, or cash need.
- Allow sale proceeds to fund a buy only when the sale is independently justified.

## Source Policy

Match the source to the claim. Tag each item rather than assigning a permanent rank to a publisher:

1. `P0 primary`: SEC filings, official regulators and government, court records, company filings, standards bodies, original technical papers, and recognized benchmark results;
2. `P1 independent specialist/reporting`: named authors with visible methods, original interviews, supply-chain work, teardowns, or independently collected data;
3. `P2 analytical opinion`: independent platforms, fund letters, long-form theses, newsletters, podcasts, and commentary whose factual inputs still require tracing;
4. `P3 social discovery/sentiment`: attributable X posts and discussions used for leads, disagreement, and narrative temperature, never a load-bearing fact;
5. `reject`: unattributed aggregation, promotional or sponsored work without clear disclosure, copied stories, AI content farms, inaccessible snippets presented as reviewed work, and claims with no verification path.

Attach dates and links to material claims. Record both publication and event dates when they differ. Cross-check load-bearing claims, deduplicate repeated coverage to its original source, and mark unavailable or paywalled evidence as `unknown`. Do not reproduce paid analysis or present a search snippet as if the underlying report was read.

Before searching a tracked ticker, inspect its dossier and relevant `sources.jsonl` entries so new work closes an evidence gap instead of repeating prior research. Re-check freshness before relying on an older source. After synthesis, add only genuinely new original sources, edit an existing record only for corrected metadata or verification state, and preserve the dated snapshot that introduced a material thesis change.

## Adversarial Review

Write independent bull and bear briefs before synthesis.

**Bull brief**

- strongest evidence-backed reasons future value may be underappreciated;
- assumptions required;
- evidence that would increase confidence.

**Bear/falsification brief**

- strongest ways the thesis could fail;
- evidence inconsistent with the bull case;
- conditions for avoid, trim, or exit.

Cross-examine the most load-bearing assumption. Require each side to concede supported opposing evidence and label the claim `survived`, `failed`, or `unresolved`. Debate volume is not evidence.

## Decision Gates

An actionable idea must pass:

- mandate fit for a new buy, or an independently justified reason for a sale;
- understandable business history, niche, customer job, and earnings engine;
- evidence-backed technical/customer advantage, strongest credible substitute, replaceability test, and moat half-life;
- five-to-ten-year durability, management and reinvestment logic, with unresolved facts stated;
- current, sourceable evidence;
- explicit valuation-realizability assumptions showing what growth, margins, cash conversion, dilution, and terminal expectations the current price requires;
- fresh top-down S&P 500, Nasdaq, volatility, AI-breadth, news, and sentiment context;
- bear case accepted as a sized risk;
- intentional portfolio effect;
- horizon of at least three months;
- feasible review within sellable shares, remaining weekly sell turnover, verified spendable cash, and the remaining daily purchase cap;
- buying power for a buy, including proceeds from a completed sell leg.

One bounded exception is allowed: at most one exploratory cash-funded buy or add per weekly plan may carry exactly one unresolved non-safety evidence gate when the core long-horizon thesis, current primary evidence, mandate, liquidity, portfolio role, regime, and broker mechanics otherwise pass. Cap it at the lesser of 3% of current portfolio value, verified buying power, the remaining daily cash-buy cap, and any tighter concentration limit. Name the uncertainty, event risk, falsification test, and review date, and prohibit another add until the evidence is reviewed. Never use this exception for MCP/account identity, mandate, liquidity/tradability, leverage or derivatives, buying power, blocking broker alerts, exact approval, a known thesis break, or an unresolved load-bearing conflict between evidence lanes.

Use `HOLD / NO TRADE` when a hard gate fails or when more than one evidence gate remains unresolved. A zero-cash account may still produce a valid sell or staged rotation; zero buying power alone is not a research conclusion.
