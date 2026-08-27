from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.util import (
    alter as alter,
    decorate as decorate,
    ident as ident,
    swap as swap,
)

class Bar(Graph):
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
