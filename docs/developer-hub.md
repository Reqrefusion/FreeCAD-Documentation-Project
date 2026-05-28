# Developer Hub

Welcome to the FreeCAD Developer Hub! This page provides resources for developers who want to contribute to FreeCAD.

## Getting Started

### Development Environment Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/FreeCAD/FreeCAD.git
   cd FreeCAD
   ```

2. **Install Dependencies**
   - **Windows:** See [Build on Windows](https://wiki.freecad.org/Compile_on_Windows)
   - **macOS:** See [Build on macOS](https://wiki.freecad.org/Compile_on_MacOS)
   - **Linux:** See [Build on Linux](https://wiki.freecad.org/Compile_on_Linux)

3. **Build FreeCAD**
   ```bash
   mkdir build
   cd build
   cmake ..
   make -j$(nproc)
   ```

## Current Developer Resources

### Official Documentation

- [Developers Handbook](https://freecad.github.io/DevelopersHandbook) - Comprehensive guide for FreeCAD developers
- [Source Documentation](https://github.com/FreeCAD/SourceDoc) - Auto-generated source code documentation
- [Addon Academy](https://github.com/FreeCAD/Addon-Academy) - Guide for creating FreeCAD add-ons
- [Lens Documentation](https://github.com/FreeCAD/lens-docs) - Documentation for the Lens module

### Contributing Guidelines

- [Contributing Guide](https://github.com/FreeCAD/FreeCAD/blob/main/CONTRIBUTING.md) - How to contribute to FreeCAD
- [Code Style Guide](https://github.com/FreeCAD/FreeCAD/blob/main/CODING.md) - Coding standards and conventions
- [Issue Tracker](https://github.com/FreeCAD/FreeCAD/issues) - Report bugs and request features

### Community

- [Discord Server](https://discord.gg/FreeCAD) - Real-time chat with developers
- [Forum](https://forum.freecad.org) - Community discussions and support
- [Stack Overflow](https://stackoverflow.com/questions/tagged/freecad) - Technical Q&A

## Architecture Overview

### Core Modules

| Module | Description | Location |
|--------|-------------|----------|
| **App** | Core application framework | `src/App/` |
| **Gui** | GUI framework and 3D view | `src/Gui/` |
| **Base** | Base utilities and types | `src/Base/` |
| **Mod** | Workbench modules | `src/Mod/` |

### Key Technologies

- **C++** - Core application
- **Python** - Scripting and workbenches
- **Qt** - GUI framework
- **Coin3D** - 3D visualization
- **OpenCascade** - CAD kernel

## Development Workflows

### Creating a Workbench

1. Use the [AddonTemplate](https://github.com/FreeCAD/AddonTemplate)
2. Follow the [Workbench Creation Guide](https://wiki.freecad.org/Workbench_creation)
3. Test with the Addon Manager

### Submitting Changes

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

### Testing

```bash
# Run tests
cd build
ctest

# Run specific test
ctest -R TestName
```

## Links

- [FreeCAD Wiki](https://wiki.freecad.org)
- [Source Code](https://github.com/FreeCAD/FreeCAD)
- [Bug Tracker](https://github.com/FreeCAD/FreeCAD/issues)
- [Release Notes](https://github.com/FreeCAD/FreeCAD/blob/main/CHANGELOG.md)
