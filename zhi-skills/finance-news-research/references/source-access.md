# Source Access Contract

Use the least invasive route that supports the claim. Access behavior and terms can change, so verify current state when a source is material.

## General Access Ladder

1. Find the canonical URL through web search or the publisher's own index.
2. Read publisher-provided title, author, date, summary, disclosure, and feed metadata for discovery.
3. Read every section visibly rendered through the normal web interface. A global paid badge or sign-in control is not the cutoff; stop at the first actual paywall region and record its heading.
4. Use subscriber content only through the user's legitimate signed-in browser or an explicitly authorized newsletter message.
5. Stop at a paywall, bot challenge, `403`, or `429`; record the limitation and find primary evidence elsewhere.

Never use alternate renderers, text mirrors, cached copies, feed payloads, or page-source fields to expose text hidden by the publisher's normal access boundary.

## SemiAnalysis

- Discovery queries: `site:semianalysis.com TICKER topic` and `site:newsletter.semianalysis.com/p TICKER topic`.
- The newsletter publication feed at `https://newsletter.semianalysis.com/feed` may be used only for title, author, date, canonical link, and public-description discovery. Ignore any feed body beyond what the canonical page visibly permits.
- Public newsletter pages can contain a substantial preview followed by a paid boundary. Read and use all normally rendered sections before that boundary, record `partial`, and name the first blocked heading. Do not discard readable sections merely because the header says `Paid` or offers `Sign in`.
- Full paid work requires the user's legitimate SemiAnalysis subscription in a normal signed-in browser. When the user has designated Chrome, use that Chrome extension session first. Never read or transfer the cookie. Record the page `login_only` and note whether it was subscriber-visible. A newsletter delivered to an authorized mailbox is a fallback that may be minimally summarized by the main agent and labeled `user_provided`.
- SemiAnalysis terms prohibit systematic or automated collection. Do not crawl the archive or automate article-body extraction. Link: `https://semianalysis.com/terms-and-conditions/`.
- Tag original measured technical or supply-chain work with visible methods as `P1`; tag interpretive essays without independently collected evidence as `P2`. Verify company-specific facts and investment implications separately.

## Seeking Alpha

- Discovery queries: `site:seekingalpha.com/article TICKER topic bull`, then repeat with `bear`, `risk`, or the disputed assumption.
- Publisher-provided feeds are discovery-only: latest analysis `https://seekingalpha.com/feed.xml`, transcripts `https://seekingalpha.com/sector/transcripts.xml`, and market news `https://seekingalpha.com/market_currents.xml`.
- Search and public shells may reveal title, author, date, summary bullets, teaser text, and analyst disclosure. Record `partial` with `metadata-only` or `preview-only` in the note; do not say the article was read.
- Direct automated article fetches may return `403`, and the site may require JavaScript and cookies. Full content is usable only if it appears in the user's legitimate signed-in browser session. Never scrape, export cookies, or reconstruct the article from snippets.
- Seeking Alpha terms prohibit robots, scraping, harvesting, and navigation circumvention. Link: `https://about.seekingalpha.com/terms`.
- Usually tag an article `P2`. Extract the author's thesis, assumptions, cited evidence, disclosed position, and strongest falsifier; verify every load-bearing fact with primary material.

## Yahoo Finance And Yahoo News

- Discovery query: `site:finance.yahoo.com/news TICKER topic`, but prefer the named original publisher once identified.
- Yahoo frequently syndicates Reuters, Business Wire, GlobeNewswire, and other outlets. The Yahoo copy and original story are one evidence lane. Record the original publisher, author, and canonical event source.
- Yahoo pages can rate-limit with `429`. Yahoo's terms prohibit automated collection without prior permission, so do not scrape pages, crawl tickers, or build an archive from Yahoo. Use search discovery and a small number of normal-interface reads; if blocked, stop and follow the original publisher.
- A Yahoo video transcript can establish what a named speaker said when the timestamp and speaker are clear. It does not verify the underlying claim.
- Aggregated or syndicated facts inherit the role of the original source. Opinion pieces remain `P2`; unattributed summaries with no ancestry are `reject`. Terms: `https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html`.

## Podscripts And Podcast Transcripts

- Start with `https://podscripts.co/podcasts/all-in-with-chamath-jason-sacks-friedberg/` for the All-In archive. Search narrowly by company, person, policy, or technology; do not crawl the full archive.
- Public episode pages currently expose timestamped transcripts without a login. No public API or explicit bulk-use permission was identified, so use a small number of decision-relevant pages through the normal interface and persist no transcript body.
- Record show, episode, episode date, speaker, timestamp, transcript provider, and the official audio or show link when available. Separate host opinion, guest claim, prediction, and advertisement.
- Treat the transcript as possibly imperfect automatic speech recognition. It is primary evidence only for the approximate words attributed to a speaker and `P2` evidence for an investment proposition. Verify names, numbers, dates, and substantive claims elsewhere.
- If Podscripts is unavailable, use the official podcast feed, publisher transcript, or video transcript. Transcribe a single relevant user-accessible episode only when justified; label the result generated and preserve uncertainty.

## Newsletter And Mail Intake

- Mail access is private even when the newsletter discusses public companies. A public-research subagent must not browse the mailbox.
- With explicit user authorization, the main agent may search only for the named publication or episode, read only relevant messages, and pass a sanitized claim note to the research lane.
- Record publisher, subject, author, sent date, canonical link, access as `user_provided`, and whether the claim was independently verified.
- Never persist the raw message, forwarding headers, recipient data, tracking URLs, credentials, or paid body in the public ticker library.

## Minimum Claim Record

For every decision-relevant item capture: publication date, event date, author or speaker, title, canonical URL, access state, source role, disclosed incentive, paraphrased claim, cited evidence, counterevidence, original ancestry, verification state, and the next primary check.
