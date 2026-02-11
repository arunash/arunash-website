# Claude Project Context

## General Rules

- Always use real data, never estimated or guessed values. If real data is unavailable (e.g., API rate limited), explicitly tell the user and ask how to proceed rather than substituting estimates silently.

- Prefer the simplest solution that works. When the user asks for logging, tracking, or automation, start with the lightest-weight approach (e.g., Apple Shortcuts, Google Sheets, simple scripts) before proposing complex systems. Ask the user about complexity preference if unclear.

- Do not generate unrequested features, content, or integrations. Only build what the user explicitly asks for. If you think something would be helpful, suggest it briefly and wait for approval before implementing.

## Project Context

This project ecosystem includes: arunash.com (personal site on GoDaddy), CEO Personal OS (iCloud-based), options/wheel strategy dashboards, Sharp Money Collective, and various MCP integrations (Google Sheets, Gmail). When working on any of these, check for existing code and configurations before creating new standalone scripts.

## Data Processing

When working with financial data (PDFs, CSVs), always check file size first. For large PDFs, extract text page-by-page or convert to text/CSV before processing. Never attempt to read entire large PDFs at once.

## Spending Analysis

For spending/transaction analysis: maintain a persistent category mapping file (e.g., `category_overrides.json`) so that transaction categorization corrections (e.g., PremJyotish → Unconscious, exclude OOJO) are remembered across sessions and never need to be re-stated.

## Sharp Money Collective (SMC)

Prediction market portfolio tracker hosted at arunash.com/sharp-money-collective.html

### Key Files
- `smc-data.json` - Portfolio data (positions, stats, scenarios)
- `sharp-money-collective.html` - Dashboard UI that renders from JSON

### Data Structure
```json
{
  "meta": { "lastUpdated": "...", "day": 17 },
  "portfolio": {
    "performance": { "startingBankroll", "realizedProfit", "unrealizedPnL", "currentValue", "totalReturnPct" },
    "stats": { "activeBets", "settledBets", "winRate", "deploymentRate" },
    "positionSummary": { ... }
  },
  "positions": {
    "shortTerm": [...],
    "longTerm": [...],
    "watchlist": [...]
  },
  "scenarios": [...],
  "upcomingEvents": [...]
}
```

### Position Statuses
- `ACTIVE` - Open position with currentPrice and unrealizedPnL
- `WON` / `LOST` - Settled bets with profit field
- `SOLD` - Early exit with exitPrice and profit

### Color Coding
- Green (#4ade80) for wins/profits
- Red (#f87171) for losses
- Always show proper +/- signs on P&L values

### Platforms
- Kalshi - Economic/political events
- Polymarket - Various prediction markets

### Workflow
1. Update prices in `smc-data.json`
2. Commit and push to GitHub
3. Site auto-refreshes from JSON every 5 minutes
