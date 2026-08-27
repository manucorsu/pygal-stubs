from pygal.graph.graph import Graph as Graph
from pygal.view import (
    HorizontalLogView as HorizontalLogView,
)
from pygal.view import (
    HorizontalView as HorizontalView,
)

class HorizontalGraph(Graph):
    horizontal: bool
    def __init__(self, *args, **kwargs) -> None: ...
