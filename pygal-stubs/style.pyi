from _typeshed import Incomplete
from pygal import colors as colors
from pygal.colors import (
    darken as darken,
    is_foreground_light as is_foreground_light,
    lighten as lighten,
)

class Style:
    plot_background: str
    background: str
    value_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    font_family: str
    label_font_family: Incomplete
    major_label_font_family: Incomplete
    value_font_family: Incomplete
    value_label_font_family: Incomplete
    tooltip_font_family: Incomplete
    title_font_family: Incomplete
    legend_font_family: Incomplete
    no_data_font_family: Incomplete
    label_font_size: int
    major_label_font_size: int
    value_font_size: int
    value_label_font_size: int
    tooltip_font_size: int
    title_font_size: int
    legend_font_size: int
    no_data_font_size: int
    guide_stroke_dasharray: str
    major_guide_stroke_dasharray: str
    guide_stroke_color: str
    major_guide_stroke_color: str
    opacity: str
    opacity_hover: str
    stroke_opacity: str
    stroke_width: str
    stroke_opacity_hover: str
    stroke_width_hover: str
    dot_opacity: str
    transition: str
    colors: Incomplete
    value_colors: Incomplete
    ci_colors: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def get_colors(self, prefix, len_): ...
    def to_dict(self): ...

DefaultStyle = Style

class DarkStyle(Style):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class LightStyle(Style):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    colors: Incomplete

class NeonStyle(DarkStyle):
    opacity: str
    opacity_hover: str
    transition: str

class CleanStyle(Style):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    colors: Incomplete

class DarkSolarizedStyle(Style):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class LightSolarizedStyle(DarkSolarizedStyle):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str

class RedBlueStyle(Style):
    background: Incomplete
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    colors: Incomplete

class LightColorizedStyle(Style):
    background: str
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class DarkColorizedStyle(Style):
    background: Incomplete
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class TurquoiseStyle(Style):
    background: Incomplete
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class LightGreenStyle(Style):
    background: Incomplete
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class DarkGreenStyle(Style):
    background: Incomplete
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class DarkGreenBlueStyle(Style):
    background: str
    plot_background: Incomplete
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class BlueStyle(Style):
    background: Incomplete
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

class SolidColorStyle(Style):
    background: str
    plot_background: str
    foreground: str
    foreground_strong: str
    foreground_subtle: str
    opacity: str
    opacity_hover: str
    transition: str
    colors: Incomplete

styles: Incomplete

class ParametricStyleBase(Style):
    colors: Incomplete
    def __init__(
        self, color, step: int = 10, max_=None, base_style=None, **kwargs
    ) -> None: ...

class LightenStyle(ParametricStyleBase): ...
class DarkenStyle(ParametricStyleBase): ...
class SaturateStyle(ParametricStyleBase): ...
class DesaturateStyle(ParametricStyleBase): ...
class RotateStyle(ParametricStyleBase): ...

parametric_styles: Incomplete
