from base_matcher import BaseMatcher


class IteratorMatcher(BaseMatcher):
    pass


class Includes(IteratorMatcher):
    def _check(self, value):
        for v in self.args:
            if v not in value:
                return False
        return True


class SameElements(Includes):
    def _check(self, value):
        if not len(value) == len(self.args):
            return False
        return super(SameElements, self)._check(value)
