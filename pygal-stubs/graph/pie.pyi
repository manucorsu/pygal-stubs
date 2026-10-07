from collections.abc import Callable, Sequence

from pygal import Config
from pygal.adapters import none_to_zero as none_to_zero
from pygal.adapters import positive as positive
from pygal.graph.graph import Graph as Graph
from pygal.serie import Serie
from pygal.style import Style
from pygal.util import alter as alter
from pygal.util import decorate as decorate
from typing_extensions import Self, override

class Pie(Graph[float | Sequence[float]]):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        pretty_print: bool | None = None,
        inner_radius: float | None = None,
        half_pie: bool | None = None,
        print_values: bool | None = None,
        value_formatter: Callable[[float], str] | None = None,
        **kwargs: object,
    ) -> None: ...
    def slice(self, serie: Serie, start_angle: float, total: float) -> float: ...
    @override
    def add(
        self,
        title: str,
        values: float | Sequence[float] | None,
        *,
        inner_radius: float | None = None,
        **kwargs: object,
    ) -> Self: ...
