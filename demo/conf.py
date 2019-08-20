# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Material Sphinx Demo'
html_short_title = 'Material Demo'

copyright = '2019, Kevin Sheppard'
author = 'Kevin Sheppard'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'numpydoc',
              'sphinx.ext.doctest',
              'sphinx.ext.extlinks',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              # One of mathjax or imgmath
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              # 'sphinx.ext.autosummary',
              'sphinx.ext.inheritance_diagram',
              'matplotlib.sphinxext.plot_directive',
              'IPython.sphinxext.ipython_console_highlighting',
              'IPython.sphinxext.ipython_directive',
              ]

autosummary_generate = True
autoclass_content = 'class'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = True
html_sidebars = {
    '**': ['logo-text.html',
           'globaltoc.html',
           'localtoc.html',
           'searchbox.html']
}

import material_sphinx_theme

extensions.append("material_sphinx_theme")
html_theme_path = material_sphinx_theme.html_theme_path()
html_context = material_sphinx_theme.get_html_context()
html_theme = 'material_sphinx_theme'

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "http://my-site.com/docs/"
}

language = 'en'
html_last_updated_fmt = ''
