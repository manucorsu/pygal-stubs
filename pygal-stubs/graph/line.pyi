from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)

class Line(Graph):
    def __init__(self, *args, **kwargs) -> None: ...
    def line(self, serie, rescale: bool = False) -> None: ...
