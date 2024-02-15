from __future__ import absolute_import

__version__ = "1.0.0"

import numbers  # noqa

from equals.constraints.anything_false import AnythingFalse  # noqa
from equals.constraints.anything_true import AnythingTrue  # noqa
from equals.equals import Equals as instance_of  # noqa

try:
    from collections.abc import Iterable  # noqa
except ImportError:
    from collections import Iterable  # noqa

anything = instance_of()
try:
    any_string = instance_of(basestring)
except NameError:
    any_string = instance_of(str)

any_bytes = instance_of(bytes)
any_number = instance_of(numbers.Number)
any_int = instance_of(int)
any_float = instance_of(float)
any_iterable = instance_of(Iterable)
any_dict = instance_of(dict)
any_list = instance_of(list)
any_tuple = instance_of(tuple)
anything_false = AnythingFalse(anything)
anything_true = AnythingTrue(anything)
