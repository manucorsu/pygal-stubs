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

_T = TypeVar("_T")

class BaseMap(Graph):
    def enumerate_values(self, serie: Serie) -> enumerate[tuple[int, object]]: ...
    def adapt_code(
        self, area_code: _T
    ) -> (
        _T
    ): ...  # this just returns area_code without modifying it or checking it at all so it can be anything
