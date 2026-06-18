# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        Configuration file for the Sphinx documentation builder.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -- Project information -----------------------------------------------------

project   = 'RECOWA'
copyright = '2026, J. Pianezze'
author    = 'J. Pianezze'
release   = '0.0'
version   = '0.0.0'

# --------------------------------------------------------
#   Get and modify install.md
# --------------------------------------------------------

import urllib.request
import os
import re

# ------- get laptop_joris files
url_install_laptop_joris = "https://raw.githubusercontent.com/JorisPianezze/models_recowa/refs/heads/master/environments/laptop_joris/"
urllib.request.urlretrieve(url_install_laptop_joris+"check_tree.rst", "installation/check_tree_laptop_joris.rst")
urllib.request.urlretrieve(url_install_laptop_joris+"compilation_libraries/compile.rst", "compilation/compile_libraries_laptop_joris.rst")
urllib.request.urlretrieve(url_install_laptop_joris+"compilation_oasis/compile.rst", "compilation/compile_oasis_laptop_joris.rst")

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.mermaid',
    'sphinx_substitution_extensions',
    'sphinx_treeview',
    'sphinx_togglebutton',
    'sphinx_design',
    'myst_parser'
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

bibtex_bibfiles        = ['references.bib']
bibtex_default_style   = 'unsrt'
bibtex_reference_style = 'author_year'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme       = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files   = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'

