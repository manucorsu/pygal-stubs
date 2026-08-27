from pygal.etree import etree as etree
from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
)
from pygal.util import (
    cached_property as cached_property,
)
from pygal.util import (
    cut as cut,
)
from pygal.util import (
    decorate as decorate,
)

class BaseMap(Graph):
    def enumerate_values(self, serie): ...
    def adapt_code(self, area_code): ...
