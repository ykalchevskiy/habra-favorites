# On Windows:
# Set-ExecutionPolicy Unrestricted -Scope Process

.all := run

.PHONY: build
build:
	pip install wheel
	python setup.py sdist bdist_wheel

.PHONY: upload
upload:
	pip install twine
	twine upload --repository pypi .\dist\*

.PHONY: run
run:
	python -m habra_favorites.main ykalchevskiy
