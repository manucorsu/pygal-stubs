from collections.abc import Iterable, Mapping
from typing import Generic, TypeVar

from pygal.graph.graph import Graph as Graph
from pygal.view import (
    HorizontalLogView as HorizontalLogView,
)
from pygal.view import (
    HorizontalView as HorizontalView,
)

_ValueT = TypeVar(
    "_ValueT",
    default=Iterable[object] | Mapping[object, object] | object,
)
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float)

class HorizontalGraph(
    Graph[_ValueT, _XLabelT, _YLabelT], Generic[_ValueT, _XLabelT, _YLabelT]
):
    horizontal: bool
