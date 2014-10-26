from equals import any_number


class TestLessThan(object):
    def test_equals_a_smaller_number(self):
        assert any_number.less_than(5) == 4

    def test_does_not_equal_same_number(self):
        assert not any_number.less_than(5) == 5

    def test_does_not_equal_larger_number(self):
        assert not any_number.less_than(5) == 6

    def test_order_of_test_does_not_matter(self):
        assert 4 == any_number.less_than(5)


class TestGreateThan(object):
    def test_equals_a_larger_number(self):
        assert any_number.greater_than(5) == 6

    def test_does_not_equal_same_number(self):
        assert not any_number.greater_than(5) == 5

    def test_does_not_equal_smaller_number(self):
        assert not any_number.greater_than(5) == 4

    def test_order_of_test_does_not_matter(self):
        assert 6 == any_number.greater_than(5)


class TestLessThanOrEqual(object):
    def test_equal_equals_a_smaller_number(self):
        assert any_number.less_than_or_equal_to(5) == 4

    def test_equals_same_number(self):
        assert any_number.less_than_or_equal_to(5) == 5

    def test_does_not_equal_larger_number(self):
        assert not any_number.less_than_or_equal_to(5) == 6

    def test_order_of_test_does_not_matter(self):
        assert 4 == any_number.less_than_or_equal_to(5)


class TestGreateThanOrEqual(object):
    def test_equals_a_larger_number(self):
        assert any_number.greater_than_or_equal_to(5) == 6

    def test_equals_same_number(self):
        assert any_number.greater_than_or_equal_to(5) == 5

    def test_does_not_equal_smaller_number(self):
        assert not any_number.greater_than_or_equal_to(5) == 4

    def test_order_of_test_does_not_matter(self):
        assert 6 == any_number.greater_than_or_equal_to(5)


class TestBetween(object):
    def test_equals_value_in_range(self):
        assert any_number.between(1, 3) == 2

    def test_does_not_equal_value_larger_than_max(self):
        assert not any_number.between(1, 3) == 4

    def test_does_not_equal_value_smaller_than_min(self):
        assert not any_number.between(1, 3) == 0

    def test_does_not_equal_value_equal_to_max(self):
        assert not any_number.between(1, 3) == 3

    def test_does_not_equal_value_equal_to_min(self):
        assert not any_number.between(1, 3) == 1

    def test_order_of_test_does_not_matter(self):
        assert 2 == any_number.between(1, 3)


class TestPlusOrMinus(object):
    def test_equals_value_within_range(self):
        assert any_number.plus_or_minus(10, 1) == 10.5

    def test_does_not_eqaul_value_out_of_range(self):
        assert not any_number.plus_or_minus(10, 1) == 11.5

    def test_order_of_test_does_not_matter(self):
        assert 10.5 == any_number.plus_or_minus(10, 1)
