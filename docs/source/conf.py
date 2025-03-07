# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "astrocompute"
copyright = "2025, Omar Crosby"
author = "Omar Crosby"
release = "1.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Auto-generate docs from docstrings
    "sphinx.ext.napoleon",  # Support for NumPy & Google docstring styles
    "sphinx.ext.viewcode",  # Adds links to source code
    "sphinx_autodoc_typehints",  # Type hint support
]

templates_path = ["sphinx_rtd_theme"]
exclude_patterns = [
    "tests/*",
    "tasks.py",
    "update_version.py",
]  # Exclude tests from documentation


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
