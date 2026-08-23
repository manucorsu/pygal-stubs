from pygal.etree import etree as etree
from pygal.graph.graph import Graph as Graph
from pygal.util import (
    alter as alter,
    cached_property as cached_property,
    cut as cut,
    decorate as decorate,
)

class BaseMap(Graph):
    def enumerate_values(self, serie): ...
    def adapt_code(self, area_code): ...
