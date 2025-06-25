import os
import sys
import subprocess

sys.path.insert(0, os.path.abspath('../../src'))


def run_apidoc():
    """Generate API docs automatically on Read the Docs"""
    if os.environ.get("READTHEDOCS") == "True":
        docs_path = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(docs_path, "../.."))
        module = os.path.join(project_root, "src", "tree_height_analysis_57")
        output_path = docs_path
        subprocess.call([
            "sphinx-apidoc", "-f", "-o", output_path, module
        ])

run_apidoc()


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
