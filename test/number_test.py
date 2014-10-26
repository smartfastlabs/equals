from equals import any_number


class TestLessThan(object):
    test_obj = any_number.less_than(5)

    def test_equals_a_smaller_number(self):
        assert self.test_obj == 4

    def test_does_not_equal_same_number(self):
        assert not self.test_obj == 5

    def test_does_not_equal_larger_number(self):
        assert not self.test_obj == 6

    def test_order_of_test_does_not_matter(self):
        assert 4 == self.test_obj

    def test_representation(self):
        expected = (
            "Any instance of <class 'numbers.Number'> "
            "less than 5"
        )
        assert str(self.test_obj) == expected
        assert repr(self.test_obj) == '<Equals {}>'.format(expected)


class TestGreateThan(object):
    test_obj = any_number.greater_than(5)

    def test_equals_a_larger_number(self):
        assert self.test_obj == 6

    def test_does_not_equal_same_number(self):
        assert not self.test_obj == 5

    def test_does_not_equal_smaller_number(self):
        assert not self.test_obj == 4

    def test_order_of_test_does_not_matter(self):
        assert 6 == self.test_obj

    def test_representation(self):
        expected = (
            "Any instance of <class 'numbers.Number'> "
            "greater than 5"
        )
        assert str(self.test_obj) == expected
        assert repr(self.test_obj) == '<Equals {}>'.format(expected)


class TestLessThanOrEqual(object):
    test_obj = any_number.less_than_or_equal_to(5)

    def test_equal_equals_a_smaller_number(self):
        assert self.test_obj == 4

    def test_equals_same_number(self):
        assert self.test_obj == 5

    def test_does_not_equal_larger_number(self):
        assert not self.test_obj == 6

    def test_order_of_test_does_not_matter(self):
        assert 4 == self.test_obj

    def test_representation(self):
        expected = (
            "Any instance of <class 'numbers.Number'> "
            "less than or equal to 5"
        )
        assert str(self.test_obj) == expected
        assert repr(self.test_obj) == '<Equals {}>'.format(expected)


class TestGreateThanOrEqual(object):
    test_obj = any_number.greater_than_or_equal_to(5)

    def test_equals_a_larger_number(self):
        assert self.test_obj == 6

    def test_equals_same_number(self):
        assert self.test_obj == 5

    def test_does_not_equal_smaller_number(self):
        assert not self.test_obj == 4

    def test_order_of_test_does_not_matter(self):
        assert 6 == self.test_obj

    def test_representation(self):
        expected = (
            "Any instance of <class 'numbers.Number'> "
            "greater than or equal to 5"
        )
        assert str(self.test_obj) == expected
        assert repr(self.test_obj) == '<Equals {}>'.format(expected)


class TestBetween(object):
    test_obj = any_number.between(1, 3)

    def test_equals_value_in_range(self):
        assert self.test_obj == 2

    def test_does_not_equal_value_larger_than_max(self):
        assert not self.test_obj == 4

    def test_does_not_equal_value_smaller_than_min(self):
        assert not self.test_obj == 0

    def test_does_not_equal_value_equal_to_max(self):
        assert not self.test_obj == 3

    def test_does_not_equal_value_equal_to_min(self):
        assert not self.test_obj == 1

    def test_order_of_test_does_not_matter(self):
        assert 2 == self.test_obj

    def test_representation(self):
        expected = (
            "Any instance of <class 'numbers.Number'> "
            "between 1 and 3"
        )
        assert str(self.test_obj) == expected
        assert repr(self.test_obj) == '<Equals {}>'.format(expected)
