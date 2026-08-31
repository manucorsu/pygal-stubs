PRs are welcome. Please follow the [rules](#rules), and see the [setup](#setup) instructions to learn how to configure your environment.

# Rules
- All stubs **must be compatible with Python 3.10**.
    - The supported version is the newest of:
        - the oldest Python version that is still receiving security updates (currently 3.10, see [Status of Python versions](https://devguide.python.org/versions/))
        - the oldest version of Python that [pygal](https://pypi.org/project/pygal/) supports (currently 3.8)
        - the oldest version of Python that [types-lxml](https://pypi.org/project/types-lxml/) supports (currently 3.9)
        - the oldest version of Python that [typing-extensions] supports (currently 3.9)
    - Take care to not accidentally import structures `from typing` when they should be imported `from typing_extensions` in Python 3.10.
- While the stubs themselves are not limited to any particular type checker, while working on them you should use basedpyright ([VS Code](https://marketplace.visualstudio.com/items?itemName=detachhead.basedpyright), [Open VSX](https://open-vsx.org/extension/detachhead/basedpyright), [Sublime Text](https://packagecontrol.io/packages/LSP-basedpyright); For CLI see [setup](#setup))
- Before submitting, please run `hatch check --fix`. This will. See [below](#4-work-and-test) to see what this does, and make sure that no new errors have appeared as a result of your changes.
- Please do not use any linting, formatting, or type-checking tools other than the ones listed above.
- Manually review all AI-generated code.
- If you create any types (including `TypeAlias`es, `Protocol`s, etc.) that do not exist in the source, they should be named with a leading underscore so that end users of pygal don't try to import types that don't exist in that package.
- If you believe any part of these rules, the content of `pyrightconfig.json`, the ignored linter errors in `pyproject.toml`, etc. should be changed, please open an issue: The rules should make this package and its development better, not hinder it.

# Setup
> [!NOTE]
> All Windows instructions are for cmd (Command Prompt), not PowerShell.

To begin working on the stubs, fork the repo and clone your fork. Make a branch for your changes. Then...
## 1. Make your Python version match the target
You'll notice that at the root of the repository sits a `.python-version` file, which currently contains `3.10.11`, the latest official release of Python 3.10 (see [above](#rules) for target version info).

You don't need to change your global/system Python version. Instead, you should use a version manager, such as **[pyenv](https://github.com/pyenv/pyenv)** (recommended for Linux and macOS) or the [**Python install manager**](https://www.python.org/downloads/windows/) for Windows.


### 1a. On Linux and macOS, using pyenv
At the root of the repository, run the following command to install the correct Python version.
```bash
pyenv install "$(cat .python-version)"
```
If pyenv says that that version already exists, you do not need to install it again.

After that, run `pyenv version` and you should see something like:
```
3.10.11 (set by home/u/path/to/pygal-stubs/.python-version)
```
The correct Python version will now be used automatically in this repository.
### 1b. On Windows, using the Python install manager
Unlike pyenv, the Python install manager does not read from `.python-version`, so you'll need to install the correct Python version manually by running (in a Command Prompt anywhere):
```bat
py install 3.10
```

## 2. Set up your environment
### 2.1 Create a venv
#### 2.1a On Linux and macOS, if you installed Python using pyenv (as in [1a](#1a-on-linux-and-macos-using-pyenv))
At the root of the repository, run:
```bash
python -m venv .venv
source .venv/bin/activate
```
#### 2.1b On Windows, if you installed using the Python install manager (as in [1b](#1b-on-windows-using-the-python-install-manager))
At the root of the repository, run:
```bat
python3.10.exe -m venv .venv
call .venv\Scripts\Activate
```
> [!IMPORTANT]
> After this, you should use **`python`** and not `python3.10.exe`, but for this specific step you must use `python3.10.exe` or you'll end up creating the venv with your global Python (likely 3.14) instead of 3.10.

## 3. (in any case) Install dependencies
After step 2, you should now see `(.venv)` at the beginning of your shell prompt. Running `which python` (\*nix) or `where python` (Windows cmd) should point to the `python` executable inside `.venv` (on Windows it's the first line of `where python`'s output that matters.)

To install dependencies, run the following:
```bash
python -m pip install -e .[dev]
```
This will install the dependencies (typing-extensions, types-lxml, django-types):
- hatch (for building; this package uses the Hatchling backend)
- black (for formatting)
- ruff (for linting)
- basedpyright (for type checking)
- pygal (so you have the source available in your venv)
- lxml, pyquery, Flask, Django and CairoSVG (required by some pygal features)

## 4. Work and test
After modifying the stubs, you should run `hatch check --fix`. This will:
- Format with black
- Fix linting with ruff
- Give you a summary of any type errors (from basedpyright) and linter errors that couldn't be auto-fixed (from ruff)

Please make sure that there are no type errors, then submit a PR.

# Additional considerations
- Once you're done working, you can run `deactivate` to make your shell leave the venv.
- **Visual Studio Code users beware**: This repository has a `.vscode/settings.json` file that will disable Pylance (Microsoft's proprietary Python language server that comes with the Python extension). Install the **[basedpyright extension](https://marketplace.visualstudio.com/items?itemName=detachhead.basedpyright)** to regain in-editor type checking.
    - Pylance will remain enabled in all other projects that don't have a `.vscode/settings.json` like this, taking priority over basedpyright.
    - _Users of non-proprietary releases (i.e. VSCodium or built from source), and forks (i.e Antigravity IDE) don't need to worry about this because Microsoft does not make Pylance available to them. You should still make sure you're using basedpyright and not another language server like pyrefly._
