from constraints import Constraints


class InstanceOf(Constraints):
    _types = None

    def __init__(self, *types):
        self._types = types

    def __eq__(self, value):
        if not self._types:
            return True
        return isinstance(value, self._types)

    def __ne__(self, value):
        return not self == value
