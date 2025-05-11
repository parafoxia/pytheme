# Edit this file to create a new theme.
# See the comment in the _colorize module for more instructions.

from _colorize import ANSIColors, default_theme, set_theme

syntax = default_theme.syntax.copy_with(
    prompt=ANSIColors.BOLD_BLUE,
)
theme = default_theme.copy_with(syntax=syntax)
set_theme(theme)
