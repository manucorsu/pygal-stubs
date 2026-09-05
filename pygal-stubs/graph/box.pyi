from typing import Literal

from pygal import Config
from pygal.graph.graph import Graph as Graph
from pygal.style import Style
from pygal.util import alter as alter
from pygal.util import decorate as decorate

class Box(Graph):
    def __init__(
        self,
        config: Config | type[Config] | None = None,
        *,
        title: str | None = None,
        style: Style | type[Style] | None = None,
        pretty_print: bool | None = None,
        box_mode: (
            Literal[
                "extremes",
                "1.5IQR",
                "tukey",
                "stdev",
                "pstdev",
            ]
            | None
        ) = None,
        **kwargs: object,
    ) -> None: ...
