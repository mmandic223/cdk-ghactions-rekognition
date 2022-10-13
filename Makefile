install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C,W0611,W0612 stacks/cdk_app_stack.py

all: install lint test