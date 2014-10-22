class Matcher(object):
    def __init__(self, *args, **kwargs):
        self.instance_types = args
        self.instance_attrs = kwargs

    def with_attrs(self, **kwargs):
        return MatchHasAttrs(
            *self.instance_types,
            **kwargs
        )


class MatchAnything(Matcher):
    def __eq__(self, value):
        return True


class MatchAnythingTruthy(Matcher):
    def __eq__(self, value):
        return bool(value)


class MatchAnythingFalsey(Matcher):
    def __eq__(self, value):
        return not bool(value)


class MatchAnyInstanceOf(Matcher):
    def __eq__(self, value):
        return isinstance(value, self.instance_types)


class MatchHasAttrs(Matcher):
    def __eq__(self, value):
        if self._wrong_type(value):
            return False

        for k, v in self.instance_attrs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True

    def _wrong_type(self, value):
        if not self.instance_types:
            return False

        return not isinstance(value, self.instance_types)
