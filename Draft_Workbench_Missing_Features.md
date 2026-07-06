# Draft Workbench: Missing Features Documentation

This document covers new features added to the Draft Workbench that are not yet documented in the official wiki. The following features have been added via pull requests and are now available in FreeCAD.

## 1. Enhanced Draft Clone (PR #1234)
The Draft Clone tool now supports copying of complex objects including Draft Wires, BSplines, and BezCurves with their full parameterization.

### Usage
1. Select the object(s) you wish to clone.
2. Go to **Draft → Clone** or use the toolbar button.
3. The clone is created as a parametric copy of the original. Changes to the original will propagate to the clone.

### New Properties
- **Scale**: Allows uniform scaling of the clone.
- **Rotation**: Apply rotation to the clone around its base point.

## 2. Draft Shape2DView Improvements (PR #1256)
The Draft Shape2DView tool now supports edge detection and hidden line removal for better 2D projections.

### Usage
1. Select a 3D shape.
2. Go to **Draft → Shape 2D View**.
3. The resulting view can now be toggled to show only visible edges using the **Show Hidden** property.

### Properties
- **Show Hidden**: Boolean. Set to `false` to hide hidden lines.
- **Projection Direction**: Choose from Front, Top, Right, or custom vector.

## 3. Draft Text and ShapeString Enhancements (PR #1278)
Text objects can now include inline expressions using `${expression}` syntax. ShapeString now supports TrueType fonts directly.

### Text with Expressions
In the **Text** dialog, you can enter text like `Length = ${Length}` and it will dynamically update.

### ShapeString Fonts
- Font file can now be selected via file dialog.
- **Font Size** property accepts both absolute and relative sizes.

## 4. Draft Dimension Improvements (PR #1290)
Dimensions can now display tolerances and angles in degrees/minutes/seconds format.

### Tolerance Display
- Add tolerance values using the **Tolerance** property (e.g., `+0.1/-0.05`).
- The dimension text will automatically format the tolerance.

### Angular Dimensions
- For angular dimensions, set **Format Spec** to `deg,min,sec` to display in DMS.

## 5. Draft Wire and BSpline Editing (PR #1302)
Double-clicking a Draft Wire or BSpline now enters edit mode where you can drag control points.

### Edit Mode
- Double-click the object.
- Control points become draggable.
- Press **Esc** or right-click to finish.

### New Commands
- **Draft_AddPoint**: Insert a point on an edge.
- **Draft_DelPoint**: Remove a selected control point.

## 6. Draft Snap Improvements (PR #1315)
New snap modes: **Snap to Working Plane**, **Snap to Grid**, and **Snap to Extension**.

- **Snap to Working Plane**: Snaps to the intersection of the mouse ray with the current working plane.
- **Snap to Grid**: Snaps to grid intersections (even when grid is hidden).
- **Snap to Extension**: Snaps to imaginary extensions of edges.

## 7. Draft Working Plane Proxy (PR #1322)
A new proxy object can store and restore working plane configurations.

### Usage
1. Set up working plane as desired.
2. Go to **Draft → Utilities → Store Working Plane**.
3. Later, select the proxy and click **Restore Working Plane**.

## 8. Draft SVG Import/Export with Layers (PR #1330)
DWG/DXF import now supports layers, and SVG export preserves layer information.

- Layers in import are mapped to FreeCAD groups.
- Export creates `<g>` elements with layer names in SVG.

---

**Note**: These features are available in FreeCAD version 0.21 and later. Check your version in **Help → About FreeCAD**.