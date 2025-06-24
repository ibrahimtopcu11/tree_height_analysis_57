import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Tree Height Analysis'
author = 'Ibrahim Topcu'
copyright = '2025, Ibrahim Topcu'

from tree_height_analysis_57 import __version__ as version
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
language = 'en'

html_theme = 'furo'
html_static_path = ['_static']

autodoc_typehints = "description"
napoleon_use_param = True
napoleon_use_rtype = False
