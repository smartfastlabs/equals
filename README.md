# equals: Enhanced Equality Testing for Python

[![PyPI version](https://badge.fury.io/py/equals.svg)](https://badge.fury.io/py/equals)
[![Documentation Status](https://readthedocs.org/projects/equals/badge/?version=latest)](https://equals.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/smartfastlabs/equals/badge.svg?branch=master)](https://coveralls.io/github/smartfastlabs/equals?branch=master)

`equals` is a Python library that provides flexible equality assertions for testing. Think of it as a more powerful version of `Mock.Any` that gives you fine-grained control over how objects are compared.

## Why Use equals?

When writing tests with mocks and stubs, exact matching can make tests brittle and hard to maintain. Often, you care about certain properties of an object but not others. For example:

- In integration tests, timestamps or UUIDs might change between test runs
- When mocking API responses, you may only care about specific fields
- Testing event handlers where message format may evolve over time
- Verifying call arguments where some data is non-deterministic

`equals` helps you write more maintainable tests by focusing on the properties that matter for your test cases, making your test suite more robust and easier to maintain.

The `equals` library provides a rich set of fuzzy matching capabilities that go beyond exact equality comparisons. Each matcher type (string, number, dictionary, etc.) implements its own set of flexible matching rules, allowing you to write tests that focus on the important aspects of your data while ignoring irrelevant details. These matchers can be combined and chained to create sophisticated matching patterns that make your tests both robust and maintainable.

## Quick Examples

The `equals` library enables flexible matching in tests through partial equality checks:
- Match dictionaries by key presence or content
- Match strings by pattern or content
- Chain multiple conditions for complex matching

### With Mock and pytest

```python
import pytest
from unittest.mock import Mock  # Using unittest.mock instead of mock package
from equals import any_dict, any_string

def test_mock_multiple_calls():
    # Arrange
    mock_service = Mock()
    
    # Act
    mock_service.update({'name': 'bob'})
    mock_service.update({'name': 'alice'})
    
    # Assert
    assert mock_service.update.call_count == 2
    mock_service.update.assert_any_call(any_dict.containing(name=any_string))
```

### With dobles and pytest

```python
import pytest
from dobles import expect
from equals import any_string

class UserService:
    def validate_email(self, email: str) -> bool:
        return '@' in email

@pytest.fixture
def user_service():
    return UserService()

def test_email_validation(user_service):
    # Arrange
    expect(user_service).validate_email.with_args(
        any_string.containing('@').and_containing('.')
    ).and_return(True)
    
    # Act & Assert
    assert user_service.validate_email('test@example.com')
```

## Fuzzy Matching Capabilities

### String Matching
```python
from equals import any_string

assert any_string.containing('abc') == '123 abc 456'     # Substring
assert any_string.starting_with('abc') == 'abcdef'       # Prefix
assert any_string.ending_with('abc') == '123abc'         # Suffix
assert any_string.matching('^abc$') == 'abc'             # Regex
```

### Number Comparisons
```python
from equals import any_number

assert any_number.less_than(5) == 4               # Less than
assert any_number.between(1, 3) == 2              # Range
assert any_number.greater_than(4) == 5            # Greater than
```

### Dictionary Validation
```python
from equals import any_dict

assert any_dict.containing(foo='bar') == {'foo': 'bar', 'other': 'value'}
assert any_dict.not_containing(foo=5) == {'foo': 3, 'bar': 5}
```

### Iterable Operations
```python
from equals import any_iterable

assert any_iterable.containing(1, 2) == [1, 2, 3]        # Contains elements
assert any_iterable.containing_only(1, 2) == [2, 1]      # Exact elements, any order
assert any_iterable.with_length(2) == [3, 4]             # Length check
```

### Object Matching
```python
from equals import anything, instance_of

assert anything == 'any value'                           # Match anything
assert instance_of(dict) == {}                          # Type check
assert anything.with_attrs(foo='bar') == obj            # Attribute check
```

## Installation

```bash
pip install equals
```

## Development

The source code is available on [GitHub](https://github.com/smartfastlabs/equals).

### Getting Started

```bash
# Install dependencies
make bootstrap

# Run tests
make test

# Build documentation
make docs
```

## Documentation

Full documentation is available at [equals.readthedocs.org](http://equals.readthedocs.org/en/latest/).

## License

[MIT License](http://opensource.org/licenses/MIT)
