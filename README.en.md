<div align="center">
    <a href="https://pypi.python.org/pypi/ChatPPT">
        <img src="https://img.shields.io/pypi/v/ChatPPT.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatPPT/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatPPT/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatPPT/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatPPT

ChatArch PPT tooling package.


Documentation entry: <https://arch.gh.wzhecnu.cn/ChatPPT/en/>

Choose documentation by scenario:

| Scenario | Document |
| --- | --- |
| Install the package, run the CLI, and confirm it works | `docs/cli-tree.en.md` |
| Check first-class capabilities and current boundaries | `docs/capability-map.en.md` |
| Call package behavior directly from Python | `docs/interface-tree.md` |

## Quick Start

```bash
pip install -e ".[dev]"
chatppt --help
chatppt --version
chatppt --tree
chatppt --tree-brief
python -m pytest -q
python -m build
```

## CLI Contract

This package depends on `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`. New commands should prefer:

- `add_tree_option()` to generate `--tree` and `--tree-brief` from the real Click registry.
- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- The typed provider in `config.py` and the `chatenv.configs` entry point make the package ChatEnv-discoverable while ChatEnv owns active and named profile storage paths.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by mkdocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
