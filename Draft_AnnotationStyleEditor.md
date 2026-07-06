# Draft AnnotationStyleEditor

## Description

The **Draft AnnotationStyleEditor** command allows you to create, edit, and manage annotation styles. Annotation styles are collections of visual properties (font size, arrow style, color, etc.) that can be applied to dimensions, texts, and other annotations.

## Usage

1. Invoke the command via the menu **Draft → Utilities → Annotation style editor** or the toolbar button.
2. The dialog shows existing styles. Select one to edit or click **New** to create a new style.
3. Set the properties (font, line width, arrow symbol, etc.).
4. Click **OK** to save. The style will appear in the list.
5. To apply a style to an annotation, use the **SetStyle** command.

## Properties

- **Font**: Font name and size.
- **Arrow type**: Dot, arrow, tick, etc.
- **Color**: Text and line colors.
- **Unit format**: Precision, unit symbol, etc.

## Notes

- Annotation styles are stored in the document.
- Styles can be shared across documents via import/export.

## Limitations

- Changing a style after annotations have been created will update only those annotations that were linked to the style.

## Scripting

See [Draft API](Draft_API.md) for Python scripting of annotation styles.