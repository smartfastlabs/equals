from __future__ import absolute_import

__version__ = '0.0.2'

import numbers
import collections

from equals.equals import Equals as instance_of
from equals.constraints.anything_true import AnythingTrue
from equals.constraints.anything_false import AnythingFalse

anything = instance_of()
try:
    any_string = instance_of(basestring)
except NameError:
    any_string = instance_of(str)
any_number = instance_of(numbers.Number)
any_int = instance_of(int)
any_float = instance_of(float)
any_iterable = instance_of(collections.Iterable)
any_dict = instance_of(dict)
any_list = instance_of(list)
any_tuple = instance_of(tuple)
anything_false = AnythingFalse(anything)
anything_true = AnythingTrue(anything)
