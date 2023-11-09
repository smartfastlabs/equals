.PHONY: test
test: clean lint
	@py.test -s test

.PHONY: lint
lint:
	@flake8 --extend-ignore E501 equals test
	@black . 

.PHONY: clean
clean:
	@find . -type f -name '*.pyc' -exec rm {} ';'

.PHONY: bootstrap
bootstrap:
	@pip install poetry 
	@poetry install --with lint,test,docs
	@poetry shell

.PHONY: docs
docs:
	@$(MAKE) -C docs html
