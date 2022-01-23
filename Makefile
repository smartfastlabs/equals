.PHONY: test
test: clean lint
	@py.test -s test

.PHONY: lint
lint:
	@flake8 equals test

.PHONY: clean
clean:
	@find . -type f -name '*.pyc' -exec rm {} ';'

.PHONY: bootstrap
bootstrap:
	@pip3 install -r requirements-dev.txt
	@pip3 install -e .
