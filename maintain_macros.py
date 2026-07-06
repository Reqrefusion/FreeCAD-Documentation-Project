#!/usr/bin/env python3
"""
Script to maintain FreeCAD macros documentation.
Fetches the list of macros from the FreeCAD wiki,
compares with a local cache, and generates updated documentation.
"""

import json
import os
import re
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# Constants
WIKI_URL = "https://wiki.freecad.org/Macros"
LOCAL_CACHE_FILE = "macros_cache.json"
OUTPUT_FILE = "macros_documentation.md"


def fetch_macros_from_wiki():
    """Scrape the FreeCAD wiki Macros page and return a list of macro dicts."""
    try:
        response = requests.get(WIKI_URL, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wiki page: {e}", file=sys.stderr)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable")
    if not table:
        print("Could not find macros table on wiki page.", file=sys.stderr)
        return []

    macros = []
    rows = table.find_all("tr")
    # Skip header row
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        # Extract macro name from first cell (link)
        name_link = cells[0].find("a")
        name = name_link.get_text(strip=True) if name_link else ""
        # Extract description from second cell
        description = cells[1].get_text(strip=True) if len(cells) > 1 else ""
        # Extract author from third cell (if present)
        author = cells[2].get_text(strip=True) if len(cells) > 2 else ""
        if name:
            macros.append({
                "name": name,
                "description": description,
                "author": author,
                "url": f"https://wiki.freecad.org/{name.replace(' ', '_')}" if name else ""
            })
    return macros


def load_local_cache():
    """Load local cache of known macros from JSON file."""
    if os.path.exists(LOCAL_CACHE_FILE):
        try:
            with open(LOCAL_CACHE_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading cache: {e}", file=sys.stderr)
    return []


def save_local_cache(macros):
    """Save macros list to local cache JSON file."""
    try:
        with open(LOCAL_CACHE_FILE, "w") as f:
            json.dump(macros, f, indent=2)
    except IOError as e:
        print(f"Error writing cache: {e}", file=sys.stderr)


def compare_and_find_new(wiki_macros, cached_macros):
    """Return list of macros present in wiki_macros but not in cached_macros."""
    cached_names = {m["name"] for m in cached_macros}
    return [m for m in wiki_macros if m["name"] not in cached_names]


def generate_documentation(macros, new_macros=None):
    """Generate Markdown documentation for macros."""
    lines = []
    lines.append("# FreeCAD Macros Documentation\n")
    lines.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")

    if new_macros:
        lines.append("## New Macros\n")
        lines.append("The following macros were newly added:\n")
        for m in new_macros:
            lines.append(f"- **{m['name']}**: {m['description']} (by {m['author']})")
        lines.append("")

    lines.append("## All Macros\n")
    lines.append("| Name | Description | Author |")
    lines.append("|------|-------------|--------|")
    for m in macros:
        lines.append(f"| [{m['name']}]({m['url']}) | {m['description']} | {m['author']} |")
    lines.append("")
    lines.append("---\n")
    lines.append(
        "*This documentation is automatically maintained. "
        "To update, run `python maintain_macros.py`.*"
    )
    return "\n".join(lines)


def main():
    print("Fetching macros from FreeCAD wiki...")
    wiki_macros = fetch_macros_from_wiki()
    if not wiki_macros:
        print("Failed to fetch macros. Exiting.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(wiki_macros)} macros on wiki.")

    cached_macros = load_local_cache()
    print(f"Loaded {len(cached_macros)} macros from local cache.")

    new_macros = compare_and_find_new(wiki_macros, cached_macros)
    if new_macros:
        print(f"Found {len(new_macros)} new macros:")
        for m in new_macros:
            print(f"  - {m['name']}")
    else:
        print("No new macros found.")

    # Update cache with current wiki list
    save_local_cache(wiki_macros)
    print("Local cache updated.")

    # Generate documentation
    doc = generate_documentation(wiki_macros, new_macros)
    with open(OUTPUT_FILE, "w") as f:
        f.write(doc)
    print(f"Documentation written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
