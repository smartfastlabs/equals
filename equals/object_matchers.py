from base_matcher import BaseMatcher


class AnythingTruthy(BaseMatcher):
    _description = 'that is true'

    def _check(self, value):
        return bool(value)


class AnythingFalsey(BaseMatcher):
    _description = 'that is false'

    def _check(self, value):
        return not bool(value)


class HasAttrs(BaseMatcher):
    _description = 'with attrs: {}'

    def _check(self, value):
        for k, v in self.kwargs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True
