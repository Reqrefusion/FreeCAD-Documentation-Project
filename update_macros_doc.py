#!/usr/bin/env python3

"""
Script to update FreeCAD macros documentation.
Scans a directory for macro files, extracts metadata,
and generates a markdown documentation file.
"""

import os
import re
import argparse
from datetime import datetime

def extract_metadata(filepath):
    """Extract metadata from a FreeCAD macro file."""
    metadata = {
        'name': os.path.splitext(os.path.basename(filepath))[0],
        'description': '',
        'author': '',
        'version': '',
        'date': '',
        'filename': os.path.basename(filepath)
    }
    
    # Patterns for standard macro header
    patterns = {
        'description': re.compile(r'^#\s*(?:Description|Short description)\s*:\s*(.+)$', re.IGNORECASE),
        'author': re.compile(r'^#\s*Author\s*:\s*(.+)$', re.IGNORECASE),
        'version': re.compile(r'^#\s*Version\s*:\s*(.+)$', re.IGNORECASE),
        'date': re.compile(r'^#\s*Date\s*:\s*(.+)$', re.IGNORECASE),
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                for key, pattern in patterns.items():
                    match = pattern.match(line)
                    if match:
                        metadata[key] = match.group(1).strip()
                        break
                # Stop after first empty line (end of header)
                if line == '':
                    break
    except Exception as e:
        print(f'Error reading {filepath}: {e}')
    
    return metadata

def scan_macros(directory):
    """Scan directory for macro files."""
    macros = []
    if not os.path.isdir(directory):
        print(f'Directory not found: {directory}')
        return macros
    
    for filename in os.listdir(directory):
        if filename.endswith(('.FCMacro', '.py')):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                metadata = extract_metadata(filepath)
                macros.append(metadata)
    
    return macros

def generate_markdown(macros, output_file):
    """Generate markdown documentation from macros list."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# FreeCAD Macros Documentation\n\n')
        f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('| Name | Description | Author | Version | Date | File |\n')
        f.write('|------|-------------|--------|---------|------|------|\n')
        
        for macro in macros:
            name = macro['name']
            desc = macro['description'].replace('|', '\\|')
            author = macro['author'].replace('|', '\\|')
            version = macro['version']
            date = macro['date']
            filename = macro['filename']
            f.write(f'| {name} | {desc} | {author} | {version} | {date} | {filename} |\n')
        
        f.write('\n---\n\n*This documentation was automatically generated.*\n')

def main():
    parser = argparse.ArgumentParser(description='Update FreeCAD macros documentation.')
    parser.add_argument('directory', help='Directory containing macro files')
    parser.add_argument('-o', '--output', default='macros_doc.md', help='Output markdown file')
    args = parser.parse_args()
    
    macros = scan_macros(args.directory)
    if not macros:
        print('No macros found.')
        return
    
    generate_markdown(macros, args.output)
    print(f'Documentation generated: {args.output}')

if __name__ == '__main__':
    main()
