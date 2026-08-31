from collections.abc import Callable
from types import FunctionType
from typing import Generic, TypeVar

from pygal import formatters as formatters
from pygal.interpolate import INTERPOLATIONS as INTERPOLATIONS
from pygal.style import DefaultStyle as DefaultStyle
from pygal.style import Style as Style
from typing_extensions import Self

import builtins

CONFIG_ITEMS: list[Key[object, object | None]]
callable = FunctionType
_T = TypeVar("_T", default=object)
_SubtypeT = TypeVar("_SubtypeT", default=None)

class Key(Generic[_T, _SubtypeT]):
    value: _T | tuple[object, ...] | None
    type: builtins.type[_T] | Callable[..., _T]
    doc: str
    category: str
    subdoc: str
    subtype: builtins.type[_SubtypeT] | Callable[[str], _SubtypeT] | None
    name: str
    def __init__(
        self,
        default_value: _T | Callable[..., _T],
        type_: builtins.type[_T] | Callable[..., _T],
        category: str,
        doc: str,
        subdoc: str = "",
        subtype: builtins.type[_SubtypeT] | Callable[[str], _SubtypeT] | None = None,
    ) -> None: ...
    @property
    def is_boolean(self) -> bool: ...
    @property
    def is_numeric(self) -> bool: ...
    @property
    def is_string(self) -> bool: ...
    @property
    def is_dict(self) -> bool: ...
    @property
    def is_list(self) -> bool: ...
    def coerce(self, value: str) -> _T | str: ...

class MetaConfig(type):
    def __new__(
        mcs, classname: str, bases: tuple[type, ...], classdict: dict[str, object]
    ) -> MetaConfig: ...

class BaseConfig(metaclass=MetaConfig):
    def __init__(self, **kwargs: object) -> None: ...
    def __call__(self, **kwargs: object) -> None: ...
    def to_dict(self) -> dict[str, object]: ...
    def copy(self) -> Self: ...

class CommonConfig(BaseConfig):
    stroke: bool
    show_dots: bool
    show_only_major_dots: bool
    dots_size: float
    fill: bool
    stroke_style: dict[str, object] | None
    rounded_bars: int | None
    inner_radius: float
    allow_interruptions: bool
    formatter: Callable[..., str] | None

class Config(CommonConfig):
    style: builtins.type[Style] | Style
    css: list[str]
    classes: list[str]
    defs: list[str]
    title: str | None
    x_title: str | None
    y_title: str | None
    width: int
    height: int
    show_x_guides: bool
    show_y_guides: bool
    show_legend: bool
    legend_at_bottom: bool
    legend_at_bottom_columns: int | None
    legend_box_size: int
    rounded_bars: int | None
    stack_from_top: bool
    spacing: int
    margin: int
    margin_top: int | None
    margin_right: int | None
    margin_bottom: int | None
    margin_left: int | None
    tooltip_border_radius: int
    tooltip_fancy_mode: bool
    inner_radius: float
    half_pie: bool
    reverse_direction: bool
    x_labels: list[str] | None
    x_labels_major: list[str] | None
    x_labels_major_every: int | None
    x_labels_major_count: int | None
    show_x_labels: bool
    show_minor_x_labels: bool
    y_labels: list[float] | None
    y_labels_major: list[str] | None
    y_labels_major_every: int | None
    y_labels_major_count: int | None
    show_minor_y_labels: bool
    show_y_labels: bool
    x_label_rotation: int
    y_label_rotation: int
    missing_value_fill_truncation: str
    x_value_formatter: Callable[..., str]
    value_formatter: Callable[..., str]
    logarithmic: bool
    interpolate: str | None
    interpolation_precision: int
    interpolation_parameters: dict[str, object]
    box_mode: str
    order_min: int | None
    min_scale: int
    max_scale: int
    range: tuple[float, float] | list[float] | None
    secondary_range: tuple[float, float] | list[float] | None
    xrange: tuple[float, float] | list[float] | None
    include_x_axis: bool
    zero: int | float
    no_data_text: str
    print_values: bool
    dynamic_print_values: bool
    print_values_position: str
    print_zeroes: bool
    print_labels: bool
    truncate_legend: int | None
    truncate_label: int | None
    js: list[str]
    disable_xml_declaration: bool
    force_uri_protocol: str | None
    explicit_size: bool
    pretty_print: bool
    strict: bool
    no_prefix: bool
    inverse_y_axis: bool

class SerieConfig(CommonConfig):
    title: str | None
    secondary: bool
