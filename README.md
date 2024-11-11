# Playwright and Pytest Framework

## Table of Contents

- [Getting Started](#getting-started)
- [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
- [Installing Dependencies](#installing-dependencies)


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