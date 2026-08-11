# CLI Capability Map

This page is the compact capability map for the `ChatPPT` CLI. Use it to review which commands are first-class entries and which are still boundary or planned slots.

Importable Python functions are mapped in [Interface Tree](interface-tree.md). Current package boundaries are tracked in [Capability Map](capability-map.md).

## Current Runtime Command Tree

The block below is rendered by `chatppt --tree` from the real Click registry. `ChatPPT` currently has no business subcommands, so only root pseudo-options are shown.

```text
chatppt # chatppt command line interface
├── --help # Show this message and exit
├── --version # Show the package version
└── --tree # Show the registered CLI command tree

```

## Base Entries

```text
chatppt --help           # Verify the command is installed and inspect current help
chatppt --version        # Verify the installed version
chatppt --tree           # Print the current real CLI registry
```

## Business Command Status

This package currently has no business subcommands. Do not document template placeholders or sample commands as available entries. Only document a command as implemented after the command, Python function, and tests exist.

## Implementation Contract

- Every implemented command must map back to a Python function, class, or service layer.
- If a command writes remote state, document credentials, permissions, dry-run/checkpoint behavior, or confirmation boundaries.
- When adding a command, update README, the interface tree, capability map, tests, and related flow pages together.
