#!/usr/bin/env python3
"""
Script to maintain the FreeCAD Macros documentation.
Fetches macro list from the FreeCAD GitHub repository and updates MACROS.md.
"""

import json
import requests
import os
from datetime import datetime

# Configuration
MACROS_API_URL = "https://api.github.com/repos/FreeCAD/FreeCAD-macros/contents/Macros"
MACROS_DOC_FILE = "MACROS.md"


def fetch_macros_list():
    """Fetch list of macro files from GitHub API."""
    response = requests.get(MACROS_API_URL)
    response.raise_for_status()
    items = response.json()
    # Filter only directories (macros are often in folders) or .FCMacro files
    macros = []
    for item in items:
        if item['type'] == 'file' and item['name'].endswith('.FCMacro'):
            macros.append(item)
        elif item['type'] == 'dir':
            # Could recurse but for simplicity assume macros are files
            pass
    return macros


def get_macro_metadata(macro_name, repo_path="FreeCAD/FreeCAD-macros"):
    """Fetch metadata for a specific macro file from GitHub."""
    # Try to get the raw file content and parse header comments
    raw_url = f"https://raw.githubusercontent.com/{repo_path}/master/Macros/{macro_name}"
    response = requests.get(raw_url)
    if response.status_code != 200:
        return {}
    content = response.text
    # Simple parsing for name, description, author, version from header comments
    metadata = {
        'name': macro_name,
        'description': '',
        'author': '',
        'version': ''
    }
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# Name:'):
            metadata['name'] = line.split(':', 1)[1].strip()
        elif line.startswith('# Description:'):
            metadata['description'] = line.split(':', 1)[1].strip()
        elif line.startswith('# Author:'):
            metadata['author'] = line.split(':', 1)[1].strip()
        elif line.startswith('# Version:'):
            metadata['version'] = line.split(':', 1)[1].strip()
    return metadata


def generate_markdown(macros_metadata):
    """Generate Markdown table from list of metadata."""
    header = "# FreeCAD Macros Documentation\n\n"
    header += f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
    header += "| Macro | Description | Author | Version |\n"
    header += "|-------|-------------|--------|---------|\n"
    rows = []
    for meta in macros_metadata:
        row = f"| {meta['name']} | {meta['description']} | {meta['author']} | {meta['version']} |"
        rows.append(row)
    return header + '\n'.join(rows)


def update_documentation():
    """Main function to update the macros documentation."""
    print("Fetching macro list...")
    try:
        macros = fetch_macros_list()
    except Exception as e:
        print(f"Error fetching macro list: {e}")
        return

    print(f"Found {len(macros)} macro files.")
    metadata_list = []
    for macro in macros:
        print(f"Fetching metadata for {macro['name']}...")
        meta = get_macro_metadata(macro['name'])
        metadata_list.append(meta)

    print("Generating Markdown...")
    markdown_content = generate_markdown(metadata_list)

    with open(MACROS_DOC_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Documentation updated: {MACROS_DOC_FILE}")


if __name__ == "__main__":
    update_documentation()
