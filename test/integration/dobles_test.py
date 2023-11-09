import pytest
from dobles import allow, expect
from dobles.exceptions import UnallowedMethodCallError

from equals import any_string


class TestClass(object):
    def method(self, input):
        return input


def test_expect_passes():
    test_object = TestClass()
    expect(test_object).method.with_args(any_string.containing("bob"))

    test_object.method("bob barker")


def test_allow_can_fail():
    test_object = TestClass()
    allow(test_object).method.with_args(any_string.containing("todd"))

    with pytest.raises(UnallowedMethodCallError):
        test_object.method("bob barker")
