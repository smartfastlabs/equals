import re

from equals import any_iterable


class TestContaining(object):
    test_obj = any_iterable.containing(1, 2, 3)

    def test_passes_on_super_set(self):
        assert self.test_obj == [1, 2, 3, 4, 5]

    def test_fails_on_sub_set(self):
        assert not self.test_obj == [2, 3, 4, 5]

    def test_representation(self):
        expected = (
            "Any instance of <class '.*Iterable'> "
            "containing: 1, 2, 3"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match('<Equals {}>'.format(expected), repr(self.test_obj))


class TestNotContaining(object):
    test_obj = any_iterable.not_containing(1, 2, 3)

    def test_passes_if_value_is_not_found(self):
        assert self.test_obj == [4, 5]

    def test_fails_if_value_is_found(self):
        assert not self.test_obj == [1, 2, 3, 4, 5]

    def test_representation(self):
        expected = (
            "Any instance of <class '.*Iterable'> "
            "not containing: 1, 2, 3"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match('<Equals {}>'.format(expected), repr(self.test_obj))


class TestContainingOnly(object):
    test_obj = any_iterable.containing_only(1, 2, 3)

    def test_containing_only_passes_on_identical_list(self):
        assert self.test_obj == [1, 2, 3]

    def test_containing_only_fails_on_super_set(self):
        assert not self.test_obj == [1, 2, 3, 4]

    def test_containing_only_fails_on_sub_set(self):
        assert not self.test_obj == [2, 3]

    def test_representation(self):
        expected = (
            "Any instance of <class '.*Iterable'> "
            "containing only: 1, 2, 3"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match('<Equals {}>'.format(expected), repr(self.test_obj))


def test_order_of_test_does_not_matter():
    assert [1, 2, 3, 4, 5] == any_iterable.containing(1, 2, 3)


def test_length():
    assert [1, 2] == any_iterable.with_length(2)
    assert [1, 2] != any_iterable.with_length(3)
