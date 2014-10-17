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
