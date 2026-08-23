from .__about__ import *
from _typeshed import Incomplete
from pygal import maps as maps
from pygal.config import Config as Config
from pygal.graph.bar import Bar as Bar
from pygal.graph.box import Box as Box
from pygal.graph.dot import Dot as Dot
from pygal.graph.funnel import Funnel as Funnel
from pygal.graph.gauge import Gauge as Gauge
from pygal.graph.graph import Graph as Graph
from pygal.graph.histogram import Histogram as Histogram
from pygal.graph.horizontalbar import HorizontalBar as HorizontalBar
from pygal.graph.horizontalline import HorizontalLine as HorizontalLine
from pygal.graph.horizontalstackedbar import HorizontalStackedBar as HorizontalStackedBar
from pygal.graph.horizontalstackedline import HorizontalStackedLine as HorizontalStackedLine
from pygal.graph.line import Line as Line
from pygal.graph.map import BaseMap as BaseMap
from pygal.graph.pie import Pie as Pie
from pygal.graph.pyramid import Pyramid as Pyramid, VerticalPyramid as VerticalPyramid
from pygal.graph.radar import Radar as Radar
from pygal.graph.solidgauge import SolidGauge as SolidGauge
from pygal.graph.stackedbar import StackedBar as StackedBar
from pygal.graph.stackedline import StackedLine as StackedLine
from pygal.graph.time import DateLine as DateLine, DateTimeLine as DateTimeLine, TimeDeltaLine as TimeDeltaLine, TimeLine as TimeLine
from pygal.graph.treemap import Treemap as Treemap
from pygal.graph.xy import XY as XY

CHARTS_BY_NAME: Incomplete
module: Incomplete
CHARTS_NAMES: Incomplete
CHARTS: Incomplete

class PluginImportFixer:
    def find_module(self, fullname, path=None): ...
    def load_module(self, name): ...
