import numbers
import collections

from equals import Equals as instance_of
from constraints.anything_true import AnythingTrue
from constraints.anything_false import AnythingFalse

anything = instance_of()
any_string = instance_of(basestring)
any_number = instance_of(numbers.Number)
any_int = instance_of(int)
any_float = instance_of(float)
any_iterable = instance_of(collections.Iterable)
any_dict = instance_of(dict)
any_list = instance_of(list)
any_tuple = instance_of(tuple)
anything_false = AnythingFalse(anything)
anything_true = AnythingTrue(anything)
