# Python Hello Docker

Develop a python app from within a docker container

## Status

This simple application shows the version of the python interpreter running [src/python_hello_docker/main.py](./src/python_hello_docker/main.py). The [Dockerfile](./Dockerfile) is configured for python 3.

## Options for developing the application

Please select and setup your favorite way of developing from [Options for developing the application](./docs/options-for-developing.md).

### Run the application

```shell
python src/python_hello_docker/main.py
```

### Execute the tests once

```shell
python -m pytest
```

### Launch the test runner in the interactive watch mode

```shell
ptw . --now --last-failed --new-first
```
