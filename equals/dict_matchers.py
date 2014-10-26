from base_matcher import BaseMatcher


class HasKeys(BaseMatcher):
    def _check(self, value):
        for i in self.args:
            if i not in value:
                return False
        return True
