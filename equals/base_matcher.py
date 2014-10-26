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

    def __repr__(self):
        return '<Equals {}>'.format(str(self))

    def __str__(self):
        join_string = ' and ' if isinstance(self._parent, BaseMatcher) else ' '
        return '{parent}{join_string}{description}'.format(
            parent=self._parent,
            description=self.description,
            join_string=join_string
        )

    @property
    def description(self):
        if self.args:
            params = ', '.join(
                [str(x) for x in self.args],
            )
        elif self.kwargs:
            params = ', '.join(
                ['{}={}'.format(*x) for x in self.kwargs.items()],
            )
        else:
            params = ''
        return self._description.format(params)
