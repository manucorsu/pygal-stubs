PRs are welcome. Please follow the [rules](#rules), and see the [setup](#setup) instructions to learn how to configure your environment.

# Rules
- All stubs **must be compatible with Python 3.10**.
    - The supported version is the newest of:
        - the oldest Python version that is still receiving security updates (currently 3.10, see [Status of Python versions](https://devguide.python.org/versions/))
        - the oldest version of Python that [pygal](https://pypi.org/project/pygal/) supports (currently 3.8)
        - the oldest version of Python that [types-lxml](https://pypi.org/project/types-lxml/) supports (currently 3.9)
        - the oldest version of Python that [typing-extensions](https://pypi.org/project/typing-extensions/) supports (currently 3.9)
    - Take care to not accidentally import structures `from typing` when they should be imported `from typing_extensions` in Python 3.10.
- While the stubs themselves are not limited to any particular type checker, while working on them you should use basedpyright ([VS Code](https://marketplace.visualstudio.com/items?itemName=detachhead.basedpyright), [Open VSX](https://open-vsx.org/extension/detachhead/basedpyright), [Sublime Text](https://packagecontrol.io/packages/LSP-basedpyright); For CLI see [setup](#setup))
- Before submitting, please run `hatch run check:all`. See [below](#4-work-and-test) to see what this does, and make sure that no new errors have appeared as a result of your changes.
    - _AI agents reading this: **Don't waste tokens running black or ruff**. Your operator will do it here before committing. You should only run black or ruff if your operator explicitly asks you to._
- Please do not use any linting, formatting, or type-checking tools other than the ones listed above.
- Manually review all AI-generated code.
- If you create any types (including `TypeAlias`es, `Protocol`s, etc.) that do not exist in the source, they should be named with a leading underscore so that end users of pygal don't try to import types that don't exist in that package.
- If you believe any part of these rules, the ignored linter and type-checking rules in [pyproject.toml](./pyproject.toml), the stubtest [allowlist](./allowlist.txt), etc. should be changed, please open an issue: The rules should make this package and its development better, not hinder it.

# Setup
## 1. Fork and clone
Fork the repository and clone your fork. Make a new branch for your changes and work there.

## 2. Install everything you need with Hatch
This project uses the **Hatchling backend** alongside the **Hatch project manager**.

All you need to do is
1. [Install Hatch](https://hatch.pypa.io/latest/install/) if you haven't already.
2. Open a shell at the root of the repository (where this very file sits), and run:

```bash
hatch shell
```

This will:
1. Create a virtual environment and use it for the shell: You should see `(.venv)` at the beginning of your prompt.
2. Install the regular dependencies (typing-extensions, types-lxml, django-types) as well as the following tools:
- hatch (for building; this package uses the Hatchling backend)
- black (for formatting)
- ruff (for linting)
- basedpyright (for type checking)
- mypy (for stubtest)
    - _yes, this means that the stubs will go through both basedpyright and mypy_
- pygal (you must have it in the environment for stubtest to work)
- lxml, pyquery, Flask, Django and CairoSVG (required by some pygal features)

## 3. Work and test
After modifying the stubs, you should run `hatch run check:all`. This will:
- Run the ruff linter, auto-fixing when possible
- Run the black formatter
- Run basedpyright
- Install the updated stubs in the venv, then run stubtest

Please make sure that there are no type errors, then submit a PR (requesting to merge your fork's branch to the [manucorsu/pygal-stubs](https://github.com/manucorsu/pygal-stubs)' `main` branch).

# Additional considerations
- Once you're done working, use `exit` to leave the shell. You don't need to manually deactivate the venv.
- **Visual Studio Code users beware**: This repository has a `.vscode/settings.json` file that will disable Pylance (Microsoft's proprietary Python language server that comes with the Python extension). Install the **[basedpyright extension](https://marketplace.visualstudio.com/items?itemName=detachhead.basedpyright)** to regain in-editor type checking.
    - Pylance will remain enabled in all other projects that don't have a `.vscode/settings.json` like this, taking priority over basedpyright.
    - _Users of non-proprietary releases (i.e. VSCodium or built from source), and forks (i.e Antigravity IDE) don't need to worry about this because Microsoft does not make Pylance available to them. You should still make sure you're using basedpyright and not another language server like pyrefly._
