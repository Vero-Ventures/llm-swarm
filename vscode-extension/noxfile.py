import json
import os
import glob
import pathlib
import urllib.request as url_lib
from typing import List
import nox  # pylint: disable=import-error


def _install_bundle(session: nox.Session) -> None:
    session.install(
        "-t",
        "./bundled/libs",
        "--no-cache-dir",
        "--implementation",
        "py",
        "--no-deps",
        "--upgrade",
        "-r",
        "./requirements.txt",
    )


def _check_files(names: List[str]) -> None:
    root_dir = pathlib.Path(__file__).parent
    for name in names:
        file_path = root_dir / name
        lines: List[str] = file_path.read_text().splitlines()
        if any(line for line in lines if line.startswith("# TODO:")):
            raise Exception(f"Please update {os.fspath(file_path)}.")


def _update_pip_packages(session: nox.Session) -> None:
    session.run(
        "pip-compile",
        "--generate-hashes",
        "--resolver=backtracking",
        "--upgrade",
        "./requirements.in",
    )
    session.run(
        "pip-compile",
        "--generate-hashes",
        "--resolver=backtracking",
        "--upgrade",
        "./src/test/python_tests/requirements.in",
    )


def _get_package_data(package):
    json_uri = f"https://registry.npmjs.org/{package}"
    with url_lib.urlopen(json_uri) as response:
        return json.loads(response.read())


def _update_npm_packages(session: nox.Session) -> None:
    pinned = {
        "vscode-languageclient",
        "@types/vscode",
        "@types/node",
    }
    package_json_path = pathlib.Path(__file__).parent / "package.json"
    package_json = json.loads(package_json_path.read_text(encoding="utf-8"))

    for package in package_json["dependencies"]:
        if package not in pinned:
            data = _get_package_data(package)
            latest = "^" + data["dist-tags"]["latest"]
            package_json["dependencies"][package] = latest

    for package in package_json["devDependencies"]:
        if package not in pinned:
            data = _get_package_data(package)
            latest = "^" + data["dist-tags"]["latest"]
            package_json["devDependencies"][package] = latest

    # Ensure engine matches the package
    if (
        package_json["engines"]["vscode"]
        != package_json["devDependencies"]["@types/vscode"]
    ):
        print(
            "Please check VS Code engine version and @types/vscode version in package.json."
        )

    new_package_json = json.dumps(package_json, indent=4)
    if not new_package_json.endswith("\n"):
        new_package_json += "\n"
    package_json_path.write_text(new_package_json, encoding="utf-8")
    session.run("npm", "install", external=True)


def _setup_template_environment(session: nox.Session) -> None:
    session.install("wheel", "pip-tools")
    session.run(
        "pip-compile",
        "--generate-hashes",
        "--resolver=backtracking",
        "--upgrade",
        "./requirements.in",
    )
    session.run(
        "pip-compile",
        "--generate-hashes",
        "--resolver=backtracking",
        "--upgrade",
        "./src/test/python_tests/requirements.in",
    )
    _install_bundle(session)


def _get_latest_version_path(pattern):
    files = glob.glob(pattern)
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0] if files else None


@nox.session(python="3.12")
def setup(session: nox.Session) -> None:
    """Sets up the template for development."""

    # Ensure custom package is built
    package_dir = "bundled/llm-swarm-build/"
    latest_file_path = _get_latest_version_path(f"{package_dir}llm_swarm-*.tar.gz")
    if not latest_file_path:
        raise Exception(f"llm_swarm package not found in {package_dir}.")

    # Ensure pip is installed and upgraded
    session.run("python", "-m", "ensurepip", external=True)
    session.run("pip", "install", "--upgrade", "pip", external=True)

    _setup_template_environment(session)

    # Install our custom package in the bundled/libs directory
    session.run(
        "pip",
        "install",
        "--target=./bundled/libs",
        latest_file_path,
        external=True,
    )

    # Debug: Print the sys.path to verify installation paths
    session.run("python", "-c", "import sys; print(sys.path)", external=True)

    # Debug: Print the installed packages to verify installation
    session.run("pip", "list", external=True)


@nox.session(python="3.12")
def tests(session: nox.Session) -> None:
    """Runs all the tests for the extension."""
    session.install("-r", "src/test/python_tests/requirements.txt")
    session.run("pytest", "src/test/python_tests")


@nox.session(python="3.12")
def lint(session: nox.Session) -> None:
    """Runs linter and formatter checks on python files."""
    session.install("-r", "./requirements.txt")
    session.install("-r", "src/test/python_tests/requirements.txt")

    session.install("pylint")
    session.run("pylint", "-d", "W0511", "./bundled/tool")
    session.run(
        "pylint",
        "-d",
        "W0511",
        "--ignore=./src/test/python_tests/test_data",
        "./src/test/python_tests",
    )
    session.run("pylint", "-d", "W0511", "noxfile.py")

    # check formatting using black
    session.install("black")
    session.run("black", "--check", "./bundled/tool")
    session.run("black", "--check", "./src/test/python_tests")
    session.run("black", "--check", "noxfile.py")

    # check import sorting using isort
    session.install("isort")
    session.run("isort", "--check", "./bundled/tool")
    session.run("isort", "--check", "./src/test/python_tests")
    session.run("isort", "--check", "noxfile.py")

    # check typescript code
    session.run("npm", "run", "lint", external=True)


@nox.session(python="3.12")
def build_package(session: nox.Session) -> None:
    """Builds VSIX package for publishing."""
    _check_files(["README.md", "LICENSE", "SECURITY.md", "SUPPORT.md"])
    _setup_template_environment(session)
    session.run("npm", "install", external=True)
    session.run("npm", "run", "vsce-package", external=True)


@nox.session(python="3.12")
def update_packages(session: nox.Session) -> None:
    """Update pip and npm packages."""
    session.install("wheel", "pip-tools")
    _update_pip_packages(session)
    _update_npm_packages(session)
