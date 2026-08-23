from _typeshed import Incomplete
from pygal.util import cached_property as cached_property

class Serie:
    index: Incomplete
    values: Incomplete
    config: Incomplete
    metadata: Incomplete
    def __init__(self, index, values, config, metadata=None) -> None: ...
    @cached_property
    def safe_values(self): ...
