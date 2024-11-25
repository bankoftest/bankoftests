# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = 'bankoftests'
copyright = '2024, 题库之家'
author = 'bankoftests'

sys.path.insert(0, os.path.abspath('_extension'))
sys.path.insert(0, os.path.abspath('scripts'))


html_title = "题库之家｜BANK of TESTS"

html_baseurl = 'https://www.bankoftests.com/'
html_extra_path = ['robots.txt']
sitemap_url_scheme = "{lang}/{version}/{link}"
html_context = {
    "version": "latest",
    "languages": ["en", "zh-CN"],
    "meta_tags": [
        {"name": "title", "content": "题库之家"},
        {"name": "description", "content": "题库之家是一个在线题库，提供各种题库，包括驾照题库，移民题库，学习题库等。"},
        {"name": "robots", "content": "index, follow"},
        {"name": "keywords", "content": "题库, 驾照题库, 移民题库, 学习题库, 温哥华驾照题库, 加拿大驾照题库， BC驾照题库"},
    ],
}


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

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_js_files = ["custom.js", "language-switcher.js", "google_analytics.js"]


# Configure theme options
html_theme_options = {
    "secondary_sidebar_items": {
         "driver_test/ca/bc/**": [],
    },
    "navbar_end": ["lang-switcher"],  # Add a custom language switcher
    "footer_start": "",
    "footer_end": ["copyright"],
}

html_sidebars = {
    "driver_test/ca/bc/**": [],
}