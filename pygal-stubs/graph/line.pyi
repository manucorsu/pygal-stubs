from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
    cached_property as cached_property,
    decorate as decorate,
)

class Line(Graph):
    def __init__(self, *args, **kwargs) -> None: ...
    def line(self, serie, rescale: bool = False) -> None: ...
