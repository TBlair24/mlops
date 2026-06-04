install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py

format:
	black hello.py

test:
	python -m pytest -vv --cov=hello test_hello.py

loadtest:
	bash run_loadtest.sh

all: install lint format test