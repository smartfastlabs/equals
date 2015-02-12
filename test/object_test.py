from collections import namedtuple
import re

from equals import (
    anything,
    anything_true,
    anything_false,
    instance_of,
)

Dummy = namedtuple('Dummy', ['foo', 'bob'])


class NeverEquals(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return False


class TestAnything(object):
    def test_equals_none(self):
        assert anything == None  # noqa

    def test_equals_true(self):
        assert anything == True  # noqa

    def test_order_of_test_does_not_matter(self):
        assert True == anything  # noqa

    def test_with_constraint_unsupported_type(self):
        assert not anything.containing(1) == 1

    def test_representation(self):
        assert repr(anything) == '<Equals Any object>'
        assert str(anything) == 'Any object'

    def test_anything_equals_anything(self):
        assert anything == anything


class TestAnythingTrue(object):
    def test_equals_true(self):
        assert anything_true == True  # noqa

    def test_equals_a_string(self):
        assert anything_true == 'test'

    def test_does_not_equal_false(self):
        assert not anything_true == False  # noqa

    def test_order_of_test_does_not_matter(self):
        assert not False == anything_true  # noqa

    def test_representation(self):
        assert repr(anything_true) == '<Equals Any object that is true>'
        assert str(anything_true) == 'Any object that is true'


class TestAnythingFalse(object):
    def test_equalsfalse(self):
        assert anything_false == False  # noqa

    def test_does_not_equal_true(self):
        assert not anything_false == True  # noqa

    def test_order_of_test_does_not_matter(self):
        assert False == anything_false  # noqa

    def test_representation(self):
        assert repr(anything_false) == '<Equals Any object that is false>'
        assert str(anything_false) == 'Any object that is false'


class TestAnyInstance(object):
    def test_equals_same_type(self):
        assert instance_of(dict) == {}

    def test_equals_same_type_with_multiple_types(self):
        assert instance_of(dict, tuple) == (1, 2)

    def test_order_of_test_does_not_matter(self):
        assert object() == instance_of(object)

    def test_representation(self):
        test_obj = instance_of(dict)
        expected = r"Any instance of <(type|class) 'dict'>"
        assert re.match(expected, str(test_obj))
        assert re.match('<Equals {}>'.format(expected), repr(test_obj))


class TestWithAttrs(object):
    test_obj = anything.with_attrs(foo='bar', bob='barker')

    def test_equals_instance_with_all_attrs(self):
        assert self.test_obj == Dummy('bar', 'barker')

    def test_does_not_equal_instance_with_all_attrs_but_diff_values(self):
        assert not self.test_obj == Dummy('Drew', 'Carey')

    def test_does_not_equal_instance_without_all_attrs(self):
        assert not self.test_obj == object()

    def test_equals_instance_of_correct_type(self):
        test_obj = instance_of(Dummy).with_attrs(foo='bar', bob='barker')
        assert test_obj == Dummy('bar', 'barker')

    def test_does_not_equal_instance_of_wrong_type(self):
        test_obj = instance_of(dict).with_attrs(foo='bar', bob='barker')
        assert not test_obj == Dummy('bar', 'barker')

    def test_order_of_test_does_not_matter(self):
        assert Dummy('bar', 'barker') == self.test_obj

    def test_passes_with_correct_args_and_kwargs(self):
        test_obj = anything.with_attrs('foo', bob='barker')
        assert Dummy('bar', 'barker') == test_obj

    def test_fails_with_incorrect_args_and_kwargs(self):
        test_obj = anything.with_attrs('bar', bob='barker')
        assert Dummy('bar', 'barker') != test_obj

    def test_representation(self):
        assert repr(self.test_obj) == (
            "<Equals Any object with attrs: bob=barker, foo=bar>"
        )
        assert str(self.test_obj) == (
            "Any object with attrs: bob=barker, foo=bar"
        )

    def test_representation_args_and_kwargs(self):
        test_obj = anything.with_attrs('bar', bob='barker')
        assert repr(test_obj) == (
            "<Equals Any object with attrs: bar and bob=barker>"
        )
        assert str(test_obj) == (
            "Any object with attrs: bar and bob=barker"
        )

    def test_poorly_implemented__eq__(self):
        test_obj = instance_of(NeverEquals).with_attrs(
            name="Bob Barker",
        )
        assert test_obj == NeverEquals("Bob Barker")
