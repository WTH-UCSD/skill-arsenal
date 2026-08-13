# Adaptation Sources

This skill synthesizes ideas from the following public projects without installing their incompatible runtime assumptions or copying their report text.

| Source | Adopted | Changed or rejected |
| --- | --- | --- |
| [Claude Equity Research](https://github.com/quant-sentiment-ai/claude-equity-research) | Fundamentals, catalysts, valuation scenarios, technical context, risk, dated sources | Removed forced exact figures, options-flow requirements, analyst-target dependence, and institutional jargon when evidence is missing. |
| [stock-trading-agents-light](https://github.com/LeoYeAI/openclaw-master-skills/tree/main/skills/stock-trading-agents-light) | Layered information gathering, independent bull and bear work, bounded cross-examination, and sentiment as a separate context lane | Replaced Tushare and OpenClaw APIs with public-source research plus Robinhood MCP; preserved `HOLD / NO TRADE`; rejected unverified social sentiment or technical analysis as thesis, forced directional calls, a decision-manager subagent, and two-round debate bloat. |
| [Anthropic Financial Services](https://github.com/anthropics/financial-services) | Staged theme-to-industry-to-peer-to-shortlist research, specialist leaf workers, and human sign-off | Adapted specialist workers to public-only research lanes; kept shortlist selection, portfolio synthesis, private account context, and every broker action in the main agent. |
| [TradeMemory](https://github.com/mnemox-ai/tradememory-protocol/tree/master/tradememory-plugin/skills/trading-memory) | Dated research snapshots as episodic evidence, current ticker dossiers as semantic memory, due reviews as prospective memory, plus behavioral drift and confidence calibration | Removed dependency on its MCP and rejected recall that automatically prioritizes profitable trades. Similar losing and winning contexts must both surface, and reusable public company research stays separate from private portfolio state. |
| [Trading Analysis Dashboard Template](https://github.com/nexu-io/open-design/tree/main/plugins/_official/examples/trading-analysis-dashboard-template) | Dense information hierarchy, risk cockpit, signal-to-order separation, honest unknown placeholders | Uses a self-contained five-minute HTML decision cockpit with collapsed audit detail; visual polish never substitutes for evidence. |

When updating this skill, revisit the upstream projects for new ideas but preserve the local account boundary, review-first order flow, long-horizon rules, and outcome-audit integrity.
