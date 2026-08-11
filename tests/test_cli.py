from click.testing import CliRunner

from chatppt import __version__
from chatppt.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatppt, version {__version__}" in result.output


def test_help_lists_tree_option_without_fake_commands():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output


def test_tree_option_renders_registered_empty_command_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert "chatppt # chatppt command line interface" in result.output
    assert "├── --help" in result.output
    assert "├── --version" in result.output
    assert "└── --tree" in result.output
    assert "hello" not in result.output.lower()
    assert "<group>" not in result.output
