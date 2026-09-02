from collections.abc import Sequence
from typing import TypeVar

from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    decorate as decorate,
)
from pygal.util import (
    ident as ident,
)
from pygal.util import (
    swap as swap,
)

_ValueT = TypeVar("_ValueT", default=float | None | Sequence[float | None])

class Bar(Graph[_ValueT]):
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
