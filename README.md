# equals: Enhanced Equality Testing for Python

[![PyPI version](https://badge.fury.io/py/equals.svg)](https://badge.fury.io/py/equals)
[![Documentation Status](https://readthedocs.org/projects/equals/badge/?version=latest)](https://equals.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/smartfastlabs/equals/badge.svg?branch=master)](https://coveralls.io/github/smartfastlabs/equals?branch=master)

`equals` is a Python library that provides flexible equality assertions for testing. Think of it as a more powerful version of `Mock.Any` that gives you fine-grained control over how objects are compared.

## Why Use equals?

Sometimes in testing, you need to verify that objects match certain patterns rather than being exactly equal. For example, you might want to:
- Check if a list contains specific elements, regardless of their order
- Verify that a string contains a substring
- Ensure a number falls within a specific range
- Validate dictionary contents without requiring an exact match

`equals` makes these comparisons easy and expressive.

## Installation

```bash
pip install equals
```

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

## Features

The `equals` library provides a rich set of fuzzy matching capabilities that go beyond exact equality comparisons. Each matcher type (string, number, dictionary, etc.) implements its own set of flexible matching rules, allowing you to write tests that focus on the important aspects of your data while ignoring irrelevant details. These matchers can be combined and chained to create sophisticated matching patterns that make your tests both robust and maintainable.

### String Matching

```python
from equals import any_string

# Match strings containing text
assert any_string.containing('abc') == '123 abc 456'

# Match string prefixes
assert any_string.starting_with('abc') == 'abcdef'

# Match string suffixes
assert any_string.ending_with('abc') == '123abc'

# Match regex patterns
assert any_string.matching('^abc$') == 'abc'
```

### Number Comparisons

```python
from equals import any_number

assert any_number.less_than(5) == 4
assert any_number.less_than_or_equal_to(5) == 5
assert any_number.greater_than(4) == 5
assert any_number.between(1, 3) == 2
```

### Dictionary Validation

```python
from equals import any_dict

# Check for key-value pairs
assert any_dict.containing(1, 2) == {1: 2, 2: 3, 4: 5}

# Check using keyword arguments
assert any_dict.containing(foo='bar') == {
    'foo': 'bar',
    'bob': 'barker'
}

# Verify absence of keys
assert any_dict.not_containing(1, foo=5) == {'foo': 3, 4: 5}
```

### Iterable Operations

```python
from equals import any_iterable

# Check for elements
assert any_iterable.containing(1, 2, 3) == [1, 2, 3, 4, 5]

# Check for exact elements (order-independent)
assert any_iterable.containing_only(1, 2, 3) == [2, 3, 1]

# Check for absence of elements
assert any_iterable.not_containing(1, 2) == [3, 4]

# Check length
assert any_iterable.with_length(2) == [3, 4]
```

### Object Matching

```python
from equals import anything, instance_of

# Match any value
assert anything == None
assert anything == True
assert anything == {'key': 'value'}

# Match by truth value
assert anything_true == 'non-empty string'
assert anything_false == ''

# Match by type
assert instance_of(dict) == {}

# Match by attributes
assert anything.with_attrs(foo='bar') == obj_with_foo_bar
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
