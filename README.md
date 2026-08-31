# pygal-stubs
## What is this?
- pygal-stubs is a package that provides external type stubs (PEP 561) for [pygal](https://github.com/Kozea/pygal).
- [Install](#installation) it to get static analyisis, type-checking and autocompletion in your favorite IDE, so that you no longer have to pollute your `"strict"` codebase with `# pyright: ignore[reportUnknownMemberType]`.
## What this isn't
- This package is not affiliated with [pygal](https://github.com/Kozea/pygal).
- It may not be (almost certainly isn't) 100% accurate. If you spot a mistake and know how to fix it, [submit a PR](./CONTRIBUTING.md); If you don't, open an issue.
- (Per the [LICENSE](./LICENSE), this package comes with no warranty whatsoever, however there is one thing we know for a fact will not work at all) **This package is not suitable for contributing to pygal itself**. If you try to open pygal's source with pygal-stubs installed and your type checker on `"strict"`, you will almost certainly get type-checking errors and could potentially be **misled as to the real types of the objects you're dealing with**.
    - This package is aimed at the _end users_ of pygal and as such reflects the types that appear in the public API, which might differ from implementation details.
- A replacement for [pygal's documentation](https://www.pygal.org/en/stable/documentation/index.html), which should always be considered the source of truth when using pygal.
## Installation
> [!IMPORTANT]
> This package currently supports **Python 3.10 and higher**.
>
> **Python versions are supported until [their EOL](https://devguide.python.org/versions/)**.
>
> This means that **Python 3.10 support will be dropped on November 1, 2026.**
>
> See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

pygal-stubs is available on [PyPI](). Installation is simple: just do `pip install pygal-stubs`, or however you usually install PyPI packages. Note that this will also install the following dependencies:

- typing-extensions
- types-lxml
- django-types

typing-extensions is required to backport modern typing features to the older Python versions we support. The others are type stubs for pygal's optional dependencies, which would've otherwise caused `Unknown` or `Any` to propagate in some parts of the stubs.