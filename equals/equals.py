from __future__ import absolute_import

from equals.constraints import Constraints


def _stringify_types(types):
    types = [str(t) for t in types]
    return ' or '.join(types)


class Equals(Constraints):
    _types = None
    _parent = None

    def __init__(self, *types):
        self._types = types

    def __eq__(self, value):
        if not self._types:
            return True
        return isinstance(value, self._types)

    def __ne__(self, value):
        return not self == value

    def __str__(self):
        if self._types:
            return 'Any instance of {types}'.format(
                types=_stringify_types(self._types),
            )
        return 'Any object'

    def __repr__(self):
        return '<Equals {}>'.format(str(self))
