#!/usr/bin/env python3
"""
Script to scan FreeCAD macro files and generate wiki documentation.
Usage: python maintain_macros.py --input_dir /path/to/macros --output_file macros_wiki.txt
"""

import os
import re
import argparse


def parse_macro_header(filepath):
    """Extract metadata from a FreeCAD macro file."""
    fields = {
        'name': '',
        'description': '',
        'author': '',
        'version': '',
        'date': '',
        'fc_version': '',
        'license': '',
        'usage': '',
        'category': '',
        'wiki': ''
    }
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return fields

    # Look for comments starting with # or ;; (common in FreeCAD macros)
    lines = content.splitlines()
    header_lines = []
    in_header = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') or stripped.startswith(';;'):
            if stripped.startswith(';;'):
                stripped = stripped[2:].strip()
            else:
                stripped = stripped[1:].strip()
            if stripped.lower().startswith('name'):
                in_header = True
            if in_header:
                header_lines.append(stripped)
        else:
            if in_header:
                # End of header (first non-comment line)
                break

    # Parse key: value pairs
    for line in header_lines:
        match = re.match(r'^([a-zA-Z_]+)\s*[:]\s*(.+)$', line)
        if match:
            key = match.group(1).strip().lower()
            value = match.group(2).strip()
            if key in fields:
                # Handle multiline? For simplicity, just first line
                if fields[key]:
                    fields[key] += ' ' + value
                else:
                    fields[key] = value

    # If no header found, use filename as name
    if not fields['name']:
        fields['name'] = os.path.splitext(os.path.basename(filepath))[0]
    return fields


def generate_wiki_entry(macro):
    """Create a MediaWiki formatted entry for the macro."""
    entry = f"== {macro['name']} ==\n"
    entry += f"|{{| class=\"wikitable\"\n"
    entry += f"! Description\n| {macro['description'] or 'No description'}\n"
    entry += f"|! Author\n| {macro['author'] or 'Unknown'}\n"
    entry += f"|! Version\n| {macro['version'] or '0.0'}\n"
    entry += f"|! Date\n| {macro['date'] or 'Unknown'}\n"
    entry += f"|! FreeCAD version\n| {macro['fc_version'] or 'All'}\n"
    entry += f"|! License\n| {macro['license'] or 'Unknown'}\n"
    entry += f"|! Category\n| {macro['category'] or 'Uncategorized'}\n"
    entry += f"|! [[Macros recipes|Usage]]\n| {macro['usage'] or 'See macro file'}\n"
    entry += f"|! Wiki page\n| {macro['wiki'] or f'[[Macro_{macro["name"]}]]'}\n"
    entry += "|}\n\n"
    return entry


def main():
    parser = argparse.ArgumentParser(description='Generate wiki documentation for FreeCAD macros.')
    parser.add_argument('--input_dir', required=True, help='Directory containing .FCMacro files')
    parser.add_argument('--output_file', required=True, help='Output wiki text file')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_file = args.output_file

    if not os.path.isdir(input_dir):
        print(f"Error: {input_dir} is not a valid directory")
        return

    macros = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.fcmacro') or filename.lower().endswith('.py'):
            filepath = os.path.join(input_dir, filename)
            if os.path.isfile(filepath):
                macro = parse_macro_header(filepath)
                macros.append(macro)

    # Generate wiki content
    wiki_content = "= Macro listings =\n\n"
    wiki_content += "This page lists all macros in the repository.\n\n"
    for macro in sorted(macros, key=lambda x: x['name']):
        wiki_content += generate_wiki_entry(macro)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(wiki_content)

    print(f"Generated wiki documentation for {len(macros)} macros in {output_file}")


if __name__ == '__main__':
    main()
