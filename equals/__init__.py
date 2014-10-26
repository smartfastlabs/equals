import numbers
import collections

from instance_of import InstanceOf as instance_of
from object_matchers import AnythingTruthy
from object_matchers import AnythingFalsey

anything = instance_of()
any_string = instance_of(basestring)
any_number = instance_of(numbers.Number)
any_int = instance_of(int)
any_float = instance_of(float)
any_iterable = instance_of(collections.Iterable)
any_dict = instance_of(dict)
any_list = instance_of(list)
any_tuple = instance_of(tuple)
anything_false = AnythingFalsey(anything)
anything_true = AnythingTruthy(anything)
