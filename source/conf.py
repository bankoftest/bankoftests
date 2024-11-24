# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bankoftests'
copyright = '2024, bankoftests'
author = 'bankoftests'

html_title = "tests"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh-CN'
locale_dirs = ['../locales/']  # Path to your translation files
gettext_compact = False  # Optional: Creates separate .po files for each RST

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_js_files = ["custom.js", "language-switcher.js"]


# Configure theme options
html_theme_options = {
    "secondary_sidebar_items": {
         "math_test/elementary_school/grade_one/**": [], 
         "driver_test/ca/bc/**": [],
    },
    "navbar_end": ["lang-switcher"],  # Add a custom language switcher

}

html_sidebars = {
    "math_test/elementary_school/grade_one/**": [], 
    "driver_test/ca/bc/**": [],
}