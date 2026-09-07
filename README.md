_The most up-to-date version of this README is on [GitHub](https://github.com/manucorsu/pygal-stubs/blob/main/README.md)._

# pygal-stubs
## What is this?
- pygal-stubs is a package that provides external type stubs (PEP 561) for [pygal](https://github.com/Kozea/pygal).
- [Install](#installation) it to get static analyisis, type-checking and autocompletion in your favorite IDE, so that you no longer have to pollute your `"strict"` codebase with `# pyright: ignore[reportUnknownMemberType]`. Be sure to read [Usage](#usage) as well.
## What this isn't
- This package is not affiliated with [pygal](https://github.com/Kozea/pygal).
- It is almost certainly not perfect or 100% accurate. If you spot a mistake (any mistake) and know how to fix it, [submit a PR](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md); If you don't, open an issue.
- (Per the [LICENSE](https://github.com/manucorsu/pygal-stubs/blob/main/LICENSE), this package comes with no warranty whatsoever, however there is one thing we know for a fact will not work at all) **This package is not suitable for contributing to pygal itself**. If you try to open pygal's source with pygal-stubs installed and your type checker on `"strict"`, you will almost certainly get type-checking errors and could potentially be **misled as to the real types of the objects you're dealing with**.
    - This package is aimed at the _end users_ of pygal and as such reflects the types that appear in the public API, which might differ from implementation details.
- These stubs are not intended for use with any particular type checker, however, they were written while using [basedpyright](https://github.com/DetachHead/basedpyright) and were tested more thoroughly with it than with any other type checker. As such, it is this package's **primary target type checker** (it's extremely similar to Pylance so vanilla VS Code users should have no issues). If you have a specific issue with another type checker, please [submit a PR](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md) or open an issue.
- (obviously) This isn't replacement for [pygal's documentation](https://www.pygal.org/en/stable/documentation/index.html), which should always be considered the source of truth when using pygal.
## Installation
> [!NOTE]
> This package currently supports **Python 3.10 and higher**.
>
> **Python versions are supported until [their EOL](https://devguide.python.org/versions/)**.
>
> This means that **Python 3.10 support will be dropped in October 2026**.
>
> See [CONTRIBUTING.md](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md) for more details.

> [!WARNING]
> Read [Usage](#usage) before using these stubs to avoid **unexpected runtime errors**.

pygal-stubs is available on [PyPI](https://pypi.org/project/pygal-stubs). Install it with:

```bash
pip install pygal-stubs
```

Or however you usually install PyPI packages.

This will automatically install the following type dependencies:
- `typing-extensions`: Backports modern typing features to all supported Python versions.
- `types-lxml` & `django-types`: Stubs for pygal's optional dependencies to prevent `Any` / `Unknown` from leaking into your codebase.
    - You might still get `Unknown` from other pygal dependencies that don't have type stubs available such as cairosvg and pyquery, as well as the map modules (see below).

Note that this package only installs the **type stubs**, not the optional runtime libraries themselves. If your code uses pygal features that rely on `lxml` or `django`, ensure you install those packages separately to avoid runtime `ImportError`s.

This package **does not include stubs for the separately packaged map modules**. You'll need to download those separately. I have created type stubs for my active fork of the world map module. You can find them here: [fork](https://github.com/manucorsu/pygal_maps_world_neo), [stubs](https://github.com/manucorsu/pygal_maps_world_neo-stubs). [^1]

[^1]: I cannot currently work on stubs for other map modules (both the documented France and Switzerland maps nor the various non-Kozea ones you can find on PyPI). If you want to make your own type stubs for those, you're more than welcome to do so using pygal-stubs and my world map stubs as a base. If you'd like those stubs to be compatible with pygal-stubs and a mistake in the definition of BaseMap is causing problems, please [submit a PR](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md). Once you're done making your type stubs, make an issue so I can add your wonderful contribution to this README for all pygal-stubs users to see.

## Usage
> [!IMPORTANT]
> TLDR: **Avoid reading Graph config attributes if possible**. If you have to do it anyways, **ALWAYS use a `try-except` block to handle potential `AttributeError`**.

If you already use a strict type checker, existing pygal code will continue to work. However, there is one key detail you must know: Graph attributes (used to configure graphs) are set dynamically at runtime via `__setattr__`, not defined explicitly on `__init__`. This means that **if you try to access a Graph attribute you haven't set explicitly, you'll get an `AttributeError` at runtime** that type checkers (and these stubs) have no way of knowing about.

For example:
```python
line = pygal.Line()
title = line.title # Your type checker will say this is str | None, when in reality this line will cause an AttributeError!
```

This isn't an issue if you never read these attributes. Assigning to them doesn't cause any issues, as seen here:

```python
import pygal
line = pygal.Line()
line.title = "My Title" # This is fine
```

We have also added the more popular (the ones found in the docs + a couple of others) attributes to the `__init__` method stubs, so you can assign them directly at instantiation:

```python
import pygal
# Instead of:
line = pygal.Line()
line.title = "My Title"

# or:
config = pygal.Config()
config.title = "My Title"
line = pygal.Line(config)

# You can do:
line = pygal.Line(title="My Title")
```

Values that aren't in the `__init__` signature will be assigned just fine, but **they won't be type checked** as you'll be falling back to the untyped `**kwargs`. If you believe that more attributes should be added to an `__init__` method signature, please [submit a PR](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md). This paragraph also applies to some other methods (e.g. `add`)

### Why is this?
pygal does not define which attributes each specific Graph type requires, instead providing all attributes, for all graphs, in the massive [CommonConfig and Config classes](https://github.com/manucorsu/pygal-stubs/blob/main/pygal-stubs/config.pyi) for documentation purposes. Then, at runtime, all attributes are assigned arbitrarily (via `__setattr__` from either explicit `instance.attr = val` asignment from the user or at instantiation time from the constructor `**kwargs`) to the graph instances.

This means that if we wanted type-checking for these values (instead of accepting anything for any key like `__setattr__` normally does), we had to basically hardcode _all_ config attributes for all graphs as properties of `BaseGraph`, the class that all graphs inherit from. If you know a better way to do this without erasing type checking for these attributes, please [submit a PR](https://github.com/manucorsu/pygal-stubs/blob/main/CONTRIBUTING.md)