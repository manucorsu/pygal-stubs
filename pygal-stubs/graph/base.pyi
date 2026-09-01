from collections.abc import Callable, Iterable
from typing import TypeAlias
from xml.etree.ElementTree import Element as _StdEtreeElement

from lxml.etree import (
    Element as _LxmlElement,
)
from pygal._compat import is_list_like as is_list_like
from pygal.adapters import (
    decimal_to_float as decimal_to_float,
)
from pygal.adapters import (
    not_zero as not_zero,
)
from pygal.adapters import (
    positive as positive,
)
from pygal.config import Config as Config
from pygal.config import SerieConfig as SerieConfig
from pygal.serie import Serie as Serie
from pygal.state import State as State
from pygal.style import Style
from pygal.svg import Svg as Svg
from pygal.util import compose as compose
from pygal.util import ident as ident
from pygal.view import Box as Box
from pygal.view import Margin as Margin
from pygal.view import View

_RawSeries: TypeAlias = list[tuple[Iterable[object], dict[str, object]]]

class BaseGraph:
    config: Config
    state: State
    uuid: str
    raw_series: _RawSeries

    xml_filters: list[Callable[[object], object]]
    x_label_rotation: float | None
    def __init__(
        self, config: Config | type[Config] | None = None, **kwargs: object
    ) -> None: ...
    zero: float
    def prepare_values(
        self, raw: _RawSeries, offset: float = 0
    ) -> list[Serie] | None: ...
    x_labels: (
        Iterable[str] | None
    )  # Why not Sequence? This example in the docs: (https://www.pygal.org/en/stable/documentation/types/line.html) feeds it a `map()` returned value
    y_labels: Iterable[str] | None
    style: Style
    series: list[Serie]
    secondary_series: list[Serie]
    horizontal: bool
    svg: Svg
    nodes: dict[str, _LxmlElement | _StdEtreeElement]
    margin_box: Margin
    view: View | None
    interpolate: bool | None
    def setup(self, **kwargs: object) -> None: ...
    def teardown(self) -> None: ...
