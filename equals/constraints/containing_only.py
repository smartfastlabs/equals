from .containing import Containing


class ContainingOnly(Containing):
    _description = 'containing only: {}'

    def _check(self, value):
        if not len(value) == len(self.args):
            return False
        return super(ContainingOnly, self)._check(value)
