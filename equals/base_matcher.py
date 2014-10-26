from constraints import Constraints


class BaseMatcher(Constraints):
    def __init__(self, parent, *args, **kwargs):
        self._parent = parent
        self.args = args
        self.kwargs = kwargs
        self._handle_args(*args, **kwargs)

    def __eq__(self, value):
        if value != self._parent:
            return False
        try:
            return self._check(value)
        except Exception:
            return False

    def __ne__(self, value):
        return not self == value

    def _handle_args(self, *args, **kwargs):
        pass
