# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bankoftests'
copyright = '2024, bankoftests'
author = 'bankoftests'

html_title = "题库之家 bankoftests.com"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# General configuration
# General configuration
extensions = [
    'myst_parser',
    'sphinx_design',
]

# MyST settings
myst_enable_extensions = [
    "colon_fence",
    "substitution",
    "deflist",
    "html_image",
    "smartquotes",
    "fieldlist",  # Add this
    "tasklist",   # Add this
    "attrs_inline" # Add this for inline attributes
]


templates_path = ['_templates']
exclude_patterns = []

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_js_files = ["custom.js", "language-switcher.js"]


# Configure theme options
html_theme_options = {
    "secondary_sidebar_items": {
         "driver_test/ca/bc/**": [],
    },
    "navbar_end": ["lang-switcher"],  # Add a custom language switcher

}

html_sidebars = {
    "driver_test/ca/bc/**": [],
}