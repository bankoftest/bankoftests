# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = 'bankoftests'
author = 'bankoftests'

sys.path.insert(0, os.path.abspath('_extension'))
sys.path.insert(0, os.path.abspath('scripts'))

html_baseurl = 'https://www.bankoftests.com/'
html_extra_path = ['robots.txt']
sitemap_url_scheme = "{lang}/{version}/{link}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# General configuration
# General configuration
extensions = [
    'myst_parser',
    'sphinx_design',
    'gallery_directive',
    'component_directive',
    'sphinx_sitemap',

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

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_js_files = ["custom.js", "language-switcher.js", "google_analytics.js"]
html_favicon = "_static/favicon.ico"

html_sidebars = {
    "driver_test/ca/bc/**": [],
}

# Configure theme options
html_theme_options = {
    "secondary_sidebar_items": {
         "driver_test/ca/bc/**": [],
    },
    "navbar_end": ["lang-switcher"],  # Add a custom language switcher
    "footer_start": "",
    "footer_end": ["copyright"],
    "logo": {
        "image_light": "_static/logo-light.svg",
        "image_dark": "_static/logo-dark.svg",
        "text": "BANK of TESTS",  
        "alt_text": "BANK of TESTS Logo",  
    }
}

language = 'en'
copyright = '2024, BANK of TESTS'
html_title = "题库之家｜BANK of TESTS"
html_context = {
    "version": "latest",
    "languages": ["en", "zh-CN"],
    "meta_tags": [
        {"name": "title", "content": "BANK of TESTS"},
        {"name": "description", "content": "BANK of TESTS is an online question bank that provides various question banks, including driver's license question"},
        {"name": "robots", "content": "index, follow"},
        {"name": "keywords", "content": "question bank, driver's license question"},
    ],
}
