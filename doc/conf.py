#!/usr/bin/env python3
#
# tensorly documentation build configuration file
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
from datetime import datetime
import tensorly

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('sphinx_ext'))
sys.path.insert(0, "..")

# -- General configuration ------------------------------------------------


# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # 'sphinx.ext.imgmath',
    "sphinx.ext.mathjax",
    "numpydoc.numpydoc",
    "sphinx_gallery.gen_gallery",
]

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "../examples",
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
}

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# generate autosummary even if no references
autosummary_generate = True
autoclass_content = "class"
autodoc_default_flags = ["members", "inherited-members"]
autosummary_filename_map = {
    "tensorly.decomposition.parafac2": "parafac2-function",
    "tensorly.decomposition.tucker": "tucker-function",
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = 'tensorly'
year = datetime.now().year
copyright = f"2016 - {year}, TensorLy Developers"
author = "Jean Kossaifi"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '0.1'
version = '.'.join(tensorly.__version__.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = tensorly.__version__
# release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

html_theme = "tensorly_sphinx_theme"
html_theme_options = {
    "google_analytics": "G-3V91QCZR03",
    "github_url": "https://github.com/tensorly/tensorly",
    "searchbar_text": "Search in TensorLy",
    "nav_links": [
        ("Install", "installation"),
        ("User Guide", "user_guide/index"),
        ("API", "modules/api"),
        ("Examples", "auto_examples/index"),
        ("About Us", "about"),
    ],
    "nav_dropdowns": [
        (
            "Ecosystem",
            [
                ("TensorLy-Torch", "http://tensorly.org/torch"),
                ("TensorLy-Quantum", "http://tensorly.org/quantum"),
                ("TensorLy-Viz", "http://tensorly.org/viz"),
                ("Notebooks", "https://github.com/JeanKossaifi/tensorly-notebooks"),
            ],
        ),
    ],
}

# "<project> v<release> documentation" by default.
html_title = "TensorLy: Tensor Learning in Python"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "TensorLy"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo_url = '_static/logos/logo_tensorly.png'
html_logo = "_static/logos/logo_tensorly.png"

html_permalinks = False

html_show_sphinx = False

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "tensorly.tex",
        "Tensor operations in Python",
        "Jean Kossaifi",
        "manual",
    ),
]

latex_preamble = r"""
\usepackage{amsmath}\usepackage{amsfonts}
\setcounter{MaxMatrixCols}{20}
"""
# \setcounter{MaxMatrixCols}{20} corrects an ugly bug if you try to have a matrix of more than 10 elements or so

# We want the same for the html version:
imgmath_latex_preamble = latex_preamble

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False


latex_use_modindex = False
latex_domain_indices = False

# If true, show page references after internal links.
latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = "footnote"

trim_doctests_flags = True

# Documents to append as an appendix to all manuals.
# latex_appendices = []
latex_elements = {
    "classoptions": ",oneside",
    "babel": "\\usepackage[english]{babel}",
    # Get completely rid of index
    "printindex": "",
    "preamble": latex_preamble,
}

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "tensorly", "TensorLy Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "tensorly",
        "TensorLy Documentation",
        author,
        "tensorly",
        "Tensor Learning in Python",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
# epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True
