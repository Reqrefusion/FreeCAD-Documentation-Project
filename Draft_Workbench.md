# Draft Workbench

The Draft Workbench is primarily focused on creating and modifying 2D objects in FreeCAD. It also provides tools for snapping, working planes, and basic 2D drafting operations.

## New Features in Version 0.20

- **Draft WorkingPlaneProxy**: This new tool creates a proxy object that stores the current working plane position and orientation. It allows you to quickly switch between saved working planes.
- **Draft SetWorkingPlane**: Enhanced with on-selection and view-aligned modes.
- **Draft Snap Manager**: Added new snap types: Endpoint, Midpoint, Perpendicular, and more. The snap toolbar now supports toggling individual snaps.
- **Draft Text**: Improved editing capabilities and support for multi-line text.
- **Draft Shape2DView**: Now supports projection of 3D shapes onto the working plane with customizable direction.
- **Draft Layer**: Layers can now be created, renamed, and organized directly from the Draft Workbench. Layer visibility and line color/width properties are available.
- **Draft Wire to BSpline**: New command to convert Draft Wires to B-Splines.
- **Draft Clone**: Now supports non-uniform scaling.

For a complete list of changes, see the [Release Notes](https://wiki.freecadweb.org/Release_notes_0.20).
