from pygal.config import SerieConfig
from pygal.util import cached_property as cached_property

class Serie:
    index: int
    values: list[object]
    config: SerieConfig
    metadata: dict[str, object] | None
    def __init__(self, index: int, values: list[object], config: SerieConfig, metadata: dict[str, object] | None = None) -> None: ...
    @cached_property
    def safe_values(self) -> list[object]: ...
