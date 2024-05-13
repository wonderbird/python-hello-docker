from python_hello_docker.main import hello


def test_main():
    assert hello() == "Hello, world!"
