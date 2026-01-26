#!/usr/bin/env python3
"""
Sharp Money Collective - Auto-Update Script
Converts betting_tracker.md to smc-data.json
Run this after updating the markdown file during daily check-ins
"""

import json
import re
from datetime import datetime
from pathlib import Path

# File paths
TRACKER_MD = Path("/Users/arunash/betting_tracker.md")
OUTPUT_JSON = Path("/Users/arunash/arunash-website/smc-data.json")

def parse_markdown_tracker(md_content):
    """Parse the markdown tracker and extract structured data"""

    data = {
        "meta": {
            "lastUpdated": datetime.now().isoformat(),
            "day": 1,  # Will be parsed from MD
            "challenge": {
                "startDate": "2026-01-25",
                "endDate": "2026-02-24"
            }
        },
        "portfolio": {
            "workingCapital": {
                "total": 119.00,
                "available": 19.00,
                "pending": 100.00
            },
            "performance": {
                "startingBankroll": 140.00,
                "currentValue": 140.00,
                "totalReturn": 0.00,
                "totalReturnPct": 0.00
            },
            "stats": {
                "activeBets": 4,
                "settledBets": 0,
                "winRate": None,
                "deploymentRate": 0.16
            }
        },
        "positions": {
            "shortTerm": [],
            "longTerm": []
        },
        "scenarios": [],
        "upcomingEvents": []
    }

    # Parse working capital
    if match := re.search(r'\*\*Available Cash\*\*: \$(\d+\.?\d*)', md_content):
        data["portfolio"]["workingCapital"]["available"] = float(match.group(1))

    if match := re.search(r'\*\*Pending Deposit.*?\*\*: \$(\d+\.?\d*)', md_content):
        data["portfolio"]["workingCapital"]["pending"] = float(match.group(1))

    if match := re.search(r'\*\*Total Working Capital\*\*: \$(\d+\.?\d*)', md_content):
        data["portfolio"]["workingCapital"]["total"] = float(match.group(1))

    # Parse stats
    if match := re.search(r'\*\*Active Short-Term Bets\*\*: (\d+)', md_content):
        short_term_count = int(match.group(1))

    if match := re.search(r'\*\*Active Bets\*\*: (\d+)', md_content):
        data["portfolio"]["stats"]["activeBets"] = int(match.group(1))

    if match := re.search(r'\*\*Settled Bets\*\*: (\d+)', md_content):
        data["portfolio"]["stats"]["settledBets"] = int(match.group(1))

    # Parse positions (simplified - you can enhance this)
    # This is a basic parser - positions would need to be extracted from the markdown

    return data

def main():
    """Main update function"""
    print("🔄 Sharp Money Collective - Auto-Update")
    print("=" * 50)

    # Check if markdown file exists
    if not TRACKER_MD.exists():
        print(f"❌ Error: {TRACKER_MD} not found")
        return

    # Read markdown
    print(f"📖 Reading {TRACKER_MD}...")
    md_content = TRACKER_MD.read_text()

    # Parse to JSON
    print("🔍 Parsing tracker data...")
    data = parse_markdown_tracker(md_content)

    # Write JSON
    print(f"💾 Writing to {OUTPUT_JSON}...")
    OUTPUT_JSON.write_text(json.dumps(data, indent=2))

    print("✅ Successfully updated smc-data.json")
    print(f"📅 Last updated: {data['meta']['lastUpdated']}")
    print(f"💰 Working Capital: ${data['portfolio']['workingCapital']['total']}")
    print(f"📊 Active Bets: {data['portfolio']['stats']['activeBets']}")

if __name__ == "__main__":
    main()
