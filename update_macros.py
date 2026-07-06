#!/usr/bin/env python3
"""
Script to maintain FreeCAD macros documentation.
This script scans the FreeCAD Addons Manager's macro repository or a local cache
and generates a markdown file listing all available macros with their details.
"""

import json
import os
import requests
from datetime import datetime

# Configuration
MACRO_SOURCE_URL = "https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/macros.json"
OUTPUT_FILE = "macros_list.md"

def fetch_macro_data(url):
    """Fetch macro metadata from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching macro data: {e}")
        return None

def generate_markdown(macros):
    """Generate markdown content from macro list."""
    lines = [
        "# FreeCAD Macros List",
        f"""
This list is auto-generated from the FreeCAD macros repository.
Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}
""",
        "| Macro Name | Description | Author | Version |",
        "|---|---|---|---|"
    ]
    
    for macro in macros:
        name = macro.get("name", "Unknown")
        desc = macro.get("description", "")
        author = macro.get("author", "Unknown")
        version = macro.get("version", "")
        # Escape pipe characters in description
        desc = desc.replace("|", "\\|")
        lines.append(f"| {name} | {desc} | {author} | {version} |")
    
    return "\n".join(lines)

def write_output(content, filepath):
    """Write content to file."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Documentation written to {filepath}")

def main():
    print("Fetching macro data...")
    macro_data = fetch_macro_data(MACRO_SOURCE_URL)
    if macro_data is None:
        print("Could not fetch macro data. Exiting.")
        return
    
    # The structure of macros.json is expected to be a list of macro objects
    # If it's a dict with a key 'macros', adjust accordingly
    if isinstance(macro_data, dict):
        macros = macro_data.get("macros", [])
    else:
        macros = macro_data
    
    print(f"Found {len(macros)} macros.")
    markdown_content = generate_markdown(macros)
    write_output(markdown_content, OUTPUT_FILE)

if __name__ == "__main__":
    main()
