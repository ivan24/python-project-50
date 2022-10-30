install:
	poetry install

test:
	poetry run pytest

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

coverage:
	poetry run pytest --cov=gendiff

.PHONY: install test test-coverage gendiff lint selfcheck check build publish coverage