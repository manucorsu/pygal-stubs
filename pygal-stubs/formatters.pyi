from typing import Literal, overload, Protocol
from typing_extensions import LiteralString
from pygal.util import float_format as float_format

class _SupportsIsoformat(Protocol):
    def isoformat(self) -> str: ...

class Formatter: ...

class HumanReadable(Formatter):
    ORDERS: LiteralString
    none_char: str
    def __init__(self, none_char: str = "∅") -> None: ...
    def __call__(self, val: float | None) -> str: ...

class Significant(Formatter):
    format: str
    def __init__(self, precision: int = 10) -> None: ...
    @overload
    def __call__(self, val: None) -> Literal[""]: ...
    @overload
    def __call__(self, val: float) -> str: ...

class Integer(Formatter):
    @overload
    def __call__(self, val: None) -> Literal[""]: ...
    @overload
    def __call__(self, val: float) -> str: ...

class Raw(Formatter):
    @overload
    def __call__(self, val: None) -> Literal[""]: ...
    @overload
    def __call__(self, val: object) -> str: ...

class IsoDateTime(Formatter):
    @overload
    def __call__(self, val: None) -> Literal[""]: ...
    @overload
    def __call__(self, val: _SupportsIsoformat) -> str: ...

class Default(Significant, IsoDateTime, Raw):
    @overload
    def __call__(self, val: None) -> Literal[""]: ...
    @overload
    def __call__(self, val: object) -> str: ...

human_readable: HumanReadable
significant: Significant
integer: Integer
raw: Raw
default: Default
