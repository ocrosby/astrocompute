"""
Invoke build tasks for the astrocompute project.
"""

import os
import re
import sys
from typing import Dict, Optional

from invoke import Context, task


@task
def clean_coverage(c: Context) -> None:
    """Remove all coverage files."""
    print("Cleaning up coverage files ...")
    c.run("find . -name '.coverage' -delete")
    c.run("find . -name 'coverage.xml' -delete")


@task(aliases=["c"])
def clean(c: Context) -> None:
    """Remove transient build artifacts."""
    c.run("echo 'Cleaning up ...'")

    c.run("find astrocompute tests -name 'coverage.xml' -delete")
    c.run("find astrocompute tests -name 'junit.xml' -delete")
    c.run("find astrocompute tests -name 'requests.json' -delete")
    c.run("find astrocompute tests -name '*.log' -delete")
    c.run("find astrocompute tests -name '.coverage' -delete")
    c.run(
        "find astrocompute tests -name '.pytest_cache' -type d -exec rm -r {} +"
    )
    c.run("find astrocompute tests -name 'logs' -type d -exec rm -r {} +")
    c.run("find astrocompute tests -name '*.egg-info' -type d -exec rm -r {} +")
    c.run("find astrocompute tests -name 'htmlReport' -type d -exec rm -r {} +")
    c.run("find astrocompute tests -name 'htmlcov' -type d -exec rm -r {} +")

    c.run(
        "rm -f .coverage output.json output.txt *.log junit.xml coverage.xml app.log"
    )
    c.run("rm -rf logs/ dist/ build/ *.egg-info/ htmlcov/ htmlReport/")


@task(aliases=["f"])
def format_code(c: Context):
    """Format the codebase using black."""
    print("Formatting code with black...")
    c.run("black .")
    c.run("isort .")
    print("Code formatting complete.")


@task(aliases=["l"], pre=[format_code])
def lint(c: Context):
    """Run pylint and flake8 on the codebase."""
    print("Running pylint...")
    c.run("pylint astrocompute")
    print("Running flake8...")
    c.run("flake8 astrocompute")


@task(aliases=["cl"])
def commitlint(c: Context):
    """Check the most recent commit message against commitlint."""
    print("Running commitlint...")
    c.run("git log -1 --pretty=%B | npx commitlint")


@task(pre=[clean], aliases=["t"])
def test(c: Context):
    """Run pytest on the tests/ directory."""
    print("Running pytest...")
    c.run("pytest tests/")


@task(aliases=["v"])
def coverage(c: Context) -> None:
    """Run tests with coverage."""
    c.run("echo 'Running tests with coverage ...'")
    c.run("pytest --cov=lambda_kit --cov-report=term-missing tests/")
    c.run("coverage report")
    c.run("coverage xml")


@task(pre=[clean], aliases=["w"])
def watch(c: Context):
    """Run pytest-watch on the tests/ directory."""
    print("Running pytest-watch...")
    c.run("ptw -- --cov=astrocompute --cov-report=term-missing")


@task(
    pre=[clean],
    aliases=["i"],
    help={"prod": "Install production dependencies."},
)
def install(c: Context, prod: bool = False):
    """Install dependencies."""
    c.run('pip install --upgrade "pip>=21.3"')
    c.run("pip install flit")

    if prod:
        print("Installing production dependencies ...")
        c.run("flit install --deps production")
    else:
        print("Installing development dependencies...")
        c.run("flit install --symlink")  # install package in editable mode


@task(aliases=["n"])
def install_node(c: Context):
    """Install the Node.js dependencies."""
    print("Installing Node.js dependencies...")
    c.run("npm install")
    c.run("npm install --save-dev @commitlint/{config-conventional,cli}")


@task(aliases=["b"])
def build(c: Context):
    """Build the package and prepare it for deployment to Artifactory."""
    print("Building the package...")

    # Build a source distribution
    c.run("python3 -m build --sdist")

    # Build a wheel
    c.run("python3 -m build --wheel")

    print("Build complete. The distribution files are in the dist/ directory.")


@task(aliases=["d"])
def deploy(c: Context, repository_url: str, username: str, password: str):
    """Deploy the package to Artifactory."""
    print("Deploying the package...")
    c.run(
        f"python -m twine upload --repository-url {repository_url} "
        f"--non-interactive --verbose --username {username} "
        f"--password {password} dist/*"
    )
    print("Deployment complete.")


@task(aliases=["r"])
def release(c: Context):
    """Run semantic-release to update version numbers and create a new release."""
    print("Running semantic-release...")
    c.run("semantic-release -vv publish")


@task(aliases=["cc"])
def check_complexity(c: Context, max_complexity: int = 12) -> None:
    """
    Check the cyclomatic complexity of the code.
    Fail if it exceeds the max_complexity.

    :param c: The context instance (automatically passed by invoke).
    :param max_complexity: The maximum allowed cyclomatic complexity.
    """
    c.run("echo 'Checking cyclomatic complexity ...'")
    result = c.run("radon cc astrocompute -s", hide=True)

    if result is None:
        print("No output from radon.")
        sys.exit(1)

    output = result.stdout
    results = parse_radon_output(output)
    display_radon_results(results)
    max_score = get_max_score(results)

    if max_score > max_complexity:
        print(
            f"\nFAILED - Maximum complexity {max_complexity} exceeded by {max_score}\n"
        )

        print("\nFunctions with complexity greater than the maximum allowed:")
        display_exceeded_complexity(results, max_complexity)

        sys.exit(1)

    print(f"\nMaximum complexity not exceeded: {max_score}\n")

    sys.exit(0)


def get_max_score(results: Dict[Optional[str], any]) -> int:
    max_score = 0
    for _, functions in results.items():
        for function in functions:
            if function["score"] > max_score:
                max_score = function["score"]
    return max_score


def display_exceeded_complexity(
    results: Dict[Optional[str], any], max_complexity: int
) -> None:
    print("File\tFunction\tComplexity\tScore")
    for file, functions in results.items():
        for function in functions:
            if function["score"] > max_complexity:
                print(
                    f"{file}\t{function['name']}\t{function['complexity']}\t{function['score']}"
                )


def display_radon_results(results: Dict[Optional[str], any]) -> None:
    for file, functions in results.items():
        print(f"\nFile: {file}")
        for function in functions:
            print(
                f"\tFunction: {function['name']}, ",
                f"Complexity: {function['complexity']}, ",
                f"Score: {function['score']}",
            )


def parse_radon_output(output: str) -> Dict[Optional[str], any]:
    # Remove the escape sequence
    output = output.replace("\x1b[0m", "")

    # Regular expression to match the lines with complexity information
    pattern = re.compile(
        r"^\s*(\w)\s(\d+:\d+)\s([\w_]+)\s-\s([A-F])\s\((\d+)\)$"
    )

    # Dictionary to store the results
    results: Dict[Optional[str], any] = {}

    # Split the output into lines
    output = output.strip()
    lines = output.splitlines()

    current_file = None
    for line in lines:
        try:
            # Check if the line is a file name
            if not line.startswith(" "):
                current_file = line.strip()
                results[current_file] = []
            else:
                # Match the line with the pattern
                match = pattern.match(line)
                if match:
                    function_info = {
                        "type": match.group(1),
                        "location": match.group(2),
                        "name": match.group(3),
                        "complexity": match.group(4),
                        "score": int(match.group(5)),
                    }
                    results[current_file].append(function_info)
        except ValueError as e:
            print(f"Error parsing line: '{line}'")
            print(e)

    return results
