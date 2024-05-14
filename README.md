# Python Hello Docker

Develop a python app from within a docker container

## Status

This simple application shows the version of the python interpreter running [src/python_hello_docker/main.py](./src/python_hello_docker/main.py). The [Dockerfile](./Dockerfile) is configured for python 3.

## Debugging from Inside the Docker Container

Read and follow the **Preqequisites** section in in [Build and run a Python app in a container](https://code.visualstudio.com/docs/containers/quickstart-python) to setup your Visual Studio Code and Docker for debugging the application.

To debug, jump to the section **Build, run, and debug the container** in [Build and run a Python app in a container](https://code.visualstudio.com/docs/containers/quickstart-python):

1. Navigate to the file that contains your app's startup code, and set a breakpoint

2. Navigate to Run and Debug and select Docker: Python - General

3. Start debugging using the F5 key

## Developing Locally on Your Machine

### Prerequisites

It is recommended to use a python virtual environment. Create and activate it:

```shell
python3 -m venv venvsource venv/bin/activate
```

Install the required python packages:

```shell
pip install -r requirements.txt
```

Then install this package in development mode:

```shell
pip install --editable .
```

### Run the Application

```shell
python src/python_hello_docker/main.py
```

### Execute the Tests Once

```shell
python -m pytest
```

### Launch the Test Runner in the Interactive Watch Mode

```shell
ptw . --now --last-failed --new-first
```
