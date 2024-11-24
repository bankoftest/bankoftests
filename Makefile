# Minimal makefile for Sphinx documentation
#

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build

# Source and build directories for each language
EN_SOURCEDIR  = docs/en/source
ZH_SOURCEDIR  = docs/zh-CN/source
EN_BUILDDIR   = build/en/html
ZH_BUILDDIR   = build/zh-CN/html

# Default target (build Chinese documentation)
html: html-zh

# Default target to open documentation (open Chinese version)
open: open-zh

# Help target
.PHONY: help clean html html-en html-zh open open-en open-zh

help:
	@echo "Available targets:"
	@echo "  make html        Build the default version (Chinese)"
	@echo "  make html-en     Build only the English version"
	@echo "  make html-zh     Build only the Chinese version"
	@echo "  make open        Open the default version (Chinese)"
	@echo "  make open-en     Open the English version index.html in the browser"
	@echo "  make open-zh     Open the Chinese version index.html in the browser"
	@echo "  make clean       Clean all build directories"

# Clean build directories
clean:
	rm -rf $(EN_BUILDDIR) $(ZH_BUILDDIR)

# Build English documentation
html-en:
	@$(SPHINXBUILD) -b html "$(EN_SOURCEDIR)" "$(EN_BUILDDIR)" $(SPHINXOPTS)

# Build Chinese documentation
html-zh:
	@$(SPHINXBUILD) -b html "$(ZH_SOURCEDIR)" "$(ZH_BUILDDIR)" $(SPHINXOPTS)

# Open English documentation index.html in the browser
open-en: html-en
	@xdg-open "$(EN_BUILDDIR)/index.html" 2>/dev/null || open "$(EN_BUILDDIR)/index.html" 2>/dev/null || echo "Open $(EN_BUILDDIR)/index.html manually"

# Open Chinese documentation index.html in the browser
open-zh: html-zh
	@xdg-open "$(ZH_BUILDDIR)/index.html" 2>/dev/null || open "$(ZH_BUILDDIR)/index.html" 2>/dev/null || echo "Open $(ZH_BUILDDIR)/index.html manually"