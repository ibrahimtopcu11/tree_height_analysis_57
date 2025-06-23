# Configuration file for the Sphinx documentation builder.

import os
import sys
from pathlib import Path

# -- Path setup -----------------------------------------------------------
# Add project root to sys.path for autodoc to find modules
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information --------------------------------------------------
project = 'Tree Height Analysis'
author = 'Ibrahim Topcu'
copyright = '2025, Ibrahim Topcu'
release = '0.1.0'

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',             # Automatically include docstrings
    'sphinx.ext.napoleon',            # Google/NumPy style docstrings
    'sphinx_autodoc_typehints',       # Show type hints in documentation
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
language = 'en'

# -- Options for HTML output ----------------------------------------------
html_theme = 'furo'                  # Modern, responsive theme
html_static_path = ['_static']

# -- Type hints and docstring formatting ----------------------------------
autodoc_typehints = "description"
napoleon_use_param = True
napoleon_use_rtype = False
