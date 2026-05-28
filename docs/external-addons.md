# External Add-on Documentation

This guide provides comprehensive documentation for external add-ons in FreeCAD, organized by category.

## Categories

### Workbench Add-ons

| Add-on | Description | Maintainer | Documentation |
|--------|-------------|------------|---------------|
| [Fasteners](https://github.com/shaise/FreeCAD_FastenersWB) | Create standard fasteners (screws, nuts, washers) | shaise | [Docs](https://github.com/shaise/FreeCAD_FastenersWB/wiki) |
| [SheetMetal](https://github.com/shaise/FreeCAD_SheetMetal) | Sheet metal design tools | shaise | [Docs](https://github.com/shaise/FreeCAD_SheetMetal/wiki) |
| [A2plus](https://github.com/kbwateruser/A2plus) | Assembly workbench | kbwateruser | [Docs](https://github.com/kbwateruser/A2plus/wiki) |
| [Assembly4](https://github.com/Zolko-123/FreeCAD_Assembly4) | Assembly workbench using expressions | Zolko-123 | [Docs](https://github.com/Zolko-123/FreeCAD_Assembly4/wiki) |
| [Curves](https://github.com/tomate44/CurvesWB) | NURBS curve tools | tomate44 | [Docs](https://github.com/tomate44/CurvesWB/wiki) |

### CAM/CNC Add-ons

| Add-on | Description | Maintainer | Documentation |
|--------|-------------|------------|---------------|
| [CAM Workbench](https://github.com/sliptonic/FreeCAD_CAM_Workbench) | CNC machining workbench | sliptonic | [Docs](https://wiki.freecad.org/CAM_Workbench) |
| [Path Workbench](https://github.com/FreeCAD/FreeCAD/tree/main/src/Mod/Path) | Built-in CNC path generation | FreeCAD | [Docs](https://wiki.freecad.org/Path_Workbench) |

### Architecture Add-ons

| Add-on | Description | Maintainer | Documentation |
|--------|-------------|------------|---------------|
| [BIM](https://github.com/yorikvanhavre/BIM_Workbench) | BIM modeling tools | yorikvanhavre | [Docs](https://github.com/yorikvanhavre/BIM_Workbench/wiki) |
| [Steel Column](https://github.com/mwganson/steel_column) | Steel column generator | mwganson | [Docs](https://github.com/mwganson/steel_column/wiki) |

### Utility Add-ons

| Add-on | Description | Maintainer | Documentation |
|--------|-------------|------------|---------------|
| [AddonManager](https://github.com/FreeCAD/FreeCAD/tree/main/src/Mod/AddonManager) | Built-in add-on manager | FreeCAD | [Docs](https://wiki.freecad.org/AddonManager) |
| [Macro Menu](https://github.com/FreeCAD/FreeCAD/tree/main/src/Mod/Macro) | Macro management | FreeCAD | [Docs](https://wiki.freecad.org/Macros) |

## Installation

### Using the Addon Manager
1. Open FreeCAD
2. Go to **Tools → Addon Manager**
3. Browse available add-ons
4. Click **Install** on the desired add-on
5. Restart FreeCAD

### Manual Installation
1. Download the add-on repository
2. Extract to your FreeCAD Mod directory:
   - **Windows:** `%APPDATA%\FreeCAD\Mod\`
   - **macOS:** `~/Library/Application Support/FreeCAD/Mod/`
   - **Linux:** `~/.FreeCAD/Mod/`
3. Restart FreeCAD

## Creating Your Own Add-on

### Getting Started
1. Use the [AddonTemplate](https://github.com/FreeCAD/AddonTemplate) as a starting point
2. Follow the [Add-on Development Guide](https://wiki.freecad.org/Workbench_creation)
3. Submit your add-on to the [Addon Repository](https://github.com/FreeCAD/FreeCAD-Addon-Academy)

### Best Practices
- Follow the [FreeCAD coding standards](https://github.com/FreeCAD/FreeCAD/blob/main/CODING.md)
- Include comprehensive documentation
- Add unit tests
- Use proper error handling
- Follow the Addon Academy guidelines

## Links

- [FreeCAD Addon Academy](https://github.com/FreeCAD/Addon-Academy)
- [Source Documentation](https://github.com/FreeCAD/SourceDoc)
- [Developers Handbook](https://freecad.github.io/DevelopersHandbook)
- [Lens Documentation](https://github.com/FreeCAD/lens-docs)
- [FreeCAD Wiki](https://wiki.freecad.org)
