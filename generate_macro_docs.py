#!/usr/bin/env python3
"""
Script to generate macro documentation from .FCMacro files.
Scans a directory for FreeCAD macro files and extracts metadata from their header comments.
Outputs a Markdown document with a table of macros.
"""

import os
import sys
import re
import argparse
from pathlib import Path

def parse_macro_header(macro_path):
    """
    Parse the header comments of a FreeCAD macro file.
    Returns a dictionary of extracted metadata.
    """
    metadata = {
        'filename': Path(macro_path).name,
        'title': '',
        'description': '',
        'author': '',
        'version': '',
        'license': '',
        'date': ''
    }
    try:
        with open(macro_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line.startswith('#'):
                    continue
                content = line.lstrip('#').strip()
                match = re.match(r'^(\w+)\s*:\s*(.*)', content, re.IGNORECASE)
                if match:
                    key = match.group(1).lower()
                    value = match.group(2).strip()
                    if key in metadata:
                        if metadata[key] == '':
                            metadata[key] = value
    except Exception as e:
        print(f"Error reading {macro_path}: {e}", file=sys.stderr)
    return metadata

def generate_documentation(macros_dir, output_file):
    """
    Scan macros_dir for .FCMacro files, parse headers, and write Markdown documentation.
    """
    macros_dir = Path(macros_dir)
    if not macros_dir.is_dir():
        print(f"Error: {macros_dir} is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    macro_files = list(macros_dir.glob('*.FCMacro')) + list(macros_dir.glob('*.py'))
    if not macro_files:
        print(f"No macro files found in {macros_dir}.", file=sys.stderr)
        macro_data = []
    else:
        macro_data = [parse_macro_header(mf) for mf in macro_files]

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write("# FreeCAD Macros Documentation\n\n")
        out.write("Automatically generated from macro files.\n\n")
        out.write("| Filename | Title | Description | Author | Version |\n")
        out.write("|----------|-------|-------------|--------|---------|\n")
        for m in macro_data:
            def esc(txt): return txt.replace('|', '\\|')
            out.write(f"| {esc(m['filename'])} | {esc(m['title'])} | {esc(m['description'])} | {esc(m['author'])} | {esc(m['version'])} |\n")
        out.write("\n## Detailed Info\n\n")
        for m in macro_data:
            out.write(f"### {m['title'] or m['filename']}\n\n")
            out.write(f"- **Filename**: `{m['filename']}`\n")
            out.write(f"- **Author**: {m['author'] or 'Unknown'}\n")
            out.write(f"- **Version**: {m['version'] or 'N/A'}\n")
            out.write(f"- **License**: {m['license'] or 'N/A'}\n")
            out.write(f"- **Date**: {m['date'] or 'N/A'}\n")
            out.write(f"- **Description**: {m['description'] or 'No description provided.'}\n\n")

    print(f"Documentation generated: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Generate macro documentation from FreeCAD macros.')
    parser.add_argument('macros_dir', nargs='?', default='macros', help='Directory containing macro files (default: macros)')
    parser.add_argument('-o', '--output', default='Macros_documentation.md', help='Output Markdown file (default: Macros_documentation.md)')
    args = parser.parse_args()
    generate_documentation(args.macros_dir, args.output)

if __name__ == '__main__':
    main()
