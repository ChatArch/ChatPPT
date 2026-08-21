"""CLI entrypoint for chatppt."""

import click
from chatstyle import add_tree_option

from chatppt import __version__


@click.group(name="chatppt")
@click.version_option(__version__, prog_name="chatppt")
@add_tree_option(renderer_options={"root_name": "chatppt"})
def main() -> None:
    """chatppt command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


if __name__ == "__main__":
    main()
