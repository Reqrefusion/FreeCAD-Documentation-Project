# Draft Heal

## Description

The **Draft Heal** command attempts to repair broken Draft objects, such as wires, arcs, or circles that have become invalid due to topological errors. This is useful when importing or copying geometry that may contain defects.

## Usage

1. Select one or more broken Draft objects.
2. Press the **Draft Heal** button, or use the menu **Draft → Utilities → Heal**, or use the keyboard shortcut `H` (if assigned).
3. The command will attempt to fix each selected object. A report view message will indicate success or failure.

## Notes

- Not all broken objects can be healed. The command may fail on severely corrupted geometry.
- This command was introduced in FreeCAD version 0.19 (PR #4567).