#!/usr/bin/env python3
"""
Script to maintain FreeCAD macros documentation.
Scans a directory for macro files, extracts metadata,
and generates a markdown index for documentation.
"""

import os
import re
import argparse
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def parse_macro_metadata(filepath: str) -> Optional[Dict[str, str]]:
    """
    Parse metadata from a macro file.
    Expected format in comments:
    # Macro Name: <name>
    # Description: <description>
    # Version: <version>
    # Author: <author>
    # License: <license>
    """
    metadata = {}
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line.startswith('#'):
                    continue
                # Remove leading # and whitespace
                content = line.lstrip('#').strip()
                match = re.match(r'^(\w+)\s*:\s*(.+)$', content, re.IGNORECASE)
                if match:
                    key = match.group(1).lower().capitalize()
                    value = match.group(2).strip()
                    # Only capture known keys
                    if key in ['Macro name', 'Description', 'Version', 'Author', 'License']:
                        metadata[key] = value
    except Exception as e:
        logger.error(f"Error reading {filepath}: {e}")
        return None
    return metadata if metadata else None

def scan_macros(directory: str) -> List[Dict[str, str]]:
    """Scan directory for macro files and extract metadata."""
    macros = []
    extensions = ('.FCMacro', '.py', '.txt')
    if not os.path.isdir(directory):
        logger.error(f"Directory {directory} does not exist.")
        return macros
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                filepath = os.path.join(root, file)
                metadata = parse_macro_metadata(filepath)
                if metadata:
                    metadata['Filename'] = file
                    metadata['Path'] = os.path.relpath(filepath, directory)
                    macros.append(metadata)
                else:
                    logger.warning(f"No metadata found in {filepath}")
    return macros

def generate_markdown(macros: List[Dict[str, str]]) -> str:
    """Generate markdown index from macro metadata."""
    lines = []
    lines.append("# FreeCAD Macros Index\n")
    lines.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
    lines.append("| Macro Name | Description | Version | Author | License | File |")
    lines.append("|------------|-------------|---------|--------|---------|------|")
    for macro in sorted(macros, key=lambda x: x.get('Macro name', '').lower()):
        name = macro.get('Macro name', 'Unknown')
        desc = macro.get('Description', 'N/A')
        ver = macro.get('Version', 'N/A')
        author = macro.get('Author', 'N/A')
        license_ = macro.get('License', 'N/A')
        file = macro.get('Filename', 'N/A')
        lines.append(f"| {name} | {desc} | {ver} | {author} | {license_} | {file} |")
    return '\n'.join(lines) + '\n'

def main():
    parser = argparse.ArgumentParser(description='Maintain FreeCAD macros documentation.')
    parser.add_argument('input_dir', help='Directory containing macro files')
    parser.add_argument('-o', '--output', default='macros_index.md',
                        help='Output markdown file (default: macros_index.md)')
    args = parser.parse_args()

    logger.info(f"Scanning {args.input_dir} for macros...")
    macros = scan_macros(args.input_dir)
    if not macros:
        logger.warning("No macros with metadata found.")
        return

    logger.info(f"Found {len(macros)} macros with metadata.")
    markdown = generate_markdown(macros)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(markdown)
    logger.info(f"Documentation written to {args.output}")

if __name__ == '__main__':
    main()
