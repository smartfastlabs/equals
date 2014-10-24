from base_matcher import BaseMatcher


class DictMatcher(BaseMatcher):
    pass


class Includes(DictMatcher):
    def _check(self, value):
        for k, v in self.kwargs.items():
            if k not in value or not value[k] == v:
                return False
        return True


class HasKeys(DictMatcher):
    def _check(self, value):
        for i in self.args:
            if i not in value:
                return False
        return True
