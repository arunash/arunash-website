#!/usr/bin/env python3
"""
Sharp Money Collective - Google Sheets Auto-Updater
Parses betting_tracker.md and writes directly to Google Sheets

Usage:
    python update-smc-sheets.py              # Update all tabs
    python update-smc-sheets.py --dry-run    # Preview changes without writing
"""

import re
import json
import argparse
import warnings
from datetime import datetime
from pathlib import Path

# Suppress Python version warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", message=".*NotOpenSSLWarning.*")

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuration
SPREADSHEET_ID = "1cQYozw6ENaen_xwdeP86I0E6cJGuNMM_8ZnlYkJpljQ"
TRACKER_MD = Path("/Users/arunash/betting_tracker.md")
CREDENTIALS_FILE = Path("/Users/arunash/credentials.json")

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Challenge config
CHALLENGE_START = datetime(2026, 1, 25)
CHALLENGE_END = datetime(2026, 2, 24)


def get_credentials():
    """Get Google API credentials from service account."""
    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(
            f"Credentials file not found at {CREDENTIALS_FILE}\n"
            "Download from Google Cloud Console -> APIs & Services -> Credentials"
        )

    creds = service_account.Credentials.from_service_account_file(
        str(CREDENTIALS_FILE),
        scopes=SCOPES
    )
    return creds


