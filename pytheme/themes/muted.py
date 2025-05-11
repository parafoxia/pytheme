# This theme is the example in the _colorize module.
# Created by Łukasz Langa.

from _colorize import ANSIColors, Syntax, default_theme, set_theme

theme_with_dim_operators = default_theme.copy_with(
    syntax=Syntax(op=ANSIColors.INTENSE_BLACK),
)
set_theme(theme_with_dim_operators)
del set_theme, default_theme, Syntax, ANSIColors, theme_with_dim_operators
