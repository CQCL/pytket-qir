.PHONY: build tests install clean dev lint

all: install tests build

install:
	pip install .

dev:
	pip install -e .

lint:
	pre-commit run --all-files

tests:
	cd tests && pytest -x -v && cd -

build:
	python -m build --sdist --wheel -n

clean:
	rm -rf dist build *.egg-info