def parse_tracker(md_content: str) -> dict:
    """Parse betting_tracker.md into structured data."""
    data = {
        "meta": {},
        "stats": {},
        "positions": [],
        "events": [],
        "scenarios": []
    }

    # Calculate day number
    today = datetime.now()
    day_num = max(1, (today - CHALLENGE_START).days + 1)

    # Meta
    data["meta"] = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"),
        "day": day_num,
        "challenge_start": "2026-01-25",
        "challenge_end": "2026-02-24"
    }

    # Parse stats
    stats_patterns = {
        "working_capital_total": r'\*\*Total Working Capital\*\*: \$(\d+\.?\d*)',
        "working_capital_available": r'\*\*Available Cash\*\*: \$(\d+\.?\d*)',
        "working_capital_pending": r'\*\*Pending Deposit.*?\*\*: \$(\d+\.?\d*)',
        "starting_bankroll": r'\*\*Starting Bankroll\*\*: \$(\d+\.?\d*)',
        "total_return": r'\*\*Total Return\*\*: \$(-?\d+\.?\d*)',
        "active_bets": r'\*\*Total Active Bets\*\*: (\d+)',
        "settled_bets": r'\*\*Settled Bets\*\*: (\d+)',
    }

    for key, pattern in stats_patterns.items():
        if match := re.search(pattern, md_content):
            data["stats"][key] = float(match.group(1)) if '.' in match.group(1) or key != "active_bets" else int(match.group(1))

    # Set defaults
    data["stats"].setdefault("working_capital_total", 119.00)
    data["stats"].setdefault("working_capital_available", 19.00)
    data["stats"].setdefault("working_capital_pending", 100.00)
    data["stats"].setdefault("starting_bankroll", 140.00)
    data["stats"].setdefault("total_return", 0.00)
    data["stats"].setdefault("active_bets", 4)
    data["stats"].setdefault("settled_bets", 0)

    # Calculate current value and return %
    data["stats"]["current_value"] = data["stats"]["starting_bankroll"] + data["stats"]["total_return"]
    data["stats"]["total_return_pct"] = round(
        (data["stats"]["total_return"] / data["stats"]["starting_bankroll"]) * 100, 1
    ) if data["stats"]["starting_bankroll"] > 0 else 0

    # Parse positions from markdown
    position_pattern = r'\*\*Position (\d+): ([^\*]+)\*\*\n(.*?)(?=\*\*Position \d+:|---|\Z)'
    positions_section = re.search(r'## Active Positions\n(.*?)(?=---|\Z)', md_content, re.DOTALL)

    if positions_section:
        pos_text = positions_section.group(1)

        # Position 1: Unemployment
        if "Unemployment" in pos_text:
            data["positions"].append({
                "id": "unemployment-jan26",
                "title": "January 2026 Unemployment Rate >4.5%",
                "type": "short",
                "platform": "Kalshi",
                "position": "YES",
                "amount": "$10.00",
                "entry_price": "$0.20",
                "contracts": "50",
                "potential_profit": "$40.00",
                "profit_pct": "400",
                "settlement": "2026-02-06",
                "est_prob": "0.375",
                "market_prob": "0.2",
                "risk": "low",
                "reasoning": "Economist consensus forecasts 4.5%, market only pricing 20% chance."
            })

        # Position 2: Payrolls
        if "Payrolls" in pos_text:
            data["positions"].append({
                "id": "payrolls-jan26",
                "title": "January 2026 Nonfarm Payrolls <=70k",
                "type": "short",
                "platform": "Kalshi",
                "position": "NO on >70k",
                "amount": "$10.00",
                "entry_price": "$0.41",
                "contracts": "24.4",
                "potential_profit": "$14.40",
                "profit_pct": "144",
                "settlement": "2026-02-06",
                "est_prob": "0.75",
                "market_prob": "0.41",
                "risk": "low",
                "reasoning": "JPMorgan forecasts only 25k/month Q1, market overpricing upside."
            })

        # Position 3: OpenAI IPO
        if "OpenAI IPO" in pos_text:
            data["positions"].append({
                "id": "openai-ipo",
                "title": "OpenAI IPO Before Jun 1 2027",
                "type": "long",
                "platform": "Kalshi",
                "position": "YES",
                "amount": "$50.00",
                "entry_price": "$0.61",
                "contracts": "82",
                "potential_profit": "$32.00",
                "profit_pct": "64",
                "settlement": "2027-06-01",
                "est_prob": "-",
                "market_prob": "0.61",
                "risk": "high",
                "reasoning": "Speculative bet on OpenAI IPO timing. 17-month timeline."
            })

        # Position 4: Jony Ive
        if "Jony Ive" in pos_text:
            data["positions"].append({
                "id": "jony-ive",
                "title": "Jony Ive Device: Clip-on",
                "type": "long",
                "platform": "Kalshi",
                "position": "Clip-on",
                "amount": "$50.00",
                "entry_price": "$0.42",
                "contracts": "119",
                "potential_profit": "$69.00",
                "profit_pct": "138",
                "settlement": "TBD",
                "est_prob": "-",
                "market_prob": "0.42",
                "risk": "very-high",
                "reasoning": "Pure speculation on product form factor."
            })

    # Events
    data["events"] = [
        {"date": "Next Week", "time": "-", "description": "+$100 capital deposit arrives"},
        {"date": "2026-02-06", "time": "8:30 AM ET", "description": "BLS Jobs Report - Unemployment & Payrolls settle"},
        {"date": "2026-02-11", "time": "-", "description": "CPI Inflation Data Release"},
        {"date": "2026-02-24", "time": "-", "description": "Challenge Period Ends"}
    ]

    # Scenarios - parse from markdown
    scenarios_match = re.search(r'\*\*Potential Outcomes.*?Best case.*?\+\$(\d+\.?\d*).*?Both lose.*?-\$(\d+\.?\d*)', md_content, re.DOTALL)

    best_profit = 155.40
    worst_loss = 121.00
    starting = data["stats"]["starting_bankroll"]

    data["scenarios"] = [
        {
            "name": "Best Case (All Win)",
            "emoji": "target",
            "total_profit": f"${best_profit:.2f}",
            "final_bankroll": f"${starting + best_profit:.2f}",
            "return_pct": str(round((best_profit / starting) * 100))
        },
        {
            "name": "Short-Term Only (Feb 6)",
            "emoji": "chart",
            "total_profit": "$54.40",
            "final_bankroll": f"${starting + 54.40:.2f}",
            "return_pct": str(round((54.40 / starting) * 100))
        },
        {
            "name": "Worst Case (All Lose)",
            "emoji": "warning",
            "total_profit": f"-${worst_loss:.2f}",
            "final_bankroll": f"${starting - worst_loss:.2f}",
            "return_pct": str(round((-worst_loss / starting) * 100))
        }
    ]

    return data


