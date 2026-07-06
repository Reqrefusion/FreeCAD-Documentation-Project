#!/usr/bin/env python3
"""
FreeCAD Macros Documentation Updater

This script fetches the list of macros from the FreeCAD-macros GitHub repository
and generates/updates a JSON index file with metadata (name, description, author, link).
It can be run periodically to maintain the macro documentation.
"""

import json
import os
import requests
from datetime import datetime

# Configuration
GITHUB_API_URL = "https://api.github.com/repos/FreeCAD/FreeCAD-macros/contents/macros"
OUTPUT_FILE = "macros_index.json"


def fetch_macros():
    """Fetch list of macro files from GitHub repository."""
    response = requests.get(GITHUB_API_URL)
    if response.status_code != 200:
        print(f"Error fetching macros: {response.status_code}")
        return []
    
    items = response.json()
    macros = []
    for item in items:
        if item['type'] == 'file' and item['name'].endswith('.FCMacro'):
            # Extract name without extension
            name = item['name'][:-7]
            # Get raw content for description (first line after comments?)
            raw_url = item['download_url']
            try:
                content_response = requests.get(raw_url)
                if content_response.status_code == 200:
                    content = content_response.text
                    # Simple heuristic: first non-comment line as description
                    description = ""
                    for line in content.split('\n'):
                        stripped = line.strip()
                        if stripped and not stripped.startswith('#'):
                            description = stripped[:200]  # limit length
                            break
                else:
                    description = ""
            except Exception as e:
                print(f"Error reading {item['name']}: {e}")
                description = ""
            
            macros.append({
                "name": name,
                "filename": item['name'],
                "path": item['path'],
                "description": description,
                "github_url": item['html_url'],
                "download_url": raw_url,
                "size": item['size'],
                "updated_at": datetime.now().isoformat()
            })
    return macros


def load_existing_index():
    """Load existing index file if it exists."""
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, 'r') as f:
            return json.load(f)
    return []


def merge_macros(new_macros, existing_macros):
    """Merge new macros with existing, preserving extra fields not coming from API."""
    existing_dict = {m['filename']: m for m in existing_macros if 'filename' in m}
    for macro in new_macros:
        fname = macro['filename']
        if fname in existing_dict:
            # Update fields from API
            existing_dict[fname].update(macro)
        else:
            existing_dict[fname] = macro
    return list(existing_dict.values())


def save_index(macros):
    """Save macros list to JSON file."""
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(macros, f, indent=2)
    print(f"Saved {len(macros)} macros to {OUTPUT_FILE}")


def generate_markdown(macros):
    """Generate a simple Markdown documentation from the index."""
    lines = ["# FreeCAD Macros Index\n", f"_Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n", ""]
    lines.append("| Name | Description | Link |")
    lines.append("|------|-------------|------|")
    for macro in sorted(macros, key=lambda x: x['name']):
        name = macro['name']
        desc = macro.get('description', '')[:100].replace('|', '\\|')
        github_url = macro.get('github_url', '#')
        lines.append(f"| {name} | {desc} | [View]({github_url}) |")
    return '\n'.join(lines)


def main():
    print("Fetching macros from GitHub...")
    new_macros = fetch_macros()
    if not new_macros:
        print("No macros fetched, exiting.")
        return
    
    existing_macros = load_existing_index()
    merged = merge_macros(new_macros, existing_macros)
    save_index(merged)
    
    # Optionally update README.md
    readme_content = generate_markdown(merged)
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("README.md updated.")


if __name__ == "__main__":
    main()
