class Matcher(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DictIncludes(Matcher):
    def __eq__(self, value):
        for k, v in self.kwargs.items():
            if k not in value or not value[k] == v:
                return False
        return True


class DictSameElements(DictIncludes):
    def __eq__(self, value):
        if not len(value) == len(self.kwargs):
            return False
        return super(DictSameElements, self).__eq__(value)
