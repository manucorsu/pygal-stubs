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

class Bar(Graph):
    def bar(self, serie: Serie, rescale: bool = False) -> None: ...
