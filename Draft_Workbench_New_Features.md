# Draft Workbench New Features

This page documents new features added to the Draft Workbench via recent pull requests.

## Draft Fillet

- **Added in PR #1234**
- Creates a fillet (rounded corner) between two Draft lines or wires.
- Usage: Select two edges or lines, then run `Draft Fillet`. Specify radius in the task panel.
- See also: [Draft Fillet documentation](Draft_Fillet.md)

## Draft Chamfer

- **Added in PR #1235**
- Creates a chamfer (beveled edge) between two Draft lines or wires.
- Usage: Select two edges, then run `Draft Chamfer`. Specify chamfer distances.
- See also: [Draft Chamfer documentation](Draft_Chamfer.md)

## Draft Heal

- **Added in PR #1236**
- Repairs broken wires by connecting endpoints within a tolerance.
- Usage: Select a set of edges, then run `Draft Heal`. Adjust tolerance as needed.
- See also: [Draft Heal documentation](Draft_Heal.md)

## Improvements

- **Draft Line enhancement (PR #1240)**: Added snap to grid while drawing.
- **Draft Dimension update (PR #1241)**: Support for angular dimensions.
