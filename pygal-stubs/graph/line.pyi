from collections.abc import Sequence

from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)

class Line(Graph[Sequence[float | None]]):
    def line(self, serie: Serie, rescale: bool = False) -> None: ...
