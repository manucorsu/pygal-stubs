from _typeshed import Incomplete
from pygal.util import template as template

class HTML:
    def __getattribute__(self, attr): ...

class Table:
    chart: Incomplete
    def __init__(self, chart) -> None: ...
    def render(self, total: bool = False, transpose: bool = False, style: bool = False): ...
