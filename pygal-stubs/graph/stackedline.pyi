from collections.abc import Sequence
from typing import Generic, TypedDict, TypeVar

from pygal.adapters import none_to_zero as none_to_zero
from pygal.graph.line import Line as Line

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_ValueT = TypeVar("_ValueT", default=Sequence[float | None])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class StackedLine(
    Line[_ValueT, _XLabelT, _YLabelT], Generic[_ValueT, _XLabelT, _YLabelT]
): ...
