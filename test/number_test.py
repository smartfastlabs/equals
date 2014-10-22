from fuzzy_match import (
    less_than,
    less_than_or_equal,
    greater_than,
    greater_than_or_equal,
    between,
    plus_or_minus,
)


class TestLessThan(object):
    def test_equals_a_smaller_number(self):
        assert less_than(5) == 4

    def test_does_not_equal_same_number(self):
        assert not less_than(5) == 5

    def test_does_not_equal_larger_number(self):
        assert not less_than(5) == 6


class TestGreateThan(object):
    def test_equals_a_larger_number(self):
        assert greater_than(5) == 6

    def test_does_not_equal_same_number(self):
        assert not greater_than(5) == 5

    def test_does_not_equal_smaller_number(self):
        assert not greater_than(5) == 4


class TestLessThanOrEqual(object):
    def test_equal_equals_a_smaller_number(self):
        assert less_than_or_equal(5) == 4

    def test_equals_same_number(self):
        assert less_than_or_equal(5) == 5

    def test_does_not_equal_larger_number(self):
        assert not less_than_or_equal(5) == 6


class TestGreateThanOrEqual(object):
    def test_equals_a_larger_number(self):
        assert greater_than_or_equal(5) == 6

    def test_equals_same_number(self):
        assert greater_than_or_equal(5) == 5

    def test_does_not_equal_smaller_number(self):
        assert not greater_than_or_equal(5) == 4


class TestBetween(object):
    def test_equals_value_in_range(self):
        assert between(1, 3) == 2

    def test_does_not_equal_value_larger_than_max(self):
        assert not between(1, 3) == 4

    def test_does_not_equal_value_smaller_than_min(self):
        assert not between(1, 3) == 0

    def test_does_not_equal_value_equal_to_max(self):
        assert not between(1, 3) == 3

    def test_does_not_equal_value_equal_to_min(self):
        assert not between(1, 3) == 1


class TestPlusOrMinus(object):
    def test_equals_value_within_range(self):
        assert plus_or_minus(10, 1) == 10.5

    def test_does_not_eqaul_value_out_of_range(self):
        assert not plus_or_minus(10, 1) == 11.5
