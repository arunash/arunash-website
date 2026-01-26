# Add Sharp Money Collective to Your Networth Sheet

## 🎯 Quick Setup (5 Minutes)

You already have the sheet! Just add these 5 new tabs:

**Your Sheet:** https://docs.google.com/spreadsheets/d/1cQYozw6ENaen_xwdeP86I0E6cJGuNMM_8ZnlYkJpljQ/

---

## 📋 Add These 5 Tabs

### Tab 1: "Meta"
Click **+** at bottom → Name it "Meta"

**Add this data:**
| Field | Value |
|-------|-------|
| Last Updated | 2026-01-25 21:00:00 |
| Day | 1 |
| Challenge Start | 2026-01-25 |
| Challenge End | 2026-02-24 |

---

### Tab 2: "Stats"
Click **+** at bottom → Name it "Stats"

**Add this data:**
| Metric | Value |
|--------|-------|
| Working Capital Total | 119.00 |
| Working Capital Available | 19.00 |
| Working Capital Pending | 100.00 |
| Starting Bankroll | 140.00 |
| Current Value | 140.00 |
| Total Return | 0.00 |
| Total Return % | 0.00 |
| Active Bets | 4 |
| Settled Bets | 0 |
| Win Rate | - |
| Deployment Rate | 0.16 |

---

### Tab 3: "Positions"
Click **+** at bottom → Name it "Positions"

**First row (headers):**
ID | Title | Type | Platform | Position | Amount | Entry Price | Contracts | Potential Profit | Profit % | Settlement | Est Prob | Market Prob | Risk | Reasoning

**Data rows:**
| ID | Title | Type | Platform | Position | Amount | Entry Price | Contracts | Potential Profit | Profit % | Settlement | Est Prob | Market Prob | Risk | Reasoning |
|----|-------|------|----------|----------|--------|-------------|-----------|------------------|----------|------------|----------|-------------|------|-----------|
| unemployment-jan26 | January 2026 Unemployment Rate >4.5% | short | Kalshi | YES | 10.00 | 0.20 | 50 | 40.00 | 400 | 2026-02-06 | 0.375 | 0.20 | low | Economist consensus forecasts 4.5%, market only pricing 20% chance |
| payrolls-jan26 | January 2026 Nonfarm Payrolls ≤70k | short | Kalshi | NO on >70k | 10.00 | 0.41 | 24.4 | 14.40 | 144 | 2026-02-06 | 0.75 | 0.41 | low | JPMorgan forecasts only 25k/month Q1, market overpricing upside |
| openai-ipo | OpenAI IPO Before Jun 1 2027 | long | Kalshi | YES | 50.00 | 0.61 | 82 | 32.00 | 64 | 2027-06-01 | - | 0.61 | high | Speculative bet on OpenAI IPO timing. 17-month timeline |
| jony-ive | Jony Ive Device: Clip-on | long | Kalshi | Clip-on | 50.00 | 0.42 | 119 | 69.00 | 138 | TBD | - | 0.42 | very-high | Pure speculation on product form factor |

---

### Tab 4: "Events"
Click **+** at bottom → Name it "Events"

**First row (headers):**
Date | Time | Description

**Data rows:**
| Date | Time | Description |
|------|------|-------------|
| Next Week | - | +$100 capital deposit arrives • Deploy 20-30% into new positions |
| 2026-02-06 | 8:30 AM ET | BLS Jobs Report → Unemployment & Payrolls bets settle • Max profit: +$54.40 |
| 2026-02-11 | - | CPI Inflation Data Release • Potential new opportunities |
| 2026-02-24 | - | Challenge Period Ends • Performance Review |

---

### Tab 5: "Scenarios"
Click **+** at bottom → Name it "Scenarios"

**First row (headers):**
Name | Emoji | Total Profit | Final Bankroll | Return %

**Data rows:**
| Name | Emoji | Total Profit | Final Bankroll | Return % |
|------|-------|--------------|----------------|----------|
| Best Case (All Win) | 🎯 | 155.40 | 295.40 | 111 |
| Short-Term Only (Feb 6) | 📊 | 54.40 | 194.40 | 39 |
| Worst Case (All Lose) | ⚠️ | -121.00 | 19.00 | -86 |

---

## ✅ Deploy the Dashboard

Once you've added the 5 tabs:

1. **Upload to your server:**
   - `sharp-money-collective-sheets.html` → rename to `sharp-money-collective.html`

2. **Update the main site:**
   - Edit `index.html` (tabbed version)
   - Change the iframe src from `/sharp-money-collective.html` to the new Sheets version

3. **Done!** Your dashboard now reads from Google Sheets

---

## 🔄 Daily Updates (9 PM Check-ins)

### What I'll Do:
1. Open your Google Sheet
2. Update row values in "Positions" tab (new bets, settlements)
3. Update "Stats" tab (working capital, returns)
4. Update "Meta" tab (Last Updated, Day number)
5. Save (auto-saves)

### What Happens:
- Your website fetches the latest data every 5 minutes
- Changes appear automatically
- No uploads, no deploys!

---

## 🎨 Test It Locally First

```bash
open /Users/arunash/arunash-website/sharp-money-collective-sheets.html
```

Should show your portfolio loaded from Google Sheets!

---

## 📝 Quick Copy/Paste for Sheets

**For easy setup, I can:**
1. Create a Google Apps Script that auto-populates these tabs
2. Or give you a CSV to import

Want me to create the script?

---

*Ready to add the tabs? Takes about 5 minutes!*
