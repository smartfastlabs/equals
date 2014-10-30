from .containing import Containing


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
