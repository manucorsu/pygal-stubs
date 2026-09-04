# pygal-stubs
## What is this?
- pygal-stubs is a package that provides external type stubs (PEP 561) for [pygal](https://github.com/Kozea/pygal).
- [Install](#installation) it to get static analyisis, type-checking and autocompletion in your favorite IDE, so that you no longer have to pollute your `"strict"` codebase with `# pyright: ignore[reportUnknownMemberType]`. Be sure to read [Usage](#usage) as well.
## What this isn't
- This package is not affiliated with [pygal](https://github.com/Kozea/pygal).
- It may not be (almost certainly isn't) 100% accurate. If you spot a mistake and know how to fix it, [submit a PR](./CONTRIBUTING.md); If you don't, open an issue.
- (Per the [LICENSE](./LICENSE), this package comes with no warranty whatsoever, however there is one thing we know for a fact will not work at all) **This package is not suitable for contributing to pygal itself**. If you try to open pygal's source with pygal-stubs installed and your type checker on `"strict"`, you will almost certainly get type-checking errors and could potentially be **misled as to the real types of the objects you're dealing with**.
    - This package is aimed at the _end users_ of pygal and as such reflects the types that appear in the public API, which might differ from implementation details.
- These stubs are not intended for use with any particular type checker, however, they were written while using [basedpyright](https://github.com/DetachHead/basedpyright) and were tested more thoroughly with it than with any other type checker. If you have a specific issue with another type checker, please [submit a PR](./CONTRIBUTING.md) or open an issue. 
- (obviously) This isn't replacement for [pygal's documentation](https://www.pygal.org/en/stable/documentation/index.html), which should always be considered the source of truth when using pygal.
## Installation
> [!NOTE]
> This package currently supports **Python 3.10 and higher**.
>
> **Python versions are supported until [their EOL](https://devguide.python.org/versions/)**.
>
> This means that **Python 3.10 support will be dropped on November 1, 2026.**
>
> See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

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

Note that this package only installs the **type stubs**, not the optional runtime libraries themselves. If your code uses pygal features that rely on `lxml` or `django`, ensure you install those packages separately to avoid runtime `ImportError`s. Same thing goes for the **maps**: We provide stubs for the World Map ([pygal_maps_world_neo](https://github.com/manucorsu/pygal_maps_world_neo)), but if you want to use the maps, you'll need to install the library itself or you will get a runtime error.

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
# Instead of:
import pygal
line = pygal.Line()
line.title = "My Title"

# You can do:
import pygal
line = pygal.Line(title="My Title")
```

Values that aren't in the `__init__` signature will be assigned just fine, but **they won't be type checked** as you'll be falling back to the untyped `**kwargs`. If you believe that more attributes should be added to an `__init__` method signature, please [submit a PR](./CONTRIBUTING.md).

### Why is this?
pygal does not define which attributes each specific Graph type requires, instead providing all attributes, for all graphs, in the massive [CommonConfig and Config classes](./pygal-stubs/config.pyi) for documentation purposes. Then, at runtime, all attributes are assigned arbitrarily (via `__setattr__` from either explicit `instance.attr = val` asignment from the user or at instantiation time from the constructor `**kwargs`) to the graph instances.

This means that if we wanted type-checking for these values (instead of accepting anything for any key like `__setattr__` normally does), we had to basically hardcode _all_ config attributes for all graphs as properties of `BaseGraph`, the class that all graphs inherit from. If you know a better way to do this without erasing type checking for these attributes, please [submit a PR](./CONTRIBUTING.md)