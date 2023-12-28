.PHONY: clean-pyc clean-build

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr src/*.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

test:
	rye run pytest tests/

release: build
	rye publish

release-test: build
	rye publish --repository testpypi --repository-url https://test.pypi.org/legacy/

build: clean
	rye build

install:
	rye sync
