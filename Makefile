install:
	pip install -r requirements-azure.txt

test:
	python -m pytest -vv te.py


lint:
	pylint --disable=R,C example.py

all: install lint test
