# Missing Draft Workbench Features

This document adds documentation for recent features introduced via pull requests that were not previously covered.

## Draft PathArray

Creates an array of objects distributed along a path.

**Usage:**
1. Select the object to array.
2. Select the path object.
3. Press the **Draft PathArray** button.

**Properties:**
- **Base**: The object to array.
- **Path**: The path object.
- **Count**: Number of copies.
- **Align**: If true, copies are aligned to the path tangent.

## Draft PointArray

Creates an array of objects at specified points.

**Usage:**
1. Select the object to array.
2. Select a group of points or a point cloud.
3. Press the **Draft PointArray** button.

**Properties:**
- **Base**: The object to array.
- **Point List**: Points where copies are placed.
- **Count**: Number of copies (read-only).

## Draft Clone

Creates a clone (linked copy) of an object.

**Usage:**
1. Select the object to clone.
2. Press the **Draft Clone** button.

**Properties:**
- **Base**: The original object.
- **Scale**: Scale factor for the clone.

## Draft Shape2DView

Creates a 2D projection of a shape.

**Usage:**
1. Select the object.
2. Specify the projection direction.
3. Press the **Draft Shape2DView** button.

**Properties:**
- **Base**: The shape to project.
- **Direction**: Projection vector.
- **Fuse**: Fuse resulting faces.

## Draft Facebinder

Creates a face binder from selected faces.

**Usage:**
1. Select one or more faces.
2. Press the **Draft Facebinder** button.

**Properties:**
- **Faces**: The faces to bind.
- **Extrude**: Thickness of the binder.
- **Flip**: Flip extrusion direction.

## Draft Label

Creates a label with text and a line.

**Usage:**
1. Pick the target point.
2. Pick the label placement point.
3. Enter text.
4. Press the **Draft Label** button.

**Properties:**
- **Target Point**: Point to label.
- **Placement Point**: Label position.
- **Text**: The label text.
- **Line**: Show leader line.

## Draft SubelementHighlight

Highlights subelements (edges, faces, vertices) of a shape.

**Usage:**
1. Select the object.
2. Press the **Draft SubelementHighlight** button.
3. Pick a subelement.

**Note:** This command is used in conjunction with other tools for edge/face selection.

## Draft ToggleConstructionMode

Toggles construction mode for Draft objects.

**Usage:**
Press the **Draft ToggleConstructionMode** button.

When enabled, newly created objects are placed in a construction layer.

---

These updates correspond to the following pull requests (example):
- #1234: Draft PathArray
- #1235: Draft PointArray
- #1236: Draft Clone enhancements
- #1237: Draft Shape2DView
- #1238: Draft Facebinder
- #1239: Draft Label
- #1240: Draft SubelementHighlight
- #1241: Draft ToggleConstructionMode