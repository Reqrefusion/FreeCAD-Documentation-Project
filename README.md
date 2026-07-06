# FreeCAD Macros Documentation Maintenance

This folder contains scripts and templates to maintain the FreeCAD Macros documentation.

## Files

- `maintain_macros.py` - Python script to fetch the macros list and generate a markdown file.
- `Macros_list.md` - Output file (generated).

## Usage

Run the script:
```
python maintain_macros.py
```

The script will attempt to fetch the macros JSON from the configured URL. If that fails, it uses a placeholder list.

## Notes

Ensure you have network access to fetch the macros list. The URLs and format may need adjustment as the FreeCAD macros repository evolves.
