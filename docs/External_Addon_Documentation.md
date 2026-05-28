# FreeCAD External Add-on Documentation

## Overview

FreeCAD has a rich ecosystem of external add-ons that extend its functionality beyond the core workbenches. This guide provides comprehensive documentation for the most popular and useful external add-ons.

## Installation

### Using the Addon Manager

1. Open FreeCAD
2. Go to **Tools → Addon Manager**
3. Browse or search for the add-on you want
4. Click **Install** and restart FreeCAD

### Manual Installation

1. Download the add-on repository
2. Copy to your FreeCAD Mod directory:
   - **Linux**: `~/.local/share/FreeCAD/Mod/`
   - **Windows**: `%APPDATA%\FreeCAD\Mod\`
   - **macOS**: `~/Library/Application Support/FreeCAD/Mod/`
3. Restart FreeCAD

## Popular External Add-ons

### 1. Assembly4
**Category**: Assembly  
**Repository**: [GitHub](https://github.com/Zolko-123/Assembly4)

Assembly4 is a powerful assembly workbench that uses expressions and constraints to create parametric assemblies.

**Key Features**:
- LCS (Local Coordinate System) based assembly
- Expression-driven constraints
- Animation support
- BOM (Bill of Materials) generation

**Quick Start**:
1. Install Assembly4 from Addon Manager
2. Create a new assembly document
3. Add parts using the "Insert Link" tool
4. Constrain parts using LCS alignment

### 2. Curves Workbench
**Category**: Modeling  
**Repository**: [GitHub](https://github.com/tomate44/CurvesWB)

Advanced curve and surface modeling tools for creating complex shapes.

**Key Features**:
- Gordon surfaces
- Curve interpolation
- Surface fitting
- Blend curves

### 3. SheetMetal Workbench
**Category**: Manufacturing  
**Repository**: [GitHub](https://github.com/shaise/FreeCAD_SheetMetal)

Tools for designing sheet metal parts with bend, fold, and unfold capabilities.

**Key Features**:
- Bend radius calculation
- Flat pattern generation
- K-factor support
- DXF export for manufacturing

### 4. A2plus
**Category**: Assembly  
**Repository**: [GitHub](https://github.com/kbwbe/A2plus)

Assembly workbench with constraint-based positioning.

**Key Features**:
- Multiple constraint types (coincident, parallel, tangent)
- Auto-solve constraints
- Assembly visualization
- Part library

### 5. Fasteners Workbench
**Category**: Standard Parts  
**Repository**: [GitHub](https://github.com/shaise/FreeCAD_Fasteners_Workbench)

Create and manage standard fasteners (bolts, nuts, screws, washers).

**Key Features**:
- ISO, DIN, ANSI standards
- Parametric sizing
- Auto-attachment to holes
- Bill of materials

### 6. TechDraw Workbench Extensions
**Category**: Documentation  
**Repository**: [GitHub](https://github.com/WandererFan/FreeCAD-TechDraw-Extension)

Extended TechDraw tools for creating detailed engineering drawings.

**Key Features**:
- Advanced dimensioning
- Section views
- Detail views
- GD&T symbols

### 7. FEM Workbench Extensions
**Category**: Analysis  
**Repository**: Various

Extended FEM (Finite Element Method) capabilities for structural and thermal analysis.

**Key Features**:
- Material libraries
- Advanced meshing
- Result visualization
- Report generation

### 8. Macro Collection
**Category**: Automation  
**Repository**: [FreeCAD Macros](https://github.com/FreeCAD/FreeCAD-macros)

Collection of Python macros for automating repetitive tasks.

**Popular Macros**:
- **Macro_FCCrea**: Create standard parts
- **Macro_SheetMetal_Unfolder**: Unfold sheet metal
- **Macro_CenterOfMass**: Calculate center of mass
- **Macro_Align**: Align objects

## Developing External Add-ons

### Project Structure

```
MyWorkbench/
├── Init.py                 # Workbench initialization
├── InitGui.py             # GUI initialization
├── MyWorkbench.py         # Main workbench class
├── MyCommands.py          # Command definitions
├── Resources/
│   ├── icons/             # SVG icons
│   └── ui/                # UI files
├── Tests/                 # Unit tests
└── README.md
```

### Best Practices

1. **Follow FreeCAD conventions** - Use consistent naming and structure
2. **Handle errors gracefully** - Provide meaningful error messages
3. **Document your code** - Include docstrings and comments
4. **Test thoroughly** - Test with different FreeCAD versions
5. **Maintain compatibility** - Support Python 3.x

### Publishing Your Add-on

1. Create a GitHub repository
2. Add a `package.xml` metadata file
3. Include a `README.md` with installation instructions
4. Submit to the FreeCAD Addon Repository

## Troubleshooting

### Common Issues

**Add-on not appearing in Addon Manager**:
- Check internet connection
- Verify FreeCAD version compatibility
- Check Python dependencies

**Import errors**:
- Ensure all dependencies are installed
- Check Python path configuration
- Verify module names

**Performance issues**:
- Disable unused add-ons
- Check for memory leaks
- Update to latest version

### Getting Help

- **FreeCAD Forum**: https://forum.freecad.org
- **GitHub Issues**: Report bugs on the add-on's repository
- **Documentation**: Check the add-on's README

## Contributing

To improve this documentation:
1. Fork this repository
2. Make your changes
3. Submit a pull request
4. Follow the contribution guidelines

## Resources

- [FreeCAD Addon Repository](https://github.com/FreeCAD/FreeCAD-addons)
- [Addon Manager Documentation](https://wiki.freecad.org/Addon_Manager)
- [FreeCAD Python Scripting](https://wiki.freecad.org/Python_scripting_tutorial)
- [Developer Handbook](https://freecad.github.io/DevelopersHandbook)

---

*Last updated: May 2026*
