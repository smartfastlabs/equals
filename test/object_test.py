from collections import namedtuple

from equals import (
    anything,
    anything_true,
    anything_false,
    instance_of,
)

Dummy = namedtuple('Dummy', ['foo', 'bob'])


class TestAnything(object):
    def test_equals_none(self):
        assert anything == None  # noqa

    def test_equals_true(self):
        assert anything == True  # noqa

    def test_order_of_test_does_not_matter(self):
        assert True == anything  # noqa


class TestAnythingTrue(object):
    def test_equals_true(self):
        assert anything_true == True  # noqa

    def test_equals_a_string(self):
        assert anything_true == 'test'

    def test_does_not_equal_false(self):
        assert not anything_true == False  # noqa

    def test_order_of_test_does_not_matter(self):
        assert not False == anything_true  # noqa


class TestAnythingFalse(object):
    def test_equalsfalse(self):
        assert anything_false == False  # noqa

    def test_does_not_equal_true(self):
        assert not anything_false == True  # noqa

    def test_order_of_test_does_not_matter(self):
        assert False == anything_false  # noqa


class TestAnyInstance(object):
    def test_equals_same_type(self):
        assert instance_of(dict) == {}

    def test_equals_same_type_with_multiple_types(self):
        assert instance_of(dict, tuple) == (1, 2)

    def test_order_of_test_does_not_matter(self):
        assert object() == instance_of(object)


class TestWithAttrs(object):
    def test_equals_instance_with_all_attrs(self):
        matcher = anything.with_attrs(foo='bar', bob='barker')
        assert matcher == Dummy('bar', 'barker')

    def test_does_not_equal_instance_with_all_attrs_but_diff_values(self):
        matcher = anything.with_attrs(foo='bar', bob='bar')
        assert not matcher == Dummy('bar', 'barker')

    def test_does_not_equal_instance_without_all_attrs(self):
        matcher = anything.with_attrs(foo='bar', cat='barker')
        assert not matcher == Dummy('bar', 'barker')

    def test_equals_instance_of_correct_type(self):
        matcher = instance_of(Dummy).with_attrs(foo='bar', bob='barker')
        assert matcher == Dummy('bar', 'barker')

    def test_does_not_equal_instance_of_wrong_type(self):
        matcher = instance_of(dict).with_attrs(foo='bar', bob='barker')
        assert not matcher == Dummy('bar', 'barker')

    def test_order_of_test_does_not_matter(self):
        matcher = anything.with_attrs(foo='bar', bob='barker')
        assert Dummy('bar', 'barker') == matcher
