from _typeshed import Incomplete
from pygal import __version__ as __version__
from pygal.etree import etree as etree
from pygal.util import (
    coord_abs_project as coord_abs_project,
    coord_diff as coord_diff,
    coord_dual as coord_dual,
    coord_format as coord_format,
    coord_project as coord_project,
    minify_css as minify_css,
    template as template,
)

nearly_2pi: Incomplete

class Svg:
    ns: str
    xlink_ns: str
    graph: Incomplete
    id: Incomplete
    processing_instructions: Incomplete
    root: Incomplete
    defs: Incomplete
    title: Incomplete
    def __init__(self, graph) -> None: ...
    def add_styles(self) -> None: ...
    def add_scripts(self): ...
    def node(self, parent=None, tag: str = "g", attrib=None, **extras): ...
    def transposable_node(self, parent=None, tag: str = "g", attrib=None, **extras): ...
    def serie(self, serie): ...
    def line(self, node, coords, close: bool = False, **kwargs): ...
    def slice(
        self,
        serie_node,
        node,
        radius,
        small_radius,
        angle,
        start_angle,
        center,
        val,
        i,
        metadata,
    ): ...
    def gauge_background(
        self,
        serie_node,
        start_angle,
        center,
        radius,
        small_radius,
        end_angle,
        half_pie,
        max_value,
    ) -> None: ...
    def solid_gauge(
        self,
        serie_node,
        node,
        radius,
        small_radius,
        angle,
        start_angle,
        center,
        val,
        i,
        metadata,
        half_pie,
        end_angle,
        max_value,
    ) -> None: ...
    def confidence_interval(self, node, x, low, high, width: int = 7): ...
    def pre_render(self) -> None: ...
    def draw_no_data(self) -> None: ...
    def render(self, is_unicode: bool = False, pretty_print: bool = False): ...
    def get_strokes(self): ...
