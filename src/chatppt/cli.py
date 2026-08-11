"""CLI entrypoint for chatppt."""

import click

from chatppt import __version__


def _command_help(command: click.Command) -> str:
    return (command.short_help or command.help or "").strip().rstrip(".")


def _group_items(group: click.Group) -> list[tuple[str, str | click.Command]]:
    items: list[tuple[str, str | click.Command]] = [
        ("--help", "Show this message and exit"),
        ("--version", "Show the package version"),
        ("--tree", "Show the registered CLI command tree"),
    ]
    for name, command in group.commands.items():
        if command.hidden:
            continue
        items.append((name, command))
    return items


def render_cli_tree(root: click.Group | None = None) -> str:
    """Render the registered Click command tree for `chatppt --tree`."""
    if root is None:
        root = main

    lines = [f"{root.name or 'chatppt'} # {_command_help(root)}"]

    def walk(items: list[tuple[str, str | click.Command]], prefix: str = "") -> None:
        for index, (name, item) in enumerate(items):
            last = index == len(items) - 1
            branch = "└── " if last else "├── "
            child_prefix = prefix + ("    " if last else "│   ")
            if isinstance(item, str):
                lines.append(f"{prefix}{branch}{name} # {item}")
                continue
            help_text = _command_help(item)
            line = f"{prefix}{branch}{name}"
            if help_text:
                line += f" # {help_text}"
            lines.append(line)
            if isinstance(item, click.Group):
                walk(_group_items(item), child_prefix)

    walk(_group_items(root))
    return "\n".join(lines)


def _tree_callback(ctx: click.Context, _param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    if not isinstance(ctx.command, click.Group):
        raise click.ClickException("--tree is only available on command groups")
    click.echo(render_cli_tree(ctx.command))
    ctx.exit()


@click.group(name="chatppt")
@click.version_option(__version__, prog_name="chatppt")
@click.option(
    "--tree",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=_tree_callback,
    help="Show the registered CLI command tree.",
)
def main() -> None:
    """chatppt command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
