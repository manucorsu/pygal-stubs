from _typeshed import Incomplete
from pygal.util import float_format as float_format

class Formatter: ...

class HumanReadable(Formatter):
    ORDERS: str
    none_char: Incomplete
    def __init__(self, none_char: str = "∅") -> None: ...
    def __call__(self, val): ...

class Significant(Formatter):
    format: Incomplete
    def __init__(self, precision: int = 10) -> None: ...
    def __call__(self, val): ...

class Integer(Formatter):
    def __call__(self, val): ...

class Raw(Formatter):
    def __call__(self, val): ...

class IsoDateTime(Formatter):
    def __call__(self, val): ...

class Default(Significant, IsoDateTime, Raw):
    def __call__(self, val): ...

human_readable: Incomplete
significant: Incomplete
integer: Incomplete
raw: Incomplete
default: Incomplete
