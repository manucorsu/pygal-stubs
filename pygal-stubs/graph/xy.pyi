from collections.abc import Sequence
from typing import Generic, TypedDict, TypeVar

from pygal import Config
from pygal.graph.dual import Dual as Dual
from pygal.graph.line import Line as Line
from pygal.style import Style
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    compose as compose,
)
from pygal.util import (
    ident as ident,
)

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_XYValueT = TypeVar("_XYValueT", default=Sequence[tuple[float | None, float | None]])
_XLabelT = TypeVar("_XLabelT", default=str | float | _AxisLabelsDict)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class XY(
    Line[_XYValueT, _XLabelT, _YLabelT],
    Dual[_XYValueT, _XLabelT, _YLabelT],
    Generic[_XYValueT, _XLabelT, _YLabelT],
):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        show_legend: bool | None = None,
        human_readable: bool | None = None,
        fill: bool | None = None,
        **kwargs: object,
    ) -> None: ...
    @cached_property
    def xvals(self) -> list[float]: ...
    @cached_property
    def yvals(self) -> list[float]: ...
