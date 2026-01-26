# Sharp Money Collective - Google Sheets Setup

## 🎯 Overview

Your portfolio data lives in a Google Sheet. The dashboard reads from it automatically. I update the sheet during our 9 PM check-ins, and your site updates instantly.

---

## 📊 Step 1: Create Your Google Sheet

### Option A: Copy This Template (Fastest)

1. **Go to:** https://docs.google.com/spreadsheets/d/1ABC123/copy
   *(I'll create a template and share the link)*

2. **Click:** "Make a copy"

3. **Rename:** "Sharp Money Collective - Portfolio Data"

### Option B: Create From Scratch

1. Go to https://sheets.google.com
2. Create new spreadsheet: "Sharp Money Collective - Portfolio Data"
3. Create these sheets (tabs):
   - `Meta` - Portfolio metadata
   - `Stats` - Current stats
   - `Positions` - Active bets
   - `Events` - Upcoming timeline
   - `Scenarios` - Outcome scenarios

---

## 🔧 Step 2: Make Sheet Public

1. **Click "Share"** (top right)
2. **Change access:**
   - "Anyone with the link" → **Viewer**
3. **Click "Copy link"**
4. **Extract Sheet ID** from URL:
   ```
   https://docs.google.com/spreadsheets/d/1ABC123XYZ456/edit
                                              ↑↑↑↑↑↑↑↑↑↑↑
                                              This is your Sheet ID
   ```
5. **Save this Sheet ID** - you'll need it for the dashboard

---

## 📋 Step 3: Structure Your Sheets

### Sheet 1: "Meta"
| Field | Value |
|-------|-------|
| Last Updated | 2026-01-25 21:00:00 |
| Day | 1 |
| Challenge Start | 2026-01-25 |
| Challenge End | 2026-02-24 |

### Sheet 2: "Stats"
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

### Sheet 3: "Positions"
| ID | Title | Type | Platform | Position | Amount | Entry Price | Contracts | Potential Profit | Profit % | Settlement | Est Prob | Market Prob | Risk | Reasoning |
|----|-------|------|----------|----------|--------|-------------|-----------|------------------|----------|------------|----------|-------------|------|-----------|
| unemployment-jan26 | January 2026 Unemployment Rate >4.5% | short | Kalshi | YES | 10.00 | 0.20 | 50 | 40.00 | 400 | 2026-02-06 | 0.375 | 0.20 | low | Economist consensus... |
| payrolls-jan26 | January 2026 Nonfarm Payrolls ≤70k | short | Kalshi | NO on >70k | 10.00 | 0.41 | 24.4 | 14.40 | 144 | 2026-02-06 | 0.75 | 0.41 | low | JPMorgan forecasts... |
| openai-ipo | OpenAI IPO Before Jun 1 2027 | long | Kalshi | YES | 50.00 | 0.61 | 82 | 32.00 | 64 | 2027-06-01 | - | 0.61 | high | Speculative... |
| jony-ive | Jony Ive Device: Clip-on | long | Kalshi | Clip-on | 50.00 | 0.42 | 119 | 69.00 | 138 | TBD | - | 0.42 | very-high | Pure speculation... |

### Sheet 4: "Events"
| Date | Time | Description |
|------|------|-------------|
| Next Week | - | +$100 capital deposit arrives |
| 2026-02-06 | 8:30 AM ET | BLS Jobs Report → Unemployment & Payrolls settle |
| 2026-02-11 | - | CPI Inflation Data Release |
| 2026-02-24 | - | Challenge Period Ends |

### Sheet 5: "Scenarios"
| Name | Emoji | Total Profit | Final Bankroll | Return % |
|------|-------|--------------|----------------|----------|
| Best Case (All Win) | 🎯 | 155.40 | 295.40 | 111 |
| Short-Term Only (Feb 6) | 📊 | 54.40 | 194.40 | 39 |
| Worst Case (All Lose) | ⚠️ | -121.00 | 19.00 | -86 |

---

## 🔗 Step 4: Get Your Sheet ID

From your sheet URL:
```
https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit
```

Copy `YOUR_SHEET_ID_HERE`

---

## 💻 Step 5: Update the Dashboard

Edit `sharp-money-collective-sheets.html` and replace `YOUR_SHEET_ID_HERE`:

```javascript
const SHEET_ID = 'YOUR_SHEET_ID_HERE';  // ← Paste your Sheet ID here
```

---

## 🚀 Step 6: Deploy

Upload to your server:
- `sharp-money-collective-sheets.html` → rename to `sharp-money-collective.html`

Done! Your dashboard now reads from Google Sheets.

---

## 🔄 Daily Updates (9 PM Check-ins)

### What I Do:
1. Open your Google Sheet (you share edit access with me)
2. Update rows in "Positions" sheet
3. Update values in "Stats" sheet
4. Update "Meta" → Last Updated timestamp
5. Save (auto-saves)

### What Happens:
- Dashboard checks every 5 minutes for updates
- New data appears automatically
- No file uploads, no deploys, nothing!

---

## 🎨 Sharing Access with Me

1. **Click "Share"** in your sheet
2. **Add:** claude-smc@anthropic.com *(or whatever email I should use)*
3. **Permission:** Editor
4. **Notify:** No (uncheck)

Or just keep it view-only and manually update yourself!

---

## ✨ Benefits

✅ **Zero deploys** - I update the sheet, site updates automatically
✅ **Version history** - Google Sheets tracks every change
✅ **Mobile editing** - You can edit from your phone
✅ **Collaboration** - We can both see/edit
✅ **Backup** - Google handles backups
✅ **No code** - Pure data updates

---

## 🔧 Advanced: Automation

### Google Apps Script Auto-Update
You can even automate updating the sheet from our markdown tracker:

```javascript
function updateFromMarkdown() {
  // Fetch betting_tracker.md from GitHub
  // Parse it
  // Update sheet cells
  // Runs on schedule
}
```

Want me to build this?

---

*Ready to create your sheet? I'll walk you through it!*
