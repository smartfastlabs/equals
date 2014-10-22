from doubles import expect, allow
from doubles.exceptions import UnallowedMethodCallError
import pytest

from fuzzy_match import contains


class TestClass(object):
    def method(self, input):
        return input


def test_expect_passes():
    test_object = TestClass()
    expect(test_object).method.with_args(contains('bob'))

    test_object.method('bob barker')


def test_allow_can_fail():
    test_object = TestClass()
    allow(test_object).method.with_args(contains('foobar'))

    with pytest.raises(UnallowedMethodCallError):
        test_object.method('bob barker')
