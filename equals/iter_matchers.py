from base_matcher import BaseMatcher


class Containing(BaseMatcher):
    _description = 'containing: {}'

    def _check(self, value):
        # This will check list like objects
        for v in self.args:
            if v not in value:
                return False

        # This will check dictionary like objects
        for k, v in self.kwargs.items():
            if k not in value or not value[k] == v:
                return False
        return True


class NotContaining(Containing):
    _description = 'not containing: {}'

    def _check(self, value):
        # This will check list like objects
        for v in self.args:
            if v in value:
                return False

        # This will check dictionary like objects
        for k, v in self.kwargs.items():
            if k in value and value[k] == v:
                return False
        return True


class ContainingOnly(Containing):
    _description = 'containing only: {}'

    def _check(self, value):
        if not len(value) == len(self.args):
            return False
        return super(ContainingOnly, self)._check(value)
