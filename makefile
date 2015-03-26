.PHONY: install clean test

install:
	python setup.py develop
	pip install -r tests/requirements.txt

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete
	-rm -rf dist *.egg-info

test:
	python setup.py test
