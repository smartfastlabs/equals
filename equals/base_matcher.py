class BaseMatcher(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __eq__(self, value):
        return self._check(value)
