# 3.1.3.4
- Dropped support for Python 3.10 due to it [reaching EOL](https://devguide.python.org/versions/#unsupported-versions) on October 1, 2026. The following types are now imported `from typing` insetad of `from typing_extensions`:
    - `Self`
    - `LiteralString`
    - `NotRequired`
- Switched to Astral's hip and trendy, blazingly fast tools:
    - hatch (CLI) has been replaced by uv.
    - Hatchling has been replaced by uv\_build.
    - black has been replaced by ruff's formatter.
    - **the official type checker is still basedpyright** and will likely remain so for the forseeable future, even after ty goes out of beta. See [PR #1](https://github.com/manucorsu/pygal-stubs/pull/1) for more details.
- Added `.python-version` file to specify the Python version for pygal-stubs development. It should always be set to the lowest supported Python version, which is currently 3.11.
- Cleaned up README
- **None of these changes should affect end users**, provided that they are using Python 3.11 or higher.
# 3.1.3.3
- Added `print_values` and `value_formatter` types to `Pie.__init__`'s kwargs.

Note: don't be alarmed by the amount of releases these days. I'm adding more types as I use them.

# 3.1.3.2
- Added the `AnyGraph` type alias to `__init__.pyi`. It is a union of all `Graph` subclasses and can be used for static typing purposes. **It does not exist at runtime** and should never ever ever be used for `isinstance` for example.
