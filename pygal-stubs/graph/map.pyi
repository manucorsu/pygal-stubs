from collections.abc import Iterable, Iterator
from typing import TypeVar

from pygal.etree import etree as etree
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    cut as cut,
)
from pygal.util import (
    decorate as decorate,
)

_AreaCodeT = TypeVar("_AreaCodeT")
_ValueT = TypeVar(
    "_ValueT",
    default=Iterable[float]
    | dict[str, float]
    | Iterable[tuple[str, float]]
    | float
    | Iterable[str]
    | None,
)

class BaseMap(Graph[_ValueT]):
    def enumerate_values(
        self, serie: Serie
    ) -> Iterator[tuple[int, tuple[object, object]]]: ...
    def adapt_code(
        self, area_code: _AreaCodeT
    ) -> (
        _AreaCodeT
    ): ...  # this just returns area_code without modifying it or checking it at all so it can be anything
