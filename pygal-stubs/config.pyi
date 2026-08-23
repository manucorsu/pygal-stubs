from _typeshed import Incomplete
from pygal import formatters as formatters
from pygal.interpolate import INTERPOLATIONS as INTERPOLATIONS
from pygal.style import DefaultStyle as DefaultStyle, Style as Style

CONFIG_ITEMS: Incomplete
callable: Incomplete

class Key:
    value: Incomplete
    type: Incomplete
    doc: Incomplete
    category: Incomplete
    subdoc: Incomplete
    subtype: Incomplete
    name: str
    def __init__(
        self, default_value, type_, category, doc, subdoc: str = "", subtype=None
    ) -> None: ...
    @property
    def is_boolean(self): ...
    @property
    def is_numeric(self): ...
    @property
    def is_string(self): ...
    @property
    def is_dict(self): ...
    @property
    def is_list(self): ...
    def coerce(self, value): ...

class MetaConfig(type):
    def __new__(mcs, classname, bases, classdict): ...

class BaseConfig(Incomplete):
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, **kwargs) -> None: ...
    def to_dict(self): ...
    def copy(self): ...

class CommonConfig(BaseConfig):
    stroke: Incomplete
    show_dots: Incomplete
    show_only_major_dots: Incomplete
    dots_size: Incomplete
    fill: Incomplete
    stroke_style: Incomplete
    rounded_bars: Incomplete
    inner_radius: Incomplete
    allow_interruptions: Incomplete
    formatter: Incomplete

class Config(CommonConfig):
    style: Incomplete
    css: Incomplete
    classes: Incomplete
    defs: Incomplete
    title: Incomplete
    x_title: Incomplete
    y_title: Incomplete
    width: Incomplete
    height: Incomplete
    show_x_guides: Incomplete
    show_y_guides: Incomplete
    show_legend: Incomplete
    legend_at_bottom: Incomplete
    legend_at_bottom_columns: Incomplete
    legend_box_size: Incomplete
    rounded_bars: Incomplete
    stack_from_top: Incomplete
    spacing: Incomplete
    margin: Incomplete
    margin_top: Incomplete
    margin_right: Incomplete
    margin_bottom: Incomplete
    margin_left: Incomplete
    tooltip_border_radius: Incomplete
    tooltip_fancy_mode: Incomplete
    inner_radius: Incomplete
    half_pie: Incomplete
    reverse_direction: Incomplete
    x_labels: Incomplete
    x_labels_major: Incomplete
    x_labels_major_every: Incomplete
    x_labels_major_count: Incomplete
    show_x_labels: Incomplete
    show_minor_x_labels: Incomplete
    y_labels: Incomplete
    y_labels_major: Incomplete
    y_labels_major_every: Incomplete
    y_labels_major_count: Incomplete
    show_minor_y_labels: Incomplete
    show_y_labels: Incomplete
    x_label_rotation: Incomplete
    y_label_rotation: Incomplete
    missing_value_fill_truncation: Incomplete
    x_value_formatter: Incomplete
    value_formatter: Incomplete
    logarithmic: Incomplete
    interpolate: Incomplete
    interpolation_precision: Incomplete
    interpolation_parameters: Incomplete
    box_mode: Incomplete
    order_min: Incomplete
    min_scale: Incomplete
    max_scale: Incomplete
    range: Incomplete
    secondary_range: Incomplete
    xrange: Incomplete
    include_x_axis: Incomplete
    zero: Incomplete
    no_data_text: Incomplete
    print_values: Incomplete
    dynamic_print_values: Incomplete
    print_values_position: Incomplete
    print_zeroes: Incomplete
    print_labels: Incomplete
    truncate_legend: Incomplete
    truncate_label: Incomplete
    js: Incomplete
    disable_xml_declaration: Incomplete
    force_uri_protocol: Incomplete
    explicit_size: Incomplete
    pretty_print: Incomplete
    strict: Incomplete
    no_prefix: Incomplete
    inverse_y_axis: Incomplete

class SerieConfig(CommonConfig):
    title: Incomplete
    secondary: Incomplete
