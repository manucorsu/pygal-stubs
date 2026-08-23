from pygal.graph.dual import Dual as Dual
from pygal.graph.line import Line as Line
from pygal.util import cached_property as cached_property, compose as compose, ident as ident

class XY(Line, Dual):
    @cached_property
    def xvals(self): ...
    @cached_property
    def yvals(self): ...
