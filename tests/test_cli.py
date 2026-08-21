from pathlib import Path

import click
from click.testing import CliRunner

from chatppt import __version__
from chatppt.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatppt, version {__version__}" in result.output


def test_help_lists_full_and_brief_tree_options_without_fake_commands():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "--tree-brief" in result.output
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output


def test_tree_options_render_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])
    brief = CliRunner().invoke(main, ["--tree-brief"])

    assert result.exit_code == 0, result.output
    assert brief.exit_code == 0, brief.output
    assert result.output == (
        "chatppt\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )
    assert brief.output == result.output
    assert result.output.splitlines().count("chatppt") == 1
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output


def test_tree_brief_omits_registered_command_signatures():
    @click.command(name="render", help="Render one presentation; writes an artifact.")
    @click.argument("source")
    @click.option("--format", "output_format")
    def render(source: str, output_format: str | None) -> None:
        del source, output_format

    main.add_command(render)
    try:
        full = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("render", None)

    assert full.exit_code == brief.exit_code == 0
    assert (
        "render <SOURCE> [--format OUTPUT-FORMAT]  # Render one presentation; writes an artifact."
        in full.output
    )
    assert "render  # Render one presentation; writes an artifact." in brief.output
    assert "<SOURCE>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output


def test_tree_root_uses_public_console_command_in_module_mode():
    result = CliRunner().invoke(main, ["--tree"], prog_name="python -m chatppt.cli")

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chatppt"
    assert "python -m chatppt.cli" not in result.output


def test_bilingual_cli_tree_docs_embed_registered_full_tree():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    documented_tree = f"```text\n{result.output.rstrip()}\n```"
    for path in (Path("docs/cli-tree.md"), Path("docs/cli-tree.en.md")):
        assert documented_tree in path.read_text(encoding="utf-8")
