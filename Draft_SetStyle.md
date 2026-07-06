# Draft SetStyle

## Description

The **Draft SetStyle** command applies a saved annotation style to selected objects. It is useful for quickly uniformizing dimensions, texts, and other annotations.

## Usage

1. Select one or more annotation objects (e.g., dimensions, texts, labels).
2. Invoke the command via **Draft → Utilities → Set style** or the toolbar button.
3. In the dialog, pick an annotation style from the list.
4. Click **OK** to apply. The selected objects will inherit the style's properties.

## Notes

- Only annotation objects that support style inheritance are affected.
- The style must be defined using the **AnnotationStyleEditor**.

## Scripting

```python
import Draft

# Apply a style to a list of objects
style_name = "MyStyle"
objects = Gui.Selection.getSelectionEx()
for obj in objects:
    Draft.setStyle(obj.Object, style_name)
```