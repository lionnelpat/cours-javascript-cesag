SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = docs
BUILDDIR    = docs/_build

.PHONY: help html pdf epub clean

help:
	@echo "Commandes disponibles :"
	@echo "  make html   — Site HTML local"
	@echo "  make pdf    — PDF via LaTeX (nécessite texlive localement)"
	@echo "  make epub   — Fichier ePub"
	@echo "  make clean  — Suppression des fichiers générés"

html:
	$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

pdf:
	$(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

epub:
	$(SPHINXBUILD) -M epub $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

clean:
	$(SPHINXBUILD) -M clean $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
