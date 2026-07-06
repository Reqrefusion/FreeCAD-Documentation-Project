# Macro Documentation Maintenance

This directory contains a script (`update_macros.py`) that automatically fetches the latest FreeCAD macros from the official repository and generates a markdown listing (`macros_list.md`).

## Usage

1. Ensure Python 3 and `requests` library are installed: `pip install requests`
2. Run the script: `python update_macros.py`
3. The file `macros_list.md` will be created/updated.

## Integration

This script can be scheduled as a cron job or GitHub Actions workflow to keep the macros documentation up-to-date.

## Note

The script expects the JSON data from the macro repository to be a list of macro objects or a dict with a "macros" key. Adjust the parsing if the source format changes.
