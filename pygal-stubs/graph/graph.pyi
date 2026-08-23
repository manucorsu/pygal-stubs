from pygal import stats as stats
from pygal._compat import is_list_like as is_list_like
from pygal.graph.public import PublicApi as PublicApi
from pygal.interpolate import INTERPOLATIONS as INTERPOLATIONS
from pygal.util import cached_property as cached_property, compute_scale as compute_scale, cut as cut, decorate as decorate, filter_kwargs as filter_kwargs, get_text_box as get_text_box, get_texts_box as get_texts_box, majorize as majorize, rad as rad, reverse_text_len as reverse_text_len, split_title as split_title, truncate as truncate
from pygal.view import LogView as LogView, ReverseView as ReverseView, View as View, XYLogView as XYLogView

class Graph(PublicApi):
    @property
    def all_series(self): ...
    def add_squares(self, squares): ...
