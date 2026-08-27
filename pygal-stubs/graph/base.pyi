from _typeshed import Incomplete
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
from pygal.svg import Svg as Svg
from pygal.util import compose as compose
from pygal.util import ident as ident
from pygal.view import Box as Box
from pygal.view import Margin as Margin

class BaseGraph:
    config: Incomplete
    state: Incomplete
    uuid: Incomplete
    raw_series: Incomplete
    xml_filters: Incomplete
    def __init__(self, config=None, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __getattribute__(self, name): ...
    zero: int
    def prepare_values(self, raw, offset: int = 0): ...
    x_labels: Incomplete
    y_labels: Incomplete
    style: Incomplete
    series: Incomplete
    secondary_series: Incomplete
    horizontal: Incomplete
    svg: Incomplete
    nodes: Incomplete
    margin_box: Incomplete
    view: Incomplete
    interpolate: Incomplete
    def setup(self, **kwargs): ...
    def teardown(self) -> None: ...
