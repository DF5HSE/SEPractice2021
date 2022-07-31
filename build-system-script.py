import sys
import subprocess
import platform
from typing import List


def call_all(calls: List[str]):
    for call in calls:
        if subprocess.call(call.split()) != 0:
            raise RuntimeError(f"Call '{call}' failed")


def install_dependencies():
    calls = [
        f"{sys.executable} -m pip install --upgrade pip",
        f"{sys.executable} -m pip install -r requirements.txt"
    ]
    call_all(calls)


def run_tests():
    calls = [
        f"{sys.executable} -m unittest tests/unit_tests.py",
        f"{sys.executable} -m unittest tests/integration_tests.py"
    ]
    call_all(calls)


def check_coverage():
    calls = [
        f"{sys.executable} -m coverage run -m unittest tests/unit_tests.py",
        f"{sys.executable} -m coverage report -m"
    ]
    call_all(calls)


def run_flake8():
    calls = [
        f"{sys.executable} -m flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics",
        f"{sys.executable} -m flake8 src --count --max-complexity=10 --max-line-length=79 --statistics",
    ]
    call_all(calls)


def run_pylint():
    calls = [
        f"{sys.executable} -m pylint src --extension-pkg-whitelist=pydantic"
    ]
    call_all(calls)


def run_type_checking():
    calls = [
        f"{sys.executable} -m mypy src"
    ]
    call_all(calls)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError(f"Wrong number of arguments. Expected 2, found {len(sys.argv)}:\n"
                           f"{sys.argv}")
    command = sys.argv[1]
    if command == "install-depends":
        install_dependencies()
    elif command == "type-check":
        run_type_checking()
    elif command == "test":
        run_tests()
    elif command == "check-coverage":
        check_coverage()
    elif command == "flake8":
        run_flake8()
    elif command == "pylint":
        run_pylint()
    elif command == "all-checks":
        run_type_checking()
        run_tests()
        check_coverage()
        run_flake8()
        run_pylint()
    else:
        raise RuntimeError(f"Wrong command '{command}'")
