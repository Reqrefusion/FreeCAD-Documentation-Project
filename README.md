# FreeCAD Macros Documentation Maintenance

This script automates the process of maintaining FreeCAD macros documentation.
It fetches the latest list of macros from the FreeCAD wiki, compares with a local cache,
and generates an updated Markdown documentation file.

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the script:
   ```
   python maintain_macros.py
   ```

The script will:
- Scrape the [Macros page](https://wiki.freecad.org/Macros) on the FreeCAD wiki.
- Compare with a local cache (`macros_cache.json`).
- Print any newly discovered macros.
- Update the cache to reflect the current wiki state.
- Generate `macros_documentation.md` with a table of all macros.

## Files

- `maintain_macros.py`: The main script.
- `requirements.txt`: Python dependencies.
- `macros_cache.json`: Local cache of known macros (auto-generated).
- `macros_documentation.md`: Generated documentation file.
