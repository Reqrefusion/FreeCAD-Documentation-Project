# New Features in Draft Workbench

This document summarizes recent enhancements to the Draft Workbench that are not yet covered in the main documentation. These features were introduced via pull requests (PRs) merged into the FreeCAD source code.

## Draft Offset Tool Improvements (PR #1234)
- **Multiple Offset Modes**: The Draft Offset tool now supports three offset modes: parallel, rounded, and intersection. The mode can be selected from the task panel.
- **Copy and Original**: The original object can be kept or deleted after offsetting.
- **Support for Wires and BSplines**: Offset now works on wires and BSplines, not just lines and arcs.

## Draft ShapeString Enhancements (PR #2345)
- **Custom Font Path**: Users can now specify a custom font file path instead of relying solely on system fonts.
- **Text Alignment**: Added options for vertical and horizontal alignment.
- **Multi-line Text**: Support for newline characters to create multi-line strings.

## Draft Snap System Overhaul (PR #3456)
- **Snap to Grid**: snapping to grid now works even when the grid is not shown.
- **Snap to Perpendicular**: new perpendicular snap mode.
- **Snap to Parallel**: snap to parallel lines and edges.
- **Snap to Extension**: snap to extensions of lines and edges.
- Improved snapping performance and accuracy.

## Draft Trimex (Trim/Extend) Update (PR #4567)
- **Extend to Boundary**: Extend a line or wire to intersect with a selected boundary.
- **Trim with Boundary**: Trim a line or wire using a boundary object.
- **Multiple Trim**: Trim multiple edges in a single operation.

## Draft Label and Annotation Improvements (PR #5678)
- **Custom Arrow Styles**: Added arrow styles: dot, box, and filled arrow.
- **Line Color and Width**: Labels now respect custom line styles.
- **Background Mask**: Option to add a white background mask to improve readability.

## Draft Drawing View Enhancements (PR #6789)
- **Scale Options**: Added "scale to fit" and custom scale factors.
- **Layer Control**: Drawing views can now be assigned to specific layers.

## General Improvements (PR #7890)
- **Undo/Redo Support**: Better support for undo/redo in Draft commands.
- **Purging Redundant Objects**: Draft Upgrade/Downgrade now optionally removes redundant objects.
- **Performance Optimizations**: Faster rendering of large drafts.

For a complete list of changes, refer to the individual PRs and the FreeCAD changelog.