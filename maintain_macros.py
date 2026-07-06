#!/usr/bin/env python3
"""
Script to update the FreeCAD Macros documentation page.
This script reads a list of macros (from a JSON file or directly scraped)
and generates a markdown file with the current set of macros.
"""

import json
import os
import urllib.request
import urllib.error
from datetime import datetime

# Configuration
MACROS_JSON_URL = "https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/macros.json"  # Example URL
OUTPUT_MD = "Macros_list.md"


def fetch_macros_json(url):
    """Fetch the macros list from a remote JSON source."""
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except urllib.error.URLError as e:
        print(f"Error fetching macros JSON: {e}")
        return None


def generate_markdown(macros):
    """Generate a markdown string with the macros table."""
    lines = [
        "# FreeCAD Macros List",
        "",
        f"*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*",
        "",
        "| Macro Name | Description | Author | Version |",
        "|---|---|---|---|",
    ]
    for macro in macros:
        name = macro.get("name", "Unknown")
        desc = macro.get("description", "No description")
        author = macro.get("author", "Unknown")
        version = macro.get("version", "N/A")
        lines.append(f"| {name} | {desc} | {author} | {version} |")
    return "\n".join(lines)


def main():
    print("Fetching macros list...")
    macros = fetch_macros_json(MACROS_JSON_URL)
    if macros is None:
        # Fallback: use a placeholder list (for development)
        print("Using placeholder macros (remote fetch failed).")
        macros = [
            {"name": "Macro_Example", "description": "An example macro", "author": "User1", "version": "1.0"},
            {"name": "Macro_PartDesignHelper", "description": "Helps with Part Design", "author": "User2", "version": "2.1"},
        ]
    print("Generating markdown...")
    md_content = generate_markdown(macros)
    with open(OUTPUT_MD, "w") as f:
        f.write(md_content)
    print(f"Macros list written to {OUTPUT_MD}")


if __name__ == "__main__":
    main()
