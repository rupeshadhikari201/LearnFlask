Pipenv: Python Virtual Environment Management Tool

Pipenv is a powerful tool for managing Python virtual environments. It bridges the gaps between pip, Python (using system Python, pyenv, or asdf), and virtualenv, supporting a multitude of systems.

## Table of Contents

1. [Installation](#installation)
2. [Basic Commands](#basic-commands)
3. [Additional Commands](#additional-commands)
4. [Windows-Specific Notes](#windows-specific-notes)
5. [Running Flask Applications](#running-flask-applications)

## Installation

To install Pipenv, use the following command:

```
pip install pipenv
```

## Basic Commands

Here are the essential Pipenv commands you'll need to get started:

1. **Create a virtual environment:**

   ```
   pipenv install
   ```

   This creates a virtual environment and adds two files: `Pipfile` and `Pipfile.lock`.

2. **Activate the virtual environment:**

   ```
   pipenv shell
   ```

   This launches the virtual environment in the current directory.

3. **Exit the virtual environment:**

   ```
   exit
   ```

4. **Install a package (e.g., Flask):**

   ```
   pipenv install flask
   ```

5. **List all installed packages:**
   ```
   pipenv list
   ```

## Additional Commands

Pipenv offers several other useful commands:

- `--where`: Output project home information.
- `--venv`: Output virtualenv information.
- `--py`: Output Python interpreter information.
- `--envs`: Output Environment Variable options.
- `--rm`: Remove the virtualenv.
- `--bare`: Minimal output.
- `--man`: Display manpage.
- `--support`: Output diagnostic information for use in GitHub issues.
- `--version`: Show the version and exit.
- `-h, --help`: Show help message and exit.

## Windows-Specific Notes

On Windows, the `./` prefix is not recognized as it is in Unix-based systems. Windows doesn't use forward slashes (/) to separate directories. To run scripts or commands, use the full path without the `./` prefix.

## Running Flask Applications

To run a Flask application on Windows, use the following commands:

```
set FLASK_APP=hello
set FLASK_ENV=development
flask run
```

Replace `hello` with the name of your Flask application file (without the .py extension).

---

Feel free to contribute to this README or report any issues you encounter while using Pipenv!
