# Sharp Money Collective - Auto-Update System

## 🎯 Overview

Your SMC dashboard updates **automatically** from `betting_tracker.md`. One command syncs to both Google Sheets AND JSON.

## 📁 File Structure

```
arunash-website/
├── sharp-money-collective-sheets.html   ← Google Sheets-powered dashboard
├── sharp-money-collective-dynamic.html  ← JSON-powered dashboard
├── smc-data.json                        ← Data file (auto-generated)
├── smc-update                           ← UNIFIED UPDATER (run this!)
├── update-smc-sheets.py                 ← Sheets-only updater
├── update-smc-data.py                   ← JSON-only updater (legacy)
└── AUTO-UPDATE-README.md                ← This file

~/smc-update                             ← Symlink for quick access
```

---

## ⚡ Quick Commands

```bash
# Update both Google Sheets AND JSON (recommended daily workflow)
~/smc-update

# Preview changes without writing
~/smc-update --dry-run

# Update only Google Sheets
~/smc-update --sheets

# Update only JSON file
~/smc-update --json
```

**Google Sheet:** https://docs.google.com/spreadsheets/d/1cQYozw6ENaen_xwdeP86I0E6cJGuNMM_8ZnlYkJpljQ

---

## 🚀 Quick Start (3 Steps)

### Step 1: Deploy the Dynamic Dashboard

Replace your current `sharp-money-collective.html` with the dynamic version:

```bash
cd /Users/arunash/arunash-website
cp sharp-money-collective.html sharp-money-collective-static-backup.html  # backup
cp sharp-money-collective-dynamic.html sharp-money-collective.html        # use dynamic version
```

### Step 2: Upload to Your Server

Upload these files:
- `sharp-money-collective.html` (the dynamic version)
- `smc-data.json` (the data file)

### Step 3: Update Only JSON Going Forward

Every day at 9 PM check-ins, I'll update **only** `smc-data.json` with new:
- Position data
- Portfolio stats
- Upcoming events
- Scenarios

---

## 🔄 How Updates Work

### Manual Update (During Daily Check-ins)

I'll edit `/Users/arunash/arunash-website/smc-data.json` directly with new data.

Then you sync it to your server:

**Option A: Manual Upload**
```bash
# Just upload the updated smc-data.json via FTP/cPanel
```

**Option B: Git Auto-Deploy** (Recommended)
```bash
cd /Users/arunash/arunash-website
git add smc-data.json
git commit -m "Update SMC portfolio - Day X"
git push origin main

# Then your hosting auto-pulls from GitHub
# (requires GitHub Actions or webhook setup)
```

**Option C: Rsync/SCP** (If you have SSH access)
```bash
# Add this to your ~/.ssh/config
# Host arunash
#   HostName your-server.com
#   User your-username

# Then sync with one command:
rsync -av smc-data.json arunash:/path/to/website/
```

---

## 🤖 Automation Options

### Option 1: GitHub Actions Auto-Deploy (Best)

Create `.github/workflows/deploy-smc.yml`:

```yaml
name: Deploy SMC Data
on:
  push:
    paths:
      - 'smc-data.json'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to server
        uses: easingthemes/ssh-deploy@main
        env:
          SSH_PRIVATE_KEY: ${{ secrets.SERVER_SSH_KEY }}
          REMOTE_HOST: ${{ secrets.SERVER_HOST }}
          REMOTE_USER: ${{ secrets.SERVER_USER }}
          TARGET: /path/to/website/
          SOURCE: "smc-data.json"
```

### Option 2: Cron Job (If hosting supports)

```bash
# On your server, add to crontab:
*/5 * * * * curl https://raw.githubusercontent.com/arunash/arunash-website/main/smc-data.json -o /path/to/website/smc-data.json
```

### Option 3: Python Auto-Update Script

```bash
# I update the markdown tracker as usual
# Then run:
python3 update-smc-data.py

# This converts betting_tracker.md → smc-data.json
# Then auto-push to GitHub
```

---

## 📋 Daily Workflow (9 PM Check-ins)

### What We Do:
1. Analyze markets
2. Update `/Users/arunash/betting_tracker.md` with new positions/stats
3. Run `~/smc-update` to sync everything

### What Happens Automatically:
1. `smc-update` reads `betting_tracker.md`
2. Writes to Google Sheets (live dashboard updates)
3. Writes to `smc-data.json` (backup/alternative)
4. Dashboard shows updated data within 5 minutes (no deploy needed)

---

## 🎨 JSON Data Structure

```json
{
  "meta": {
    "lastUpdated": "ISO 8601 timestamp",
    "day": 1,
    "challenge": { "startDate": "...", "endDate": "..." }
  },
  "portfolio": {
    "workingCapital": { "total": 119, "available": 19, "pending": 100 },
    "performance": { "startingBankroll": 140, "currentValue": 140, ... },
    "stats": { "activeBets": 4, "settledBets": 0, ... }
  },
  "positions": {
    "shortTerm": [ { "id": "...", "title": "...", ... } ],
    "longTerm": [ { "id": "...", "title": "...", ... } ]
  },
  "scenarios": [ { "name": "Best Case", "totalProfit": 155.40, ... } ],
  "upcomingEvents": [ { "date": "...", "description": "..." } ]
}
```

---

## ✅ Benefits

- ✅ **No more HTML edits** - Just update JSON
- ✅ **Auto-refresh** - Dashboard checks for updates every 5 minutes
- ✅ **Version control** - Git tracks all data changes
- ✅ **Easy updates** - I can update during our check-ins
- ✅ **Mobile-friendly** - Same responsive design
- ✅ **Fast loading** - JSON is tiny (~5-10 KB)

---

## 🔧 Troubleshooting

### Dashboard shows "Loading..." forever
- Check if `smc-data.json` is accessible at `/smc-data.json` on your server
- Open browser console (F12) to see errors
- Verify JSON is valid at https://jsonlint.com

### Data doesn't update
- Check file timestamp: `ls -l smc-data.json`
- Force refresh in browser: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache

### Want to test locally?
```bash
cd /Users/arunash/arunash-website
python3 -m http.server 8000
# Open http://localhost:8000/sharp-money-collective.html
```

---

## 📞 Next Steps

**Recommended Setup:**
1. Deploy dynamic HTML + JSON today
2. Set up GitHub Actions auto-deploy (I can help with this)
3. During daily check-ins, I update JSON only
4. Changes go live automatically within 5 minutes

**Questions?** Ask during our 9 PM check-in tomorrow!

---

*Last updated: 2026-01-25 (added Google Sheets auto-write)*
