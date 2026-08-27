from collections.abc import Sequence
from typing import Literal, overload
from pygal import Graph, __version__ as __version__
from pygal.etree import etree as etree
from pygal.serie import Serie
from pygal.util import (
    coord_abs_project as coord_abs_project,
    coord_diff as coord_diff,
    coord_dual as coord_dual,
    coord_format as coord_format,
    coord_project as coord_project,
    minify_css as minify_css,
    template as template,
)
from xml.etree.ElementTree import Element as _StdEtreeElement
from lxml.etree import (
    Element as _LxmlElement,
    _ProcessingInstruction as _LxmlProcessingInstruction,
)

# see Svg.processing_instructions to see why we import a private
# type. It was that or leaving it as list[object]. If you have a
# better suggestion please submit a PR.

nearly_2pi: float

class Svg:
    ns: str
    xlink_ns: str
    graph: Graph
    id: str
    processing_instructions: list[_StdEtreeElement | _LxmlProcessingInstruction]
    root: _StdEtreeElement | _LxmlElement
    defs: _StdEtreeElement | _LxmlElement
    title: _StdEtreeElement | _LxmlElement
    def __init__(self, graph: Graph) -> None: ...
    def add_styles(self) -> None: ...
    def add_scripts(self) -> None: ...
    def node(
        self,
        parent: _StdEtreeElement | _LxmlElement | None = None,
        tag: str = "g",
        attrib: dict[str, object] | None = None,
        **extras: object,
    ) -> _StdEtreeElement | _LxmlElement: ...
    def transposable_node(
        self,
        parent: _StdEtreeElement | _LxmlElement | None = None,
        tag: str = "g",
        attrib: dict[str, object] | None = None,
        **extras: object,
    ) -> _StdEtreeElement | _LxmlElement: ...
    def serie(self, serie: Serie) -> dict[str, _StdEtreeElement | _LxmlElement]: ...
    def line(
        self,
        node: _StdEtreeElement | _LxmlElement,
        coords: Sequence[Sequence[float]],
        close: bool = False,
        **kwargs: object,
    ) -> _StdEtreeElement | _LxmlElement: ...
    def slice(
        self,
        serie_node: _StdEtreeElement | _LxmlElement,
        node: _StdEtreeElement | _LxmlElement,
        radius: float,
        small_radius: float,
        angle: float,
        start_angle: float,
        center: tuple[float, float],
        val: float,
        i: int,
        metadata: dict[str, object],
    ) -> _StdEtreeElement | _LxmlElement | None: ...
    def gauge_background(
        self,
        serie_node: _StdEtreeElement | _LxmlElement,
        start_angle: float,
        center: tuple[float, float],
        radius: float,
        small_radius: float,
        end_angle: float,
        half_pie: bool,
        max_value: float,
    ) -> None: ...
    def solid_gauge(
        self,
        serie_node: _StdEtreeElement | _LxmlElement,
        node: _StdEtreeElement | _LxmlElement,
        radius: float,
        small_radius: float,
        angle: float,
        start_angle: float,
        center: tuple[float, float],
        val: float,
        i: int,
        metadata: dict[str, object],
        half_pie: bool,
        end_angle: float,
        max_value: float,
    ) -> None: ...
    def confidence_interval(
        self,
        node: _StdEtreeElement | _LxmlElement,
        x: float,
        low: float,
        high: float,
        width: int = 7,
    ) -> _StdEtreeElement | _LxmlElement: ...
    def pre_render(self) -> None: ...
    def draw_no_data(self) -> None: ...
    @overload
    def render(
        self, is_unicode: Literal[False] = False, pretty_print: bool = False
    ) -> str | bytes: ...
    @overload
    def render(self, is_unicode: Literal[True], pretty_print: bool = False) -> str: ...
    def get_strokes(self) -> str: ...
