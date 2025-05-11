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


@click.group()
@click.version_option()
def pytheme():
    pass


@pytheme.command()
def create():
    theme = Path(_template.__file__)
    theme.copy_into(Path()).rename("new_theme.py")


@pytheme.command()
@click.argument("theme")
def install(theme: str):
    theme_path = (
        Path(theme)
        if theme.endswith(".py")
        else Path(__file__).parent / "themes" / f"{theme}.py"
    )

    if not theme_path.exists():
        click.echo(f"Theme {theme!r} does not exist.")
        return

    if sys.prefix == sys.base_prefix:
        # Not a virtual environment.
        import os

        install_path = Path(os.__file__).parent / "sitecustomize.py"
    else:
        # Virtual environment.
        import site

        install_path = (
            Path(site.getsitepackages(prefixes=[sys.prefix])[0]) / "sitecustomize.py"
        )

    if install_path.exists():
        ans = input(
            f"A sitecustomize.py file already exists for this interpreter. Overwrite? [y/N] ",
        )
        if not ans.lower().startswith("y"):
            click.echo("Theme not applied.")
            return

    theme_path.copy(install_path)
    click.echo(f"Theme {theme!r} installed to '{install_path}'.")


if __name__ == "__main__":
    pytheme()
