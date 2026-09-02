# pygal-stubs
## What is this?
- pygal-stubs is a package that provides external type stubs (PEP 561) for [pygal](https://github.com/Kozea/pygal).
- [Install](#installation) it to get static analyisis, type-checking and autocompletion in your favorite IDE, so that you no longer have to pollute your `"strict"` codebase with `# pyright: ignore[reportUnknownMemberType]`.
## What this isn't
- This package is not affiliated with [pygal](https://github.com/Kozea/pygal).
- It may not be (almost certainly isn't) 100% accurate. If you spot a mistake and know how to fix it, [submit a PR](./CONTRIBUTING.md); If you don't, open an issue.
- (Per the [LICENSE](./LICENSE), this package comes with no warranty whatsoever, however there is one thing we know for a fact will not work at all) **This package is not suitable for contributing to pygal itself**. If you try to open pygal's source with pygal-stubs installed and your type checker on `"strict"`, you will almost certainly get type-checking errors and could potentially be **misled as to the real types of the objects you're dealing with**.
    - This package is aimed at the _end users_ of pygal and as such reflects the types that appear in the public API, which might differ from implementation details.
- These stubs are not intended for use with any particular type checker, however, they were written while using [basedpyright](https://github.com/DetachHead/basedpyright) and were tested more thoroughly with it than with any other type checker. If you have a specific issue with another type checker, please [submit a PR](./CONTRIBUTING.md) or open an issue. 
- (obviously) This isn't replacement for [pygal's documentation](https://www.pygal.org/en/stable/documentation/index.html), which should always be considered the source of truth when using pygal.
## Installation
> [!IMPORTANT]
> This package currently supports **Python 3.10 and higher**.
>
> **Python versions are supported until [their EOL](https://devguide.python.org/versions/)**.
>
> This means that **Python 3.10 support will be dropped on November 1, 2026.**
>
> See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

pygal-stubs is available on [PyPI](https://pypi.org/project/pygal-stubs). Install it with:

```bash
pip install pygal-stubs
```

Or however you usually install PyPI packages.

This will automatically install the following type dependencies:
- `typing-extensions`: Backports modern typing features to all supported Python versions.
- `types-lxml` & `django-types`: Stubs for pygal's optional dependencies to prevent `Any` / `Unknown` from leaking into your codebase.

> [!WARNING]
> This package only installs the **type stubs**, not the optional runtime libraries themselves. If your code uses pygal features that rely on `lxml` or `django`, ensure you install those packages separately to avoid runtime `ImportError`s.

## Usage
If you already use a strict type checker, existing pygal code will continue to work. However, we recommend the following approach when configuring graphs:

1. **If the attribute is in the `__init__` signature**: Pass it as a keyword argument during instantiation.
2. **If the attribute is NOT in the `__init__` signature**: Assign it post-instantiation on the graph object (the pygal documentation way).

### Recommended Pattern

```python
# 1. Pass attributes in the __init__ signature during instantiation:
line_chart = pygal.Line(
    title="Browser usage evolution (in %)",
    x_labels=map(str, range(2002, 2013)),
)

# 2. For options not present in the __init__ signature, assign them on the instance:
line_chart.interpolate = "cubic"
```

The most common attributes are explicitly typed as keyword arguments in `__init__`. Options not present in `__init__` will fall into unchecked `**kwargs: object` if passed at instantiation, but **are type-checked when assigned directly on the instance**.

If an attribute you use frequently is missing from a graph's `__init__` signature, please [submit a PR](./CONTRIBUTING.md) to add it.

---

#### Why pass config as kwargs instead of mutating attributes?
pygal defines config attributes dynamically at runtime via `__setattr__`. To support autocomplete and type checking on instance attributes, the stubs declare them on the class. However, accessing an unset attribute before writing to it will pass type checking (`str | None`), but **raises an `AttributeError` at runtime**:

```python
line_chart = pygal.Line()
ttl = line_chart.title  # Type checker sees `str | None`, but Python raises AttributeError!
```

Passing attributes directly to `__init__` avoids this trap. (If you know a cleaner way to model this in type stubs, please [submit a PR](./CONTRIBUTING.md)!)

#### Why aren't all config attributes typed on `BaseGraph.__init__`?
pygal's documentation lists every config attribute in a single `Config` class, regardless of whether it applies to a given chart type. If all attributes were declared globally on `BaseGraph`, every graph class' `__init__` signature would be polluted with irrelevant options.
