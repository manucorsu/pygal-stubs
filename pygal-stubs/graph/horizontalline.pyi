from collections.abc import Sequence
from typing import TypedDict, TypeVar

from pygal.graph.horizontal import HorizontalGraph as HorizontalGraph
from pygal.graph.line import Line as Line

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_ValueT = TypeVar("_ValueT", default=Sequence[float | None])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class HorizontalLine(
    HorizontalGraph[_ValueT, _XLabelT, _YLabelT],
    Line[_ValueT, _XLabelT, _YLabelT],
): ...
