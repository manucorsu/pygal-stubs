from pygal import colors as colors
from pygal.colors import (
    darken as darken,
)
from pygal.colors import (
    is_foreground_light as is_foreground_light,
)
from pygal.colors import (
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
    label_font_family: str | None
    major_label_font_family: str | None
    value_font_family: str | None
    value_label_font_family: str | None
    tooltip_font_family: str | None
    title_font_family: str | None
    legend_font_family: str | None
    no_data_font_family: str | None
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
    colors: tuple[str, ...]
    value_colors: tuple[str | None, ...]
    ci_colors: tuple[str | None, ...]
    def __init__(self, **kwargs: object) -> None: ...
    def get_colors(self, prefix: str, len_: int) -> tuple[str, ...]: ...
    def to_dict(self) -> dict[str, object]: ...

DefaultStyle = Style

class DarkStyle(Style): ...
class LightStyle(Style): ...
class NeonStyle(DarkStyle): ...
class CleanStyle(Style): ...
class DarkSolarizedStyle(Style): ...
class LightSolarizedStyle(DarkSolarizedStyle): ...
class RedBlueStyle(Style): ...
class LightColorizedStyle(Style): ...
class DarkColorizedStyle(Style): ...
class TurquoiseStyle(Style): ...
class LightGreenStyle(Style): ...
class DarkGreenStyle(Style): ...
class DarkGreenBlueStyle(Style): ...
class BlueStyle(Style): ...
class SolidColorStyle(Style): ...

styles: dict[str, type[Style]]

class ParametricStyleBase(Style):
    def __init__(
        self,
        color: str,
        step: int = 10,
        max_: int | None = None,
        base_style: Style | None = None,
        **kwargs: object,
    ) -> None: ...

class LightenStyle(ParametricStyleBase): ...
class DarkenStyle(ParametricStyleBase): ...
class SaturateStyle(ParametricStyleBase): ...
class DesaturateStyle(ParametricStyleBase): ...
class RotateStyle(ParametricStyleBase): ...

parametric_styles: dict[str, type[ParametricStyleBase]]
