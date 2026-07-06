## Draft ShapeString

### Description
The Draft ShapeString command inserts a compound shape representing a text string at a given point in the document. The text, size, tracking, and font can be specified.

### Usage
1. Press the **Draft ShapeString** button, or use the menu **Draft → Utilities → ShapeString**.
2. Click a point in the 3D view to position the text.
3. Enter the text and adjust properties in the task panel.
4. Press **OK** to create the shape.

### Options
- **Text**: The string to display.
- **Height**: The font height in document units.
- **Tracking**: The spacing between characters.
- **Font**: Choose from system fonts or a custom font file.

### Notes
- ShapeStrings can be converted to sketches for further editing.
- The text is a parametric shape that can be modified after creation.

### Properties
- **Position**: X, Y, Z coordinates.
- **Font File**: Path to the font file.
- **String**: The text content.
- **Size**: Font height.
- **Tracking**: Character spacing.

### Scripting
See the [FreeCAD Scripting Basics](https://wiki.freecadweb.org/FreeCAD_Scripting_Basics) for more information.

Example:
```python
import FreeCAD as App
import Draft

doc = App.newDocument()
shape = Draft.make_shape_string("Hello", App.Vector(0,0,0), size=10)
doc.recompute()
```

### Availability
Introduced in version 0.19.