import re

from python_hello_docker.main import python_version_message


def test_main():
    message = python_version_message()

    version_number = re.search(r"\d+\.\d+", message).group()
    major, minor = version_number.split(".")
    
    assert major == "3" and minor == "10"
