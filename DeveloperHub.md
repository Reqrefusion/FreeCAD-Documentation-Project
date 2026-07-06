# FreeCAD Developer Hub

Welcome to the FreeCAD Developer Hub! This is the central starting point for developers contributing to FreeCAD, creating add-ons, or extending the application. Here you'll find essential resources, architecture overviews, and guidelines.

## Getting Started

- [FreeCAD Developers Handbook](https://freecad.github.io/DevelopersHandbook) – The official handbook covering build instructions, code structure, and contribution workflows.
- [Source Documentation (SourceDoc)](https://github.com/FreeCAD/SourceDoc) – Auto-generated Doxygen documentation for the FreeCAD source code.
- [Lens Docs](https://github.com/FreeCAD/lens-docs) – In-depth documentation on specific subsystems like the constraint solver, topology naming, and more.

## Architecture Overview

FreeCAD is a parametric 3D modeler built on a modular architecture. Key components:
- **App**: Core application logic, document management, and data model.
- **Gui**: Qt-based graphical user interface.
- **Mod**: Modules (e.g., Part, PartDesign, Sketcher) that extend functionality.
- **Base**: Utility classes (vectors, matrices, etc.).

The handbook provides a detailed map of the codebase.

## Contributing to FreeCAD

- **Code contributions**: Follow the [Contribution Guidelines](https://freecad.github.io/DevelopersHandbook/contributing/) in the Developers Handbook.
- **Bug reports & feature requests**: Use the [FreeCAD issue tracker](https://github.com/FreeCAD/FreeCAD/issues).
- **Translation**: Help translate FreeCAD via Crowdin (see handbook).
- **Community**: Join the [FreeCAD Forum](https://forum.freecadweb.org) and developer channels.

## Addon Development

FreeCAD supports add-ons (workbenches, macros, preference packs). Resources:
- [Addon Academy](https://github.com/FreeCAD/Addon-Academy) – Tutorials and examples for creating add-ons.
- [Addon Manager](https://wiki.freecadweb.org/Addon_Manager) – How to distribute your add-on.
- [Workbench Creation](https://wiki.freecadweb.org/Workbench_creation) – Guide on building a custom workbench.

### Steps to Create an Addon
1. Set up a development environment (see Developers Handbook).
2. Use the [Addon Academy templates](https://github.com/FreeCAD/Addon-Academy/tree/main/templates) as a starting point.
3. Implement your workbench, macro, or pack.
4. Test with the latest FreeCAD version.
5. Submit to the Addon Manager by creating a pull request to the [FreeCAD-addons repository](https://github.com/FreeCAD/FreeCAD-addons).

## Source Documentation & Code Exploration

- **SourceDoc**: Automated Doxygen output – ideal for navigating the core APIs.
- **Lens Docs**: Human-written deep dives into solver, topology, and other complex areas.
- **Online code search**: Use [SourceGraph](https://sourcegraph.com/github.com/FreeCAD/FreeCAD) or GitHub's built-in search.

## Testing and Quality Assurance

- [Testing guide](https://freecad.github.io/DevelopersHandbook/testing/) – How to run unit tests and write new ones.
- [Continuous Integration](https://github.com/FreeCAD/FreeCAD/actions) – GitHub Actions workflows for builds and tests.

## License and Governance

FreeCAD is licensed under LGPL-2.0+ and is managed by a core team. See [Governance](https://freecad.github.io/DevelopersHandbook/governance/) in the handbook.

## Additional Resources

- [FreeCAD Wiki](https://wiki.freecadweb.org) – General user documentation.
- [Developer forums](https://forum.freecadweb.org/viewforum.php?f=10) – Discuss development topics.
- [GitHub organization](https://github.com/FreeCAD) – All official repositories.

---

_Last updated by the FreeCAD Documentation Project._