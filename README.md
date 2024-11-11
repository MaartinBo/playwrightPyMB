# Playwright and Pytest Framework

## Table of Contents

- [Getting Started](#getting-started)
- [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Visual Studio Code Setup](#visual-studio-code-setup)
- [Code Formatting](#code-formatting)
- [Code Linting](#code-linting)
- [Pre-commit Hooks](#pre-commit-hooks)

## Getting Started

**Prerequisites**

- **Python 3.7+**: Make sure you have Python 3.7 or higher installed.
- **Pip**: Python package installer should be available.
- **Git**: Required for version control.
- **Node.js**: Needed for Playwright browsers (Playwright will install it automatically if not present).
- **Visual Studio Code**: Recommended IDE for this project (optional).

**Clone the Repository**

Begin by cloning the repository to your local machine:

```bash
git clone https://github.com/MaartinBo/playwrightPyMB.git
cd playwrightPyMB
```

## Setting Up a Virtual Environment

It's recommended to create a virtual environment for this project to manage dependencies cleanly:

**1.Create the Virtual Environment:**

```bash
python3 -m venv .venv
```

**2.Activate the Virtual Environment:**

Use the appropriate command based on your terminal and operating system:

**Git Bash on Windows:**

```
source .venv/Scripts/activate
```

**Linux/Mac:**

```
source .venv/bin/activate
```

**For Windows (basic cmd)**

```
.venv\Scripts\activate
```

**For Windows(powershell)**

```
.venv\Scripts\Activate.ps1
```

## Installing Dependencies

With the virtual environment activated, install the required packages by running:

```bash
pip install -r requirements.txt
```

## Visual Studio Code Setup

Recommended extensions and settings are provided in the `.vscode` folder for an optimal development experience.

### Recommended Extensions

- **Python** (`ms-python.python`)
- **Pylance** (`ms-python.vscode-pylance`)
- **Playwright Test for VSCode** (`ms-playwright.playwright`)
- **Code Spell Checker** (`streetsidesoftware.code-spell-checker`)
- **Isort** (`ms-python.isort`) - for organizing imports
- **Black Formatter** (`ms-python.black-formatter`) - for consistent code formatting

### Settings

- **Formatting**: Code is automatically formatted on save using Black via the `ms-python.black-formatter` extension.
- **Organizing Imports**: Imports are automatically organized on save using `isort`, configured to follow Black's style for consistency.
- **Linting**: Flake8 is enabled for linting Python code, providing immediate feedback on code style and syntax issues.
- **Testing**: Pytest is configured as the default test framework, and tests are expected to be located in the `tests` directory.
- **Type Checking**: Pylance is set up with basic type checking (`typeCheckingMode: "basic"`) to help maintain code quality and identify potential issues early.
- **Spell Check**: The Code Spell Checker is configured to recognize specific terms, such as `pytestmark`, to avoid unnecessary spell check warnings on domain-specific terms.

### Additional Configuration Details

- **Python Interpreter**: The Python interpreter path is set to `env/bin/python`, assuming a virtual environment located in the `env` folder.
- **File Exclusion**: Commonly generated cache files and directories, such as `__pycache__` and `.pytest_cache`, are excluded from the file watcher to improve performance and reduce clutter.
- **Organizing Imports on Save**: The setting `editor.codeActionsOnSave.source.organizeImports` is configured as `"explicit"`, ensuring that imports are organized whenever files are saved.

## Code Formatting

I use **Black** for code formatting.

The configuration is stored in `pyproject.toml`

To launch black in "check" mode run:

```bash
black --check .
```

To format the code run:

```bash
black  .
```

## Code Linting

I use **Flake8** for linting to maintain code quality.

The configuration is stored in `pyproject.toml` using the `flake8-pyproject` plugin.

To run the linter use:

```bash
flake8
```

## Pre-commit Hooks

I use pre-commit to automate code formatting and linting.

### Installing Pre-commit Hooks

To set up pre-commit hooks for this project, run:

```bash
pre-commit install
```

### Running Pre-commit Hooks Manually

To run all hooks against all files:

```bash
pre-commit run --all-files
```

Expected result:

![alt text](image.png)
