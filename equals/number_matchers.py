from base_matcher import BaseMatcher


class NumberMatcher(BaseMatcher):
    def _handle_args(self, value):
        self.value = value


class LessThan(NumberMatcher):
    _description = 'less than {}'

    def _check(self, value):
        return value < self.value


class LessThanOrEqual(NumberMatcher):
    _description = 'less than or equal to {}'

    def _check(self, value):
        return value <= self.value


class GreaterThan(NumberMatcher):
    _description = 'greater than {}'

    def _check(self, value):
        return value > self.value


class GreaterThanOrEqual(NumberMatcher):
    _description = 'greater than or equal to {}'

    def _check(self, value):
        return value >= self.value


class Between(NumberMatcher):
    @property
    def description(self):
        return 'between {min} and {max}'.format(
            min=self.min_val,
            max=self.max_val,
        )

    def _handle_args(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def _check(self, value):
        return self.min_val < value < self.max_val
