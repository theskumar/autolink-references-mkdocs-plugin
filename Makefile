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
	pip install pytest
	pip install -e .
	pytest tests/

release: sdist
	twine check dist/*
	twine upload dist/*

release-test: sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

sdist: clean
	pip install twine wheel -U
	python setup.py sdist bdist_wheel
	ls -l dist
