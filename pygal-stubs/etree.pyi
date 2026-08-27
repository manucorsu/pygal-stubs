from typing import Any
from typing_extensions import override

class Etree:
    lxml: bool
    def __init__(self) -> None: ...
    @override
    def __getattribute__(
        self, attr: str
    ) -> Any: ...  # pyright: ignore[reportExplicitAny]
    def to_lxml(self) -> None: ...
    def to_etree(self) -> None: ...

etree: Etree
