from pygal.graph.bar import Bar as Bar
from pygal.graph.dual import Dual as Dual
from pygal.util import alter as alter, cached_property as cached_property, decorate as decorate

class Histogram(Dual, Bar):
    @cached_property
    def xvals(self): ...
    @cached_property
    def yvals(self): ...
    def bar(self, serie, rescale: bool = False) -> None: ...
