from collections.abc import Sequence
from types import ModuleType

from pygal import maps as maps
from pygal import style as style
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
from pygal.graph.horizontalstackedbar import (
    HorizontalStackedBar as HorizontalStackedBar,
)
from pygal.graph.horizontalstackedline import (
    HorizontalStackedLine as HorizontalStackedLine,
)
from pygal.graph.line import Line as Line
from pygal.graph.map import BaseMap as BaseMap
from pygal.graph.pie import Pie as Pie
from pygal.graph.pyramid import Pyramid as Pyramid
from pygal.graph.pyramid import VerticalPyramid as VerticalPyramid
from pygal.graph.radar import Radar as Radar
from pygal.graph.solidgauge import SolidGauge as SolidGauge
from pygal.graph.stackedbar import StackedBar as StackedBar
from pygal.graph.stackedline import StackedLine as StackedLine
from pygal.graph.time import (
    DateLine as DateLine,
)
from pygal.graph.time import (
    DateTimeLine as DateTimeLine,
)
from pygal.graph.time import (
    TimeDeltaLine as TimeDeltaLine,
)
from pygal.graph.time import (
    TimeLine as TimeLine,
)
from pygal.graph.treemap import Treemap as Treemap
from pygal.graph.xy import XY as XY

from .__about__ import (
    __author__ as __author__,
)
from .__about__ import (
    __copyright__ as __copyright__,
)
from .__about__ import (
    __email__ as __email__,
)
from .__about__ import (
    __license__ as __license__,
)
from .__about__ import (
    __summary__ as __summary__,
)
from .__about__ import (
    __title__ as __title__,
)
from .__about__ import (
    __uri__ as __uri__,
)
from .__about__ import (
    __version__ as __version__,
)

CHARTS_BY_NAME: dict[str, type[Graph]]
CHARTS_NAMES: list[str]
CHARTS: list[type[Graph]]

class PluginImportFixer:
    def find_module(
        self, fullname: str, path: Sequence[str] | None = None
    ) -> PluginImportFixer | None: ...
    def load_module(self, name: str) -> ModuleType: ...
