# pytheme

A theme manager for Python 3.14.

This is built on top of the `_colorize` standard library module, and so
is inherently unstable as a result. It simply exists to provide an
easier mechanism for applying themes, until a more official solution is
decided upon.

## Installation

Unfortunately pytheme isn't on PyPI yet, and won't be until I'm able to
submit a [PEP 541](https://peps.python.org/pep-0541/) request, though
for now, you can clone and install it manually:

```sh
git clone https://github.com/parafoxia/pytheme
pip install uv
uv build
pip install dist/pytheme-0.1.0-py3-none-any.whl
```

The version number won't change until it's on PyPI.

## Usage

It's important to note that pytheme will only operate on the interpreter
it's called from.

### Creating themes

To start creating a new theme, use:

```sh
python -m pytheme create
```

This will generate a file in your current working directory that you can
use to create your theme!

For instructions on creating a theme, see the [`_colorize`](https://github.com/python/cpython/blob/main/Lib/_colorize.py)
module, or [this YouTube video](https://youtu.be/28oh6h89h_g).

### Installing themes

You can either install a theme you created yourself, or one that ships
with pytheme.

To install a theme, use:

```sh
python -m pytheme install [theme]
```

If `[theme]` ends in ".py", pytheme will look for a file of that name,
otherwise it will search the themes shipped with pytheme.

⚠️ This will overwrite any `sitecustomize.py` file you have in place for
the interpreter, so be careful! Future versions will be capable of just
adding and removing the theme information.

### Uninstalling themes

If you wish to uninstall your active theme and revert to the default,
use:

```sh
python -m pytheme uninstall
```

⚠️ This will remove any `sitecustomize.py` file you have in place for
the interpreter, so be careful! Future versions will be capable of just
adding and removing the theme information.

### Listing available themes

To see a list of all themes that ship with pytheme, use:

```sh
python -m pytheme list
```

Currently, this does not show which theme is currently active, but it
will in future versions.

## Adding themes to pytheme

Contributions are very much welcome! If you have a theme you're proud of
and want to see shipped with pytheme, open a PR!

Please do include some author information in the file comments if you
wish.

## License

The pytheme module for Python is licensed under the [BSD 3-Clause License](https://github.com/parafoxia/pytheme/blob/main/LICENSE).
