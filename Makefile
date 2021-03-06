.PHONY: all install-dev test coverage cov test-all tox docs clean-pyc upload-docs

all: test

install-dev:
	pip install -q -e .

test: clean-pyc install-dev
	pytest

coverage: clean-pyc install-dev
	coverage run -m pytest
	coverage report
	coverage html

cov: coverage

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

init_db:
	flask init-db

run:
	flask run