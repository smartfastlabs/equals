class ValueMatcher(object):
    def __init__(self, value):
        self.value = value


class LessThan(ValueMatcher):
    def __eq__(self, value):
        return value < self.value


class LessThanOrEqual(ValueMatcher):
    def __eq__(self, value):
        return value <= self.value


class GreaterThan(ValueMatcher):
    def __eq__(self, value):
        return value > self.value


class GreaterThanOrEqual(ValueMatcher):
    def __eq__(self, value):
        return value >= self.value


class WithinRange(object):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __eq__(self, value):
        return self.min_val < value < self.max_val


class PlusOrMinus(WithinRange):
    def __init__(self, value, error):
        super(PlusOrMinus, self).__init__(
            value - error,
            value + error,
        )
