import sys


def python_version_message():
    major, minor, _, _, _ = sys.version_info
    python_version = f"{major}.{minor}"
    return f"You are running python version {python_version}"


if __name__ == "__main__":
    print(python_version_message())
