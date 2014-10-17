from fuzzy_match import (
    less_than,
    less_than_or_equal,
    greater_than,
    greater_than_or_equal,
    between,
    plus_or_minus,
)


def test_less_than_equals_a_smaller_number():
    assert less_than(5) == 4


def test_less_than_does_not_equal_same_number():
    assert not less_than(5) == 5


def test_less_than_does_not_equal_larger_number():
    assert not less_than(5) == 6


def test_greater_than_equals_a_larger_number():
    assert greater_than(5) == 6


def test_greater_than_does_not_equal_same_number():
    assert not greater_than(5) == 5


def test_greater_than_does_not_equal_smaller_number():
    assert not greater_than(5) == 4


def test_less_than_or_equal_equals_a_smaller_number():
    assert less_than_or_equal(5) == 4


def test_less_than_or_equal_equals_same_number():
    assert less_than_or_equal(5) == 5


def test_less_than_or_equal_does_not_equal_larger_number():
    assert not less_than_or_equal(5) == 6


def test_greater_than_or_equal_equals_a_larger_number():
    assert greater_than_or_equal(5) == 6


def test_greater_than_or_equal_equals_same_number():
    assert greater_than_or_equal(5) == 5


def test_greater_than_or_equal_does_not_equal_smaller_number():
    assert not greater_than_or_equal(5) == 4


def test_between_equals_value_in_range():
    assert between(1, 3) == 2


def test_between_does_not_equal_value_larger_than_max():
    assert not between(1, 3) == 4


def test_between_does_not_equal_value_smaller_than_min():
    assert not between(1, 3) == 0


def test_between_does_not_equal_value_equal_to_max():
    assert not between(1, 3) == 3


def test_between_does_not_equal_value_equal_to_min():
    assert not between(1, 3) == 1


def test_plus_or_minus_equals_value_within_range():
    assert plus_or_minus(10, 1) == 10.5


def test_plus_or_minus_does_not_eqaul_value_out_of_range():
    assert not plus_or_minus(10, 1) == 11.5
