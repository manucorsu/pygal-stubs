from collections.abc import Callable, Iterable, Sequence
from types import EllipsisType
from typing import Generic, Literal, TypedDict, TypeVar

from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.style import Style
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)
from typing_extensions import LiteralString, Self, override

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

class _ValueNodePair(TypedDict):
    value: float
    node: dict[str, object]

_ValueT = TypeVar("_ValueT", default=Sequence[float | None | _ValueNodePair])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class Line(Graph[_ValueT, _XLabelT, _YLabelT], Generic[_ValueT, _XLabelT, _YLabelT]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        x_title: str | None = None,
        y_title: str | None = None,
        style: Style | type[Style] | None = None,
        pretty_print: bool | None = None,
        x_labels: Iterable[_XLabelT] | None = None,
        x_labels_major: Iterable[str] | None = None,
        x_labels_major_every: int | None = None,
        x_labels_major_count: int | None = None,
        show_minor_x_labels: bool | None = None,
        x_label_rotation: float | None = None,
        show_x_labels: bool | None = None,
        y_labels: Iterable[_YLabelT] | None = None,
        y_labels_major: Iterable[str] | None = None,
        y_labels_major_every: int | None = None,
        y_labels_major_count: int | None = None,
        show_y_labels: bool | None = None,
        show_minor_y_labels: bool | None = None,
        y_label_rotation: float | None = None,
        truncate_label: int | None = None,
        range: tuple[float, float] | list[float] | None = None,
        fill: bool | None = None,
        x_value_formatter: Callable[..., str] | None = None,
        show_legend: bool | None = None,
        legend_at_bottom: bool | None = None,
        legend_at_bottom_columns: int | None = None,
        legend_box_size: int | None = None,
        truncate_legend: int | None = None,
        include_x_axis: bool | None = None,
        inverse_y_axis: bool | None = None,
        xrange: tuple[float, float] | list[float] | None = None,
        secondary_range: tuple[float, float] | list[float] | None = None,
        logarithmic: bool | None = None,
        min_scale: int | None = None,
        max_scale: int | None = None,
        order_min: int | None = None,
        interpolate: (
            Literal["quadratic", "qubic", "hermite", "lagrange", "trigonometric"] | None
        ) = None,
        interpolation_precision: int | None = None,
        interpolation_parameters: dict[str, object] | None = None,
        value_formatter: Callable[..., str] | None = None,
        tooltip_border_radius: int | None = None,
        stroke: bool | None = None,
        zero: float | None = None,
        show_only_major_dots: bool | None = None,
        dots_size: int | None = None,
        stroke_style: dict[str, object] | None = None,
        show_x_guides: bool | None = None,
        show_y_guides: bool | None = None,
        css: Sequence[str] | tuple[EllipsisType, str] | None = None,
        classes: Sequence[str] | tuple[EllipsisType, str] | None = None,
        **kwargs: object,
    ) -> None: ...
    def line(self, serie: Serie, rescale: bool = False) -> None: ...
    @override
    def add(
        self,
        title: str,
        values: _ValueT,
        *,
        secondary: bool | None = None,
        show_dots: bool | None = None,
        show_only_major_dots: bool | None = None,
        dots_size: int | None = None,
        stroke_style: dict[str, object] | None = None,
        allow_interruptions: bool | None = None,
        **kwargs: object,
    ) -> Self: ...
    @override
    def render_sparkline(
        self,
        *,
        width: int | None = None,
        height: int | None = None,
        show_dots: bool | None = None,
        show_x_labels: bool | None = None,
        show_y_labels: bool | None = None,
        **kwargs: object,
    ) -> str: ...
    @override
    def render_sparktext(
        self,
        relative_to: float | None = None,
    ) -> Literal[""] | LiteralString: ...
