from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
    cached_property as cached_property,
    decorate as decorate,
    safe_enumerate as safe_enumerate,
)
from pygal.view import ReverseView as ReverseView, View as View

class Dot(Graph):
    def dot(self, serie, r_max) -> None: ...
