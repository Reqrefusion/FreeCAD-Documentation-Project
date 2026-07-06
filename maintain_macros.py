#!/usr/bin/env python3
"""
Script to maintain FreeCAD macros documentation.
Scrapes the FreeCAD wiki Macros page and generates a markdown file
with an up-to-date list of macros.
"""

import requests
from bs4 import BeautifulSoup
import re
import sys

WIKI_URL = "https://wiki.freecad.org/Macros"
OUTPUT_FILE = "Macros_List.md"

def fetch_macros():
    """Fetch and parse macros from the wiki page."""
    try:
        response = requests.get(WIKI_URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wiki page: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')
    macros = []

    # The macro list is typically in a table with class "wikitable"
    tables = soup.find_all('table', class_='wikitable')
    if not tables:
        print("No wikitable found on the page.", file=sys.stderr)
        sys.exit(1)

    for table in tables:
        rows = table.find_all('tr')
        for row in rows[1:]:  # skip header
            cols = row.find_all('td')
            if len(cols) < 3:
                continue
            # First column: macro name (link text)
            name_cell = cols[0]
            name_link = name_cell.find('a')
            if name_link:
                name = name_link.get_text(strip=True)
                link = name_link.get('href', '')
                if link and not link.startswith('http'):
                    link = "https://wiki.freecad.org" + link
            else:
                name = name_cell.get_text(strip=True)
                link = ""
            # Second column: description
            desc = cols[1].get_text(strip=True) if len(cols) > 1 else ""
            # Third column: author (optional)
            author = cols[2].get_text(strip=True) if len(cols) > 2 else ""
            macros.append({
                'name': name,
                'link': link,
                'description': desc,
                'author': author
            })
    return macros

def generate_markdown(macros):
    """Generate Markdown content from macros list."""
    content = ["# FreeCAD Macros List\n",
               "Automatically generated from the [FreeCAD Wiki](https://wiki.freecad.org/Macros).\n",
               "| Macro | Description | Author | Link |",
               "|-------|-------------|--------|------|"]
    for m in macros:
        name = m['name'].replace('|', '\\|')
        desc = m['description'].replace('|', '\\|')
        author = m['author'].replace('|', '\\|')
        link = m['link']
        content.append(f"| {name} | {desc} | {author} | [Link]({link}) |")
    content.append(f"\n\n_Total macros: {len(macros)}_")
    return '\n'.join(content)

def main():
    print("Fetching macros from wiki...")
    macros = fetch_macros()
    if not macros:
        print("No macros found.", file=sys.stderr)
        sys.exit(1)
    print(f"Found {len(macros)} macros.")
    md_content = generate_markdown(macros)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Documentation written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
