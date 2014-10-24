from base_matcher import BaseMatcher


class NumberMatcher(BaseMatcher):
    def __init__(self, value):
        self.value = value


class LessThan(NumberMatcher):
    def _check(self, value):
        return value < self.value


class LessThanOrEqual(NumberMatcher):
    def _check(self, value):
        return value <= self.value


class GreaterThan(NumberMatcher):
    def _check(self, value):
        return value > self.value


class GreaterThanOrEqual(NumberMatcher):
    def _check(self, value):
        return value >= self.value


class WithinRange(NumberMatcher):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def _check(self, value):
        return self.min_val < value < self.max_val


class PlusOrMinus(WithinRange):
    def __init__(self, value, error):
        super(PlusOrMinus, self).__init__(
            value - error,
            value + error,
        )
