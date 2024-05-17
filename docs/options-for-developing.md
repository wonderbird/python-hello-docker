# Options for developing the application

You can either develop using your local python installation or work with a docker container. If you are using Visual Studio Code, then you can use the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) to [run and debug from within a container](https://code.visualstudio.com/docs/containers/quickstart-python). As an alternative you can run a [Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container) in VSCode.

The following sections address each of the options.

## Developing in your locally installed python 3 environment

This is the recommended way of developing, because it provides the best developer experience with regards to IDE integration and running the tests.

### Prerequisites

It is recommended to use a python 3 virtual environment. Create and activate it:

```shell
python -m venv
source venv/bin/activate
```

Install the required python packages:

```shell
pip install -r requirements.txt
```

Then install this package in development mode:

```shell
pip install --editable .
```

## NOTE: You cannot run the unit tests from python 2.7

If you use python 2.7, then you won't be able to run the unit tests.

Running the tests requires installing this directory as an editable package. To facilitate this, the project uses [pyproject.toml](./pyproject.toml) and the packages `build` and `hatch`.

Unfortunately, python 2.7 requires `setup.py` and does not support the more modern `pyproject.toml` approach.

## Running with Docker

In this example I use python 2.7 - working with a python 3 container works similarly.

Connect current directory to a python 2.7 docker container:

```shell
docker run --rm -it -v "$PWD:/app" --name python27 python:2.7 /bin/bash
cd /app
```

Run the script:

```shell
python src/python_hello_docker/main.py
You are running python version 2.7
```

Leave the container - it will be removed, because the `--rm` flag was given when creating it:

```shell
exit
```

## VSCode: Debug from inside a plain docker container using the Docker extension

NOTE: For python 2.7, setting up the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) for Visual Studio Code is complicated (1)(2). Thus I suggest running python 2.7 manually from inside a corresponding docker container, as described in the section **Running with Docker** above.

- (1) [Stack Overflow: Visual Studio Code debugs python 2.7 app in a docker container with python3](https://stackoverflow.com/a/69395067)
- (2) [GitHub: Visual Studio Code debugs python 2.7 app in a docker container with python3](https://github.com/microsoft/vscode-docker/discussions/3585)

Read and follow the **Preqequisites** section in in [Build and run a Python app in a container](https://code.visualstudio.com/docs/containers/quickstart-python) to setup your Visual Studio Code and Docker for debugging the application.

To debug, jump to the section **Build, run, and debug the container** in [Build and run a Python app in a container](https://code.visualstudio.com/docs/containers/quickstart-python):

1. Navigate to the file that contains your app's startup code, and set a breakpoint

2. Navigate to Run and Debug and select Docker: Python - General

3. Start debugging using the F5 key

## VSCode: Run with a Dev Container

The `.devcontainer` directory contains the [configuration](./.devcontainer/devcontainer.json), a custom [Dockerfile](./.devcontainer/Dockerfile) and [requirements.txt](./.devcontainer/requirements.txt) file to run a python 2.7 environment inside a [VSCode Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container). You can adapt these for python 3.

To switch VSCode to the Dev Container, select **Dev Containers: Reopen in Container** from the command palette.

To leave the Dev Container, select **Dev Containers: Reopen Folder locally** from the command palette.
