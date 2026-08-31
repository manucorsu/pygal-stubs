from pygal import Graph
from pygal.util import template as template
from typing_extensions import override

class HTML:
    @override
    def __getattribute__(self, attr: str) -> object: ...

class Table:
    chart: Graph
    def __init__(self, chart: Graph) -> None: ...
    def render(
        self, total: bool = False, transpose: bool = False, style: bool = False
    ) -> str: ...
