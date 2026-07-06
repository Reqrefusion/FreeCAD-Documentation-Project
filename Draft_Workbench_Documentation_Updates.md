# Draft Workbench Documentation Updates

This document adds missing documentation for features recently added to the Draft Workbench.

## New Draft Commands

### Draft Fillet
Creates a fillet (rounded corner) or chamfer between two edges of a Draft Wire or Draft BSpline.

**Usage:**
1. Select two connected edges of a Draft Wire or Draft BSpline.
2. Press the **Draft Fillet** button.
3. Set the radius in the task panel. For a chamfer, enable the "Chamfer" option and set the chamfer size.

The result is a new Draft Wire with the fillet/chamfer applied.

### Draft Trim/Extend
Trims or extends a Draft object to an intersection with another object.

**Usage:**
1. Select the first object (the one to trim/extend).
2. Press the **Draft Trim** or **Draft Extend** button.
3. Select the second object (the cutting/boundary edge).
4. The first object is trimmed/extended to the nearest intersection.

**Note:** Works with Draft Wires, Lines, and Arcs.

### Draft Offset
Creates a parallel copy of a Draft object at a given distance.

**Usage:**
1. Select the object to offset.
2. Press the **Draft Offset** button.
3. Set the offset distance. Enable "Copy" to keep the original.
4. Optionally enable "Fill" to create a closed shape offset (for wires).
5. Click in the 3D view to set the direction.

### Draft Clone
Creates a parametric clone of a Draft object.

**Usage:**
1. Select one or more objects.
2. Press the **Draft Clone** button.
3. The clone updates when the original is modified.

**Properties:**
- **Scale:** Sets overall scale factor.
- **Fuse:** If multiple originals, fuses them into one clone.

### Draft Mirror
Mirrors a Draft object across a plane.

**Usage:**
1. Select the object.
2. Press the **Draft Mirror** button.
3. Pick three points in the 3D view to define the mirror plane, or select a face.
4. The mirrored copy is created.

### Draft Rotate
Rotates a Draft object around a center point.

**Usage:**
1. Select the object(s).
2. Press the **Draft Rotate** button.
3. Pick the rotation center.
4. Set the base angle (starting from current orientation) and rotation angle.
5. Optionally enable "Copy" to create a rotated copy.

### Draft Scale
Scales a Draft object uniformly or non-uniformly.

**Usage:**
1. Select the object.
2. Press the **Draft Scale** button.
3. Pick the scaling center.
4. Enter scale factors for X, Y, Z (or uniform).
5. Optionally enable "Copy" to create a scaled copy.

## Draft Panel Enhancements

### Improved Draft Layer
Layers now support auto-grouping: objects created while a layer is active are automatically added to it. The layer's line color, line width, and shape color are applied to new objects.

### Draft Annotation Enhancements
- **Draft Text**: Now supports multi-line text and custom font files.
- **Draft Dimension**: New "Override" property to set a custom dimension string.
- **Draft Label**: Can display a custom text and arrow.

### Draft Snap Improvements
- **Snap Near**: Snaps to the nearest point on an edge.
- **Snap Parallel**: Snaps along a line parallel to an existing edge.
- **Snap Extension**: Snaps to an imaginary extension of an edge.

### Draft Working Plane Proxy
Allows storing a working plane orientation in a document object for later reuse.

## Deprecated Commands
- **Draft Array** (use Draft PolarArray, Draft CircularArray, Draft PathArray, Draft OrthoArray)
- **Draft Drawing** (use TechDraw Workbench)

## See Also
- [Draft Workbench](https://wiki.freecadweb.org/Draft_Workbench)
- [Release Notes](https://wiki.freecadweb.org/Release_notes_0.20)