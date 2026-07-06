#!/usr/bin/env python3
"""
Script to generate macro documentation from FreeCAD macro files.
Usage: python generate_macro_docs.py [macros_directory] [output_file]
"""

import os
import sys
import re
import argparse
from datetime import datetime

def parse_macro_file(filepath):
    """Extract metadata from a FreeCAD macro file."""
    metadata = {
        'filename': os.path.basename(filepath),
        'name': 'Unknown',
        'description': '',
        'author': 'Unknown',
        'version': 'Unknown',
        'date': '',
    }
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if not line.startswith('#'):
                    continue
                line = line.lstrip('#').strip()
                if not line:
                    continue
                match = re.match(r'(Name|Description|Author|Version|Date)\s*:\s*(.*)', line, re.IGNORECASE)
                if match:
                    key = match.group(1).lower()
                    value = match.group(2).strip()
                    if key in metadata:
                        metadata[key] = value
                elif 'Description' not in [k for k in metadata if metadata[k]]:
                    if not metadata['description']:
                        metadata['description'] = line
                    else:
                        metadata['description'] += ' ' + line
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
    return metadata

def generate_markdown(macros, output_path):
    """Generate markdown index from list of macro metadata."""
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write("# FreeCAD Macros Index\n\n")
        out.write("Generated on {}\n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        out.write("| Macro | Description | Author | Version |\n")
        out.write("|-------|-------------|--------|---------|\n")
        for macro in sorted(macros, key=lambda m: m['name'].lower()):
            name = macro['name']
            desc = macro['description'].replace('|', '\\|') if macro['description'] else ''
            author = macro['author'].replace('|', '\\|')
            version = macro['version']
            out.write(f"| {name} | {desc} | {author} | {version} |\n")

def main():
    parser = argparse.ArgumentParser(description='Generate macro documentation from FreeCAD macro files.')
    parser.add_argument('macros_dir', nargs='?', default='.', help='Directory containing macro files (default: current directory)')
    parser.add_argument('-o', '--output', default='macros_index.md', help='Output markdown file (default: macros_index.md)')
    args = parser.parse_args()

    macros_dir = args.macros_dir
    if not os.path.isdir(macros_dir):
        print(f"Error: {macros_dir} is not a directory.", file=sys.stderr)
        sys.exit(1)

    macros = []
    for root, dirs, files in os.walk(macros_dir):
        for file in files:
            if file.lower().endswith('.fcmacro'):
                filepath = os.path.join(root, file)
                meta = parse_macro_file(filepath)
                macros.append(meta)

    if not macros:
        print("No macro files found.", file=sys.stderr)
        sys.exit(1)

    generate_markdown(macros, args.output)
    print(f"Generated {args.output} with {len(macros)} macros.")

if __name__ == '__main__':
    main()
