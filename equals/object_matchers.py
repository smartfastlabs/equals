from base_matcher import BaseMatcher


class AnythingTruthy(BaseMatcher):
    def _check(self, value):
        return bool(value)


class AnythingFalsey(BaseMatcher):
    def _check(self, value):
        return not bool(value)


class AnyInstanceOf(BaseMatcher):
    def _check(self, value):
        return isinstance(value, self.args)


class HasAttrs(BaseMatcher):
    def _check(self, value):
        for k, v in self.kwargs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True
