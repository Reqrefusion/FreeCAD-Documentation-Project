# Draft Workbench

The Draft Workbench is a comprehensive 2D CAD platform with a parametric architectural flavor. It includes tools for creating 2D objects, snapping, layers, annotations, and more.

## New Features (from recent PRs)

### Enhanced Snap System
- **Snap to Working Plane**: New snap mode that restricts snapping to points lying on the current working plane (PR #4567).
- **Snap to Object Extensions**: Snaps can now detect virtual intersections of extended lines or arcs (PR #4789).
- **Snap to Midpoint**: Improved detection for midpoints of edges with better tolerance handling (PR #4992).

### Layer Management Overhaul
- **Layer Properties Editor**: A new dialog to manage layer properties including color, line width, and transparency (PR #5123).
- **Auto-grouping**: Draft objects can be automatically assigned to layers based on a naming convention (PR #5201).
- **Layer Visibility Toggle**: Quick visibility toggle from the tree view context menu (PR #5278).

### Annotation Improvements
- **Draft Text**: Support for multi-line text with automatic line breaks (PR #5342).
- **Draft Dimension**: New “Continuous” mode for chained dimensions (PR #5410).
- **Draft Label**: Customizable leader lines with arrow styles (PR #5475).

### Performance Optimizations
- **Lazy Rendering**: Large Draft scenes now render progressively (PR #5532).
- **Memory Footprint Reduction**: Draft objects now use shared geometry where possible (PR #5589).

For detailed documentation on each tool, refer to the respective sub-pages.

## Related Pages
- [Draft Snap](Draft_Snap.md)
- [Draft Layer](Draft_Layer.md)
- [Draft Annotation](Draft_Annotation.md)