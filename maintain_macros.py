#!/usr/bin/env python3
"""
Script to scan FreeCAD official macro repository and extract metadata for documentation.
This script fetches the list of macro files from the FreeCAD-macros GitHub repo,
parses their headers to get name, description, author, version, and outputs the
information as JSON for further processing (e.g., updating wiki or markdown docs).
"""

import requests
import json
import re
import sys

GITHUB_API = "https://api.github.com"
REPO_OWNER = "FreeCAD"
REPO_NAME = "FreeCAD-macros"
BRANCH = "master"
MACROS_PATH = "Macros"

def get_macro_files():
    """Retrieve list of macro files from the repository's Macros directory."""
    url = f"{GITHUB_API}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{MACROS_PATH}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        items = resp.json()
        # Filter only .FCMacro files (also could include directories for further recursion)
        macro_files = [item for item in items if item['type'] == 'file' and item['name'].endswith('.FCMacro')]
        return macro_files
    except requests.exceptions.RequestException as e:
        print(f"Error fetching macro list: {e}", file=sys.stderr)
        return []

def fetch_metadata(download_url):
    """Download macro file and parse metadata from header comments.
    Expected format: lines starting with '#' containing 'Key: Value'."""
    try:
        resp = requests.get(download_url, timeout=30)
        resp.raise_for_status()
        content = resp.text
        metadata = {}
        pattern = r'^#\s*(\w+)\s*:\s*(.+)$'
        for line in content.splitlines():
            match = re.match(pattern, line)
            if match:
                key = match.group(1).lower()
                value = match.group(2).strip()
                metadata[key] = value
        return metadata
    except Exception as e:
        print(f"Error downloading/parsing {download_url}: {e}", file=sys.stderr)
        return {}

def main():
    macro_files = get_macro_files()
    if not macro_files:
        print(json.dumps({"error": "No macro files found or error fetching"}))
        sys.exit(1)

    macros = []
    for mfile in macro_files:
        metadata = fetch_metadata(mfile['download_url'])
        if 'name' in metadata and 'description' in metadata:
            macros.append({
                'name': metadata['name'],
                'description': metadata['description'],
                'author': metadata.get('author', 'unknown'),
                'version': metadata.get('version', 'unknown'),
                'url': mfile['html_url'],
                'updated': mfile.get('updated_at', None)
            })
        else:
            # Optionally report files without proper header
            print(f"Warning: {mfile['name']} missing name or description in header", file=sys.stderr)

    output = {
        "scanned_at": None,  # could add timestamp
        "total": len(macros),
        "macros": macros
    }
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
