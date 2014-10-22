class Matcher(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Includes(Matcher):
    def __eq__(self, value):
        for k, v in self.kwargs.items():
            if k not in value or not value[k] == v:
                return False
        return True


class HasKeys(Matcher):
    def __eq__(self, value):
        for i in self.args:
            if i not in value:
                return False
        return True
