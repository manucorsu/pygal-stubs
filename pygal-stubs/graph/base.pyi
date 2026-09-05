from collections.abc import Callable, Iterable
from typing import Generic, Literal, TypeAlias, TypeVar
from xml.etree.ElementTree import Element as _StdEtreeElement

from lxml.etree import (
    Element as _LxmlElement,
)
from pygal._compat import is_list_like as is_list_like
from pygal.adapters import (
    decimal_to_float as decimal_to_float,
)
from pygal.adapters import (
    not_zero as not_zero,
)
from pygal.adapters import (
    positive as positive,
)
from pygal.config import Config as Config
from pygal.config import SerieConfig as SerieConfig
from pygal.serie import Serie as Serie
from pygal.state import State as State
from pygal.style import Style
from pygal.svg import Svg as Svg
from pygal.util import compose as compose
from pygal.util import ident as ident
from pygal.view import Box as Box
from pygal.view import Margin as Margin
from pygal.view import View

_RawSeries: TypeAlias = list[tuple[Iterable[object], dict[str, object]]]
_XLabelT = TypeVar("_XLabelT", default=str)

class BaseGraph(Generic[_XLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        **kwargs: object,
    ) -> None: ...
    def prepare_values(
        self, raw: _RawSeries, offset: float = 0
    ) -> list[Serie] | None: ...

    # from BaseGraph
    zero: float
    x_label_rotation: float | None
    config: Config
    state: State
    uuid: str
    raw_series: _RawSeries
    xml_filters: list[Callable[[object], object]]
    style: Style
    series: list[Serie]
    secondary_series: list[Serie]
    horizontal: bool
    svg: Svg
    nodes: dict[str, _LxmlElement | _StdEtreeElement]
    margin_box: Margin
    view: View | None
    interpolate: (
        Literal["quadratic", "qubic", "hermite", "lagrange", "trigonometric"] | None
    )

    # from CommonConfig
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

    # from Config (excluding duplicates)
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
    stack_from_top: bool
    spacing: int
    margin: int
    margin_top: int | None
    margin_right: int | None
    margin_bottom: int | None
    margin_left: int | None
    tooltip_border_radius: int
    tooltip_fancy_mode: bool
    half_pie: bool
    reverse_direction: bool
    # (labels are declared as list in Config,
    #  but then multiple docs examples pass
    #  map which is incompatible with Sequence
    x_labels: Iterable[_XLabelT] | None
    x_labels_major: Iterable[str] | None
    x_labels_major_every: int | None
    x_labels_major_count: int | None
    show_x_labels: bool
    show_minor_x_labels: bool
    y_labels: Iterable[float] | None
    y_labels_major: Iterable[str] | None
    y_labels_major_every: int | None
    y_labels_major_count: int | None
    show_minor_y_labels: bool
    show_y_labels: bool
    y_label_rotation: int
    missing_value_fill_truncation: str
    x_value_formatter: Callable[..., str]
    value_formatter: Callable[..., str]
    logarithmic: bool
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

    def setup(self, **kwargs: object) -> None: ...
    def teardown(self) -> None: ...
