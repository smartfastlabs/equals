class Matcher(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


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
        return isinstance(value, self.args)


class MatchHasAttrs(Matcher):
    def __init__(self, instance_type=None, **kwargs):
        self.instance_type = instance_type
        self.expected_attrs = kwargs

    def __eq__(self, value):
        if self._wrong_type(value):
            return False

        for k, v in self.expected_attrs.items():
            if not hasattr(value, k):
                return False
            if getattr(value, k) != v:
                return False

        return True

    def _wrong_type(self, value):
        if not self.instance_type:
            return False

        return not isinstance(value, self.instance_type)
