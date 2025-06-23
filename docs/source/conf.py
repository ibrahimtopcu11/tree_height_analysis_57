# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path

# -- Path setup -----------------------------------------------------------
sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information --------------------------------------------------
project = 'Tree Height Analysis'
author = 'Ibrahim Topcu'
copyright = '2025, Ibrahim Topcu'

version = "0.1.23"
release = "0.1.24"

# -- General configuration ------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
language = 'en'

# -- Options for HTML output ----------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']

# -- Type hints and docstring formatting ----------------------------------
autodoc_typehints = "description"
napoleon_use_param = True
napoleon_use_rtype = False
