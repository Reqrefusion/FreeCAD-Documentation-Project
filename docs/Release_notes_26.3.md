# FreeCAD 26.3 Release Notes

## New Features

### Python API

- **`FreeCADGui.Selection` enhancements**:
  - New `Selection.addSelection()` method now supports batch selection of multiple objects in a single call.
  - Added `Selection.getPreSelectedObject()` to retrieve the currently pre-selected object without triggering a full selection update.
  - `Selection.clearSelection()` now accepts an optional `keep_preselection` parameter to preserve the pre-selection state.

- **`Part` module improvements**:
  - New `Part.makeLoft()` parameter `ruled` for creating ruled lofts between profiles.
  - `Part.Shape.exportBrep()` now supports an optional `version` parameter to control the BRep file format version (V1 or V2).
  - Added `Part.Shape.getSubShape()` method to extract sub-shapes by path (e.g., `"Face1.Edge2"`).
  - `Part.makeThickness()` now supports a `tolerance` parameter for more precise shell operations.

- **`Draft` module**:
  - New `Draft.makeArray()` parameter `use_link` to create linked arrays instead of copies.
  - `Draft.makeWire()` now accepts a `closed` parameter to automatically close the wire.
  - Added `Draft.getVisibleObjects()` utility function to retrieve all visible objects in the active document.

- **`Spreadsheet` module**:
  - New `Sheet.setAlias()` method for programmatically setting cell aliases.
  - Added support for `=IF()`, `=AND()`, and `=OR()` logical functions in spreadsheet formulas.
  - `Sheet.getContents()` now returns a dictionary mapping cell addresses to values for faster bulk access.

### Workbench Updates

#### Part Workbench
- New **"Create Ruled Loft"** tool in the Part menu for generating lofts with ruled surfaces between two or more profiles.
- **"Refine Shape"** operation now available as a standalone tool in the Part menu (previously only accessible via the Part Design workbench).
- Added **"Convert to BSpline"** tool for converting NURBS curves and surfaces to BSpline representations.

#### Draft Workbench
- New **"Array (Linked)"** tool that creates parametric linked arrays, allowing the source object to be modified and have all array instances update automatically.
- **"Wire"** tool now has a "Close" checkbox in the task panel to automatically close the resulting wire.
- Added **"Offset 2D"** tool for creating offset curves from existing 2D geometry.

#### Spreadsheet Workbench
- New logical functions: `=IF(condition, value_if_true, value_if_false)`, `=AND(condition1, condition2, ...)`, and `=OR(condition1, condition2, ...)`.
- Cell aliases can now be set programmatically via the Python API using `Sheet.setAlias()`.
- Improved formula parser performance for large spreadsheets (up to 50% faster for sheets with 10,000+ cells).

#### Mesh Workbench
- New **"Decimate Mesh"** tool with adjustable target face count and quality parameters.
- **"Remesh"** operation now supports anisotropic remeshing for better preservation of feature edges.
- Added **"Mesh Statistics"** dialog showing face count, edge count, vertex count, and bounding box dimensions.

### Performance Improvements

- **BRep operations**: Boolean operations (union, intersection, difference) are now up to 30% faster for complex shapes with more than 100 faces.
- **Mesh processing**: Mesh boolean operations and mesh-mesh intersections have been optimized, resulting in up to 40% speedup for meshes with 100,000+ faces.
- **Document loading**: Loading of large documents (100+ objects) is now 20% faster due to improved dependency resolution.
- **Rendering**: Viewport rendering of scenes with 50,000+ triangles is now smoother due to improved frustum culling.

### Command-Line Options

- New `--export-format` option to specify the export format when using `--export` in headless mode.
  