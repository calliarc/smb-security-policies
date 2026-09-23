# Convenience targets. Run `make help` for a list.
CONFIG ?= company.yml
PYTHON ?= python3

.PHONY: help build markdown test lint clean

help:
	@echo "make build     Fill placeholders from $(CONFIG) and export MD/DOCX/PDF to dist/"
	@echo "make markdown  Same, Markdown only"
	@echo "make test      Run unit tests"
	@echo "make lint      Run markdownlint (needs Node.js)"
	@echo "make clean     Remove dist/"
	@echo "Override the config with: make build CONFIG=path/to/company.yml"

build:
	$(PYTHON) scripts/build.py --config $(CONFIG) --combined

markdown:
	$(PYTHON) scripts/build.py --config $(CONFIG) --formats md --combined

test:
	$(PYTHON) -m unittest discover -s tests -v

lint:
	npx --yes markdownlint-cli2@0.23.3

clean:
	rm -rf dist
