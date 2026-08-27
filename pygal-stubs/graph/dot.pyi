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
from pygal.util import (
    safe_enumerate as safe_enumerate,
)
from pygal.view import ReverseView as ReverseView
from pygal.view import View as View

class Dot(Graph):
    def dot(self, serie: Serie, r_max: float) -> None: ...
