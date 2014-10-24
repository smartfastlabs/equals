from base_matcher import BaseMatcher


class Matcher(BaseMatcher):

    def with_attrs(self, **kwargs):
        return MatchHasAttrs(
            *self.args,
            **kwargs
        )


class MatchAnything(Matcher):
    def _check(self, value):
        return True


class MatchAnythingTruthy(Matcher):
    def _check(self, value):
        return bool(value)


class MatchAnythingFalsey(Matcher):
    def _check(self, value):
        return not bool(value)


class MatchAnyInstanceOf(Matcher):
    def _check(self, value):
        return isinstance(value, self.args)


class MatchHasAttrs(Matcher):
    def _check(self, value):
        if self._wrong_type(value):
            return False

        for k, v in self.kwargs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True

    def _wrong_type(self, value):
        if not self.args:
            return False

        return not isinstance(value, self.args)
