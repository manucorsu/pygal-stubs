from collections.abc import Callable, Iterable, Sequence
from typing import Generic, TypedDict, TypeVar

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

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_ValueT = TypeVar("_ValueT", default=Sequence[float | None])
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
        **kwargs: object,
    ) -> None: ...
    def line(self, serie: Serie, rescale: bool = False) -> None: ...
