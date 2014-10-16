class Matcher(object):
    def __init__(self, *args):
        self.args = args


class IteratorIncludes(Matcher):
    def __eq__(self, value):
        for v in self.args:
            if v not in value:
                return False
        return True


class IteratorSameElements(IteratorIncludes):
    def __eq__(self, value):
        if not len(value) == len(self.args):
            return False
        return super(IteratorSameElements, self).__eq__(value)
