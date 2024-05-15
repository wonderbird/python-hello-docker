import sys


def python_version_message():
    major, minor, _, _, _ = sys.version_info
    python_version = "{}.{}".format(major, minor)
    return "You are running python version {}".format(python_version)


if __name__ == "__main__":
    print(python_version_message())
