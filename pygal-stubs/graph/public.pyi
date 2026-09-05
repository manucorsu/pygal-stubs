from collections.abc import Callable, Iterable, Mapping
from os import PathLike
from typing import Any, Generic, Literal, TypeAlias, TypeVar, overload
from xml.etree.ElementTree import Element as _StdEtreeElement

import flask
from django.http import HttpResponse as _DjangoHttpResponse
from lxml.etree import (
    Element as _LxmlElement,
)
from pygal._compat import is_list_like as is_list_like
from pygal.graph.base import BaseGraph as BaseGraph
from pyquery import (  # type: ignore[import-untyped] # pyright: ignore[reportMissingTypeStubs]
    PyQuery,
)
from typing_extensions import LiteralString, Self

_FilePath: TypeAlias = (
    int | str | bytes | PathLike[str] | PathLike[bytes]
)  # anything open()'s file parameter will take

_ValueT = TypeVar(
    "_ValueT", default=Iterable[object] | Mapping[object, object] | object
)
_XLabelT = TypeVar("_XLabelT", default=str)
_YLabelT = TypeVar("_YLabelT", default=str | float)

class PublicApi(BaseGraph[_XLabelT, _YLabelT], Generic[_ValueT, _XLabelT, _YLabelT]):
    def add(
        self,
        title: str,
        values: _ValueT,
        **kwargs: Any,  # pyright: ignore[reportExplicitAny, reportAny]
    ) -> Self: ...
    def __call__(self, *args: object, **kwargs: object) -> Self: ...
    def add_xml_filter(
        self,
        callback: Callable[
            [_StdEtreeElement | _LxmlElement], _StdEtreeElement | _LxmlElement
        ],
    ) -> Self: ...
    @overload
    def render(self, is_unicode: Literal[False] = False) -> str | bytes: ...
    @overload
    def render(self, is_unicode: Literal[True]) -> str: ...
    def render_tree(self, **kwargs: object) -> _StdEtreeElement | _LxmlElement: ...
    def render_table(self, **kwargs: object) -> str: ...
    def render_pyquery(self, **kwargs: object) -> PyQuery: ...
    def render_in_browser(self, **kwargs: object) -> None: ...
    def render_response(self, **kwargs: object) -> flask.Response: ...
    def render_django_response(self, **kwargs: object) -> _DjangoHttpResponse: ...
    def render_data_uri(self, **kwargs: object) -> str: ...
    def render_to_file(self, filename: _FilePath | None, **kwargs: object) -> None: ...
    def render_to_png(
        self, filename: _FilePath | None = None, dpi: int = 72, **kwargs: object
    ) -> bytes | None: ...
    def render_sparktext(
        self, relative_to: float | None = None
    ) -> Literal[""] | LiteralString: ...
    def render_sparkline(
        self, **kwargs: Any  # pyright: ignore[reportAny, reportExplicitAny]
    ) -> str: ...
