from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
    decorate as decorate,
    ident as ident,
    swap as swap,
)

class Bar(Graph):
    def bar(self, serie, rescale: bool = False) -> None: ...
