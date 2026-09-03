from collections.abc import Iterable, Mapping
from typing import Generic, TypeVar

from pygal.graph.graph import Graph as Graph
from pygal.util import compute_scale as compute_scale
from pygal.util import cut as cut

_ValueT = TypeVar(
    "_ValueT",
    default=Iterable[object] | Mapping[object, object] | object,
)
_XLabelT = TypeVar("_XLabelT", default=str)

class Dual(Graph[_ValueT, _XLabelT], Generic[_ValueT, _XLabelT]): ...
