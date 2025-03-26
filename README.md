# RealWorld Example App

This codebase was created to demonstrate a fully fledged full-stack application
built with [Django](https://www.djangoproject.com/) including CRUD operations,
authentication, routing, pagination, and more. For more information on how this
works, head over to the [RealWorld](https://github.com/gothinkster/realworld)
repo.

## Getting Started

First, make sure that these requirements are already installed:

* [Python](https://www.python.org/) (version 3.11, recommended to use
  [pyenv](https://github.com/pyenv/pyenv))
* [Poetry](https://python-poetry.org/)

Then, set up the application using these commands:

```shell
# Set up the virtual environment
virtualenv .venv
source .venv/bin/activate

# Install the Python packages
poetry install

# Set up the environment variables
export DEBUG=1
export SECRET_KEY=<PUT_YOUR_SECRET_KEY_HERE>

# Run the application server
python manage.py runserver
```

## Development Tools

### Pre-Commit Hooks

To ensure code standard, this project uses
[pre-commit](https://pre-commit.com/) hooks. Install them using this command:

```shell
pre-commit install
```