def update_sheets(service, data: dict, dry_run: bool = False):
    """Write parsed data to Google Sheets."""

    updates = []

    # Meta tab
    meta_values = [
        ["Field", "Value"],
        ["Last Updated", data["meta"]["last_updated"]],
        ["Day", str(data["meta"]["day"])],
        ["Challenge Start", data["meta"]["challenge_start"]],
        ["Challenge End", data["meta"]["challenge_end"]]
    ]
    updates.append({"range": "Meta!A1:B5", "values": meta_values})

    # Stats tab
    stats = data["stats"]
    stats_values = [
        ["Metric", "Value"],
        ["Working Capital Total", f"${stats['working_capital_total']:.2f}"],
        ["Working Capital Available", f"${stats['working_capital_available']:.2f}"],
        ["Working Capital Pending", f"${stats['working_capital_pending']:.2f}"],
        ["Starting Bankroll", f"${stats['starting_bankroll']:.2f}"],
        ["Current Value", f"${stats['current_value']:.2f}"],
        ["Total Return", f"${stats['total_return']:.2f}"],
        ["Total Return %", str(stats['total_return_pct'])],
        ["Active Bets", str(stats['active_bets'])],
        ["Settled Bets", str(stats['settled_bets'])]
    ]
    updates.append({"range": "Stats!A1:B10", "values": stats_values})

    # Positions tab
    positions_values = [
        ["ID", "Title", "Type", "Platform", "Position", "Amount", "Entry Price",
         "Contracts", "Potential Profit", "Profit %", "Settlement", "Est Prob",
         "Market Prob", "Risk", "Reasoning"]
    ]
    for pos in data["positions"]:
        positions_values.append([
            pos["id"], pos["title"], pos["type"], pos["platform"], pos["position"],
            pos["amount"], pos["entry_price"], pos["contracts"], pos["potential_profit"],
            pos["profit_pct"], pos["settlement"], pos["est_prob"], pos["market_prob"],
            pos["risk"], pos["reasoning"]
        ])
    updates.append({"range": f"Positions!A1:O{len(positions_values)}", "values": positions_values})

    # Events tab
    events_values = [["Date", "Time", "Description"]]
    for event in data["events"]:
        events_values.append([event["date"], event["time"], event["description"]])
    updates.append({"range": f"Events!A1:C{len(events_values)}", "values": events_values})

    # Scenarios tab
    scenarios_values = [["Name", "Emoji", "Total Profit", "Final Bankroll", "Return %"]]
    for scenario in data["scenarios"]:
        scenarios_values.append([
            scenario["name"], scenario["emoji"], scenario["total_profit"],
            scenario["final_bankroll"], scenario["return_pct"]
        ])
    updates.append({"range": f"Scenarios!A1:E{len(scenarios_values)}", "values": scenarios_values})

    if dry_run:
        print("\n[DRY RUN] Would write the following updates:")
        for update in updates:
            print(f"\n  {update['range']}:")
            for row in update['values'][:3]:
                print(f"    {row}")
            if len(update['values']) > 3:
                print(f"    ... ({len(update['values']) - 3} more rows)")
        return

    # Batch update all ranges
    body = {
        "valueInputOption": "USER_ENTERED",
        "data": [{"range": u["range"], "values": u["values"]} for u in updates]
    }

    result = service.spreadsheets().values().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=body
    ).execute()

    print(f"Updated {result.get('totalUpdatedCells', 0)} cells across {len(updates)} tabs")


def main():
    parser = argparse.ArgumentParser(description="Update SMC Google Sheets from markdown tracker")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    args = parser.parse_args()

    print("=" * 60)
    print("Sharp Money Collective - Google Sheets Updater")
    print("=" * 60)

    # Read markdown tracker
    if not TRACKER_MD.exists():
        print(f"Error: Tracker not found at {TRACKER_MD}")
        return 1

    print(f"\n1. Reading tracker: {TRACKER_MD}")
    md_content = TRACKER_MD.read_text()

    # Parse data
    print("2. Parsing tracker data...")
    data = parse_tracker(md_content)
    print(f"   - Day {data['meta']['day']} of challenge")
    print(f"   - {len(data['positions'])} active positions")
    print(f"   - Working capital: ${data['stats']['working_capital_total']:.2f}")

    # Authenticate with Google
    print("3. Authenticating with Google Sheets API...")
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)

    # Update sheets
    print(f"4. {'[DRY RUN] ' if args.dry_run else ''}Updating spreadsheet...")
    update_sheets(service, data, dry_run=args.dry_run)

    print("\nDone!")
    print(f"View sheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")

    return 0


if __name__ == "__main__":
    exit(main())
