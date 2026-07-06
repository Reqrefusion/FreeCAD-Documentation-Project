#!/usr/bin/env python3
"""
Script to find recent PRs merged into the FreeCAD Draft Workbench
and generate a markdown summary of missing documentation features.
"""
import os
import sys
import json
import requests
from datetime import datetime, timedelta

def get_github_token():
    """Get GitHub token from environment variable."""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Warning: GITHUB_TOKEN not set. API rate limits may apply.", file=sys.stderr)
    return token

def fetch_merged_prs(repo, label, since_days=30):
    """Fetch merged PRs with a specific label from the last N days."""
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {"Accept": "application/vnd.github.v3+json"}
    token = get_github_token()
    if token:
        headers["Authorization"] = f"token {token}"
    since_date = (datetime.utcnow() - timedelta(days=since_days)).isoformat() + "Z"
    params = {
        "state": "closed",
        "sort": "updated",
        "direction": "desc",
        "per_page": 100,
        "since": since_date
    }
    prs = []
    page = 1
    while True:
        params["page"] = page
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching page {page}: {e}", file=sys.stderr)
            break
        data = response.json()
        if not data:
            break
        # Filter for merged PRs that are labeled
        for pr in data:
            if pr.get("merged_at"):
                # Check labels
                labels = [l["name"].lower() for l in pr.get("labels", [])]
                if label.lower() in labels:
                    prs.append({
                        "number": pr["number"],
                        "title": pr["title"],
                        "html_url": pr["html_url"],
                        "merged_at": pr["merged_at"],
                        "body": pr.get("body", "")[:500]  # Truncate
                    })
        page += 1
        if len(data) < 100:
            break
    return prs

def generate_markdown_report(prs, label):
    """Generate a markdown report of the PRs."""
    report = f"# Missing Documentation: Draft Workbench PRs with label '{label}'\n\n"
    report += f"Generated on {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n\n"
    if not prs:
        report += "No PRs found in the specified period."
        return report
    report += f"Found {len(prs)} merged PR(s):\n\n"
    for pr in prs:
        report += f"## PR #{pr['number']}: {pr['title']}\n"
        report += f"- **Merged:** {pr['merged_at']}\n"
        report += f"- **URL:** {pr['html_url']}\n"
        report += f"- **Description:** {pr['body'][:200]}...\n\n"
    report += "---\n"
    report += "**Action:** Update the Draft Workbench documentation to reflect these changes."
    return report

if __name__ == "__main__":
    REPO = "FreeCAD/FreeCAD"
    LABEL = "Draft"  # Adjust as needed
    DAYS_BACK = 60
    print(f"Searching for merged PRs with label '{LABEL}' in {REPO} from last {DAYS_BACK} days...", file=sys.stderr)
    prs = fetch_merged_prs(REPO, LABEL, since_days=DAYS_BACK)
    report = generate_markdown_report(prs, LABEL)
    output_file = "draft_doc_update_report.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Report saved to {output_file}")
