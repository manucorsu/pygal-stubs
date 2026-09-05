from collections.abc import Sequence
from typing import Generic, TypedDict, TypeVar

from pygal.adapters import none_to_zero as none_to_zero
from pygal.adapters import positive as positive
from pygal.graph.line import Line as Line
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    compute_scale as compute_scale,
)
from pygal.util import (
    cut as cut,
)
from pygal.util import (
    deg as deg,
)
from pygal.util import (
    truncate as truncate,
)
from pygal.view import PolarLogView as PolarLogView
from pygal.view import PolarView as PolarView

class _AxisLabelsDict(TypedDict):
    label: str
    value: float

_ValueT = TypeVar("_ValueT", default=Sequence[float | None])
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float | _AxisLabelsDict)

class Radar(
    Line[_ValueT, _XLabelT, _YLabelT], Generic[_ValueT, _XLabelT, _YLabelT]
): ...
