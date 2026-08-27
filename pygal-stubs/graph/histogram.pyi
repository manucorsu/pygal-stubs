from pygal.graph.bar import Bar as Bar
from pygal.graph.dual import Dual as Dual
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    decorate as decorate,
)

class Histogram(Dual, Bar):
    @cached_property
    def xvals(self): ...
    @cached_property
    def yvals(self): ...
    def bar(self, serie, rescale: bool = False) -> None: ...
