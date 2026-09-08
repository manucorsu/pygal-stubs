# 3.1.3.3
- Added `print_values` and `value_formatter` types to `Pie.__init__`'s kwargs.

Note: don't be alarmed by the amount of releases these days. I'm adding more types as I use them.

# 3.1.3.2
- Added the `AnyGraph` type alias to `__init__.pyi`. It is a union of all `Graph` subclasses and can be used for static typing purposes. **It does not exist at runtime** and should never ever ever be used for `isinstance` for example.