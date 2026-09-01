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

class HorizontalGraph(Graph[_ValueT], Generic[_ValueT]):
    horizontal: bool
    def __init__(self, *args: object, **kwargs: object) -> None: ...
