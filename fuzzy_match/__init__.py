from string_matchers import StringContainsMatcher as contains  # noqa
from string_matchers import StringStartsWithMatcher as startswith  # noqa
from string_matchers import StringEndsWithMatcher as endswith  # noqa
from string_matchers import StringRegexMatcher as matches  # noqa

from iter_matchers import SameElements as same_elements  # noqa
from dict_matchers import HasKeys as has_keys  # noqa
import iter_matchers
import dict_matchers

from object_matchers import MatchAnything
from object_matchers import MatchAnythingTruthy
from object_matchers import MatchAnythingFalsey
from object_matchers import MatchAnyInstanceOf as instance_of  # noqa

from number_matchers import LessThan as less_than  # noqa
from number_matchers import LessThanOrEqual as less_than_or_equal  # noqa
from number_matchers import GreaterThan as greater_than  # noqa
from number_matchers import GreaterThanOrEqual as greater_than_or_equal  # noqa
from number_matchers import WithinRange as between  # noqa
from number_matchers import PlusOrMinus as plus_or_minus  # noqa

anything = MatchAnything()
anything_false = MatchAnythingFalsey()
anything_true = MatchAnythingTruthy()


def has_elements(*args, **kwargs):
    if kwargs:
        return dict_matchers.Includes(**kwargs)
    return iter_matchers.Includes(*args)
