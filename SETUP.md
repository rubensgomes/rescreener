# Setup

This page contains information to setup your development environment for 
the `recscreener` application.

## Getting Started

### Prerequisites

- pipx 1.7.1 or later
- poetry 2.1.3 or later
- pylint 3.3.7 or later
- python3 3.13.0 or later
- pytest 8.3.4 or later
- IDE (e.g., PyCharm)

## Setting Up Shell Development Environment

Following instructions are for `macOS UNIX`:

1. Ensure python3, and pipx are installed:

    ```shell
    brew install python3
    brew install pipx
    pipx ensurepath
    ```

2. Install `pylint`, `poetry`, and `poetry-plugin-shell`  using `pipx`

    ```shell
    pipx install pylint
    pipx install poetry
    # notice that the poetry-plugin-shell needs to be injected
    pipx inject poetry poetry-plugin-shell
    ```

3. Upgrade `poetry` and update dependencies

- to upgrade `poetry`:

    ```shell
    pipx upgrade poetry
  ```
  
- to get latest versions of dependencies and to update `poetry.lock`:

    ```shell
    poetry update -vvv
    ```

- to update `poetry.lock` after changes to `pyproject.toml`:

    ```shell
    poetry lock --regenerate -vv
    ```

## Creating Shell Python Virtual Environment

As per [PEP 668](https://peps.python.org/pep-0668/) starting with Python 3.12,
non-brew-packaged Python package should only be installed in virtual
environments.

1. Configure `poetry` venv location and install packages defined in the
   `pyproject.toml` dependencies:

    ```shell
    # configure poetry to create virtual environment under <project>/.venv
    poetry config virtualenvs.in-project true
    poetry lock --regenerate -vv
    poetry build
    poetry install
    ```

2. To display information about the virtual environment:

    ```shell
    poetry env info
    ```

3. Open a shell within virtual environment using `poetry`:

    ```shell
    # Ensure at the top of the project root folder
    # NOTE: this assumes you have cloned this project from a Git repo
    cd $(git rev-parse --show-toplevel) || exit
    poetry shell
    ```

## Clean Shell Environment

- To complete clean any files and folders from this project untracked by git,
  including venv (virtual enviroments) run:

    ```shell
    git clean -fXd
    ```

- To remove only the virtual environment delete the `.venv` folder:

    ```shell
    # Ensure at the top of the project root folder
    # NOTE: this assumes you have cloned this project from a Git repo
    cd $(git rev-parse --show-toplevel) || exit
    rm -fr .venv/
    ```

## Setting Up PyCharm IDE Development Environment

- First, ensure to follow all the previous steps to "Setting Up Shell
  Development Environment"

1. Open the project `rescreener` folder using `PyCharm`
2. Follow instructions
   to [Create a Poetry environment](https://www.jetbrains.com/help/pycharm/poetry.html#poetry-env)
    - Click on the Python Interpreter Selector to "Add New Interpreter"
    - Select "Add Local Interpreter..."
    - Select "Poetry Environment"
    - Ensure "Base interpreter" is /opt/homebrew/bin/python3 (macOS only)
    - Ensure "Poetry executable" (e.g., ${HOME}/.local/bin/poetry)
    - Click the OK button
3. Go to `PyCharm` > `Settings`
    - Enter `Python Integrated Tools`
    - Under `Testing` > `Default test runner` select `pytest`
4. Open `PyCharm` > `Terminal` to go to venv prompt
    - Ensure .venv correct settings:

    ```shell
    poetry env info
    ```

## Linting the Code

   ```shell
   cd $(git rev-parse --show-toplevel) || exit
   poetry run pylint rescreener
   ```

## Running the Unit Tests with Coverage

   ```shell
   cd $(git rev-parse --show-toplevel) || exit
   # run pytest with coverage
   poetry run python -m coverage run -m pytest tests/
   # generate coverage report
   poetry run python -m coverage report -m
   ```
   
