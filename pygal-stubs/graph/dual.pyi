from collections.abc import Iterable, Mapping
from typing import Generic, TypeVar

from pygal.graph.graph import Graph as Graph
from pygal.util import compute_scale as compute_scale
from pygal.util import cut as cut

_ValueT = TypeVar(
    "_ValueT",
    default=Iterable[object] | Mapping[object, object] | object,
)

class Dual(Graph[_ValueT], Generic[_ValueT]): ...
