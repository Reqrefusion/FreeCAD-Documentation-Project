# FreeCAD Documentation Maintenance Tool

This script scans a directory of FreeCAD macro files and generates a markdown documentation table.

## Usage

```bash
python update_macros_doc.py /path/to/macros -o macros_list.md
```

## Requirements

- Python 3.x
- No external dependencies

## Notes

The script extracts metadata from the standard FreeCAD macro header (comments at the top of the file).
If macros lack proper headers, the table will have empty fields.
