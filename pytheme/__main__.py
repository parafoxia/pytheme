# BSD 3-Clause License
#
# Copyright (c) 2025, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import sys
from pathlib import Path

import click

from .themes import _template


def _get_sitecustomize_path() -> Path:
    if sys.prefix != sys.base_prefix:
        # This is a virtual environment.
        import site

        return Path(site.getsitepackages(prefixes=[sys.prefix])[0]) / "sitecustomize.py"

    import os

    return Path(os.__file__).parent / "sitecustomize.py"


SITECUSTOMIZE_PATH = _get_sitecustomize_path()


@click.group()
@click.version_option()
def pytheme() -> None:
    pass


@pytheme.command(help="Generate a new file from which you can create a new theme.")
def create() -> None:
    theme = Path(_template.__file__)
    theme.copy_into(Path()).rename("new_theme.py")


@pytheme.command(help="Install a theme into the current interpreter.")
@click.argument("theme")
def install(theme: str) -> None:
    theme_path = (
        Path(theme)
        if theme.endswith(".py")
        else Path(__file__).parent / "themes" / f"{theme}.py"
    )

    if not theme_path.exists():
        click.echo(f"Theme {theme!r} does not exist.")
        return

    if SITECUSTOMIZE_PATH.exists():
        ans = input(
            f"A sitecustomize.py file already exists for this interpreter. Overwrite? [y/N] ",
        )
        if not ans.lower().startswith("y"):
            click.echo("No changed applied.")
            return

    theme_path.copy(SITECUSTOMIZE_PATH)
    click.echo(f"Theme {theme!r} installed to '{SITECUSTOMIZE_PATH}'.")


@pytheme.command(
    help=(
        "Uninstall the currently installed theme from the interpreter. "
        "This will remove the entire sitecustomize.py file, so be careful!."
    ),
)
def uninstall() -> None:
    if not SITECUSTOMIZE_PATH.exists():
        click.echo("No sitecustomize.py file exists for this interpreter.")
        return

    ans = input("This will remove the entire sitecustomize.py file. Continue? [y/N] ")
    if not ans.lower().startswith("y"):
        click.echo("No changes applied.")
        return

    SITECUSTOMIZE_PATH.unlink()
    click.echo("Theme uninstalled.")


if __name__ == "__main__":
    pytheme()
