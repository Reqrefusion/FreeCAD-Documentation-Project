# Draft Layer

Layers are used to organize objects. The Draft Workbench has improved layer management with support for nesting (layers within layers) and property inheritance.

## Creating a Layer

- Use the **Draft Layer** command from the **Utilities** menu.
- A new layer is created and added to the document tree.

## Managing Layers

- Drag and drop objects onto a layer to assign them.
- Layer properties (color, line width, visibility) can be set in the property editor.
- **Layer Groups**: You can now create groups of layers for better organization.

## Layer Properties

- **Visibility**: Show/hide all objects in the layer.
- **Color**: Default color for new objects in the layer.
- **Line width**: Default line width.
- **Transparency**: Override transparency.

## Notes

- Objects inherit the layer's default properties only if they are set to "inherit".
- Layer groups can be toggled together.

## Scripting

```python
import Draft
layer = Draft.makeLayer(name="MyLayer")
layer.ViewObject.LineColor = (1.0, 0.0, 0.0)  # Red
layer.ViewObject.Visibility = True
```