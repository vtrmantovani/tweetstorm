clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.pytest_cache" | xargs rm -rf
	@find . -name "*.DS_Store" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f coverage.xml

test: clean
	@py.test -xs tests/

coverage: clean
	@py.test -xs --cov tweetstorm/ --cov-report=term-missing tests/

requirements-dev:
	pip install -r requirements-dev.txt

lint: flake8 check-python-import

flake8:
	@flake8 --show-source .

check-python-import:
	@isort --check

isort:
	@isort