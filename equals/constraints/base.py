from . import Constraints


class Base(Constraints):
    def __init__(self, parent, *args, **kwargs):
        self._parent = parent
        self.args = args
        self.kwargs = kwargs
        self._handle_args(*args, **kwargs)

    def __eq__(self, value):
        if not self._parent == value:
            return False
        try:
            return self._check(value)
        except Exception:
            return False

    def __ne__(self, value):
        return not self == value

    def _handle_args(self, *args, **kwargs):
        if args:
            self.value = args[0]

    def __repr__(self):
        return '<Equals {}>'.format(str(self))

    def __str__(self):
        join_string = ' and ' if isinstance(self._parent, Base) else ' '
        return '{parent}{join_string}{description}'.format(
            parent=self._parent,
            description=self.description,
            join_string=join_string
        )

    @property
    def description(self):
        constraints = []
        if self.args:
            constraints = [', '.join(
                [str(x) for x in self.args],
            )]
        if self.kwargs:
            kwargs = sorted(self.kwargs.items())
            constraints.append(', '.join(
                ['{}={}'.format(*x) for x in kwargs],
            ))
        params = ' and '.join(constraints)
        return self._description.format(params)
