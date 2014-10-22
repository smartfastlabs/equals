from string_matchers import StringContainsMatcher as contains  # noqa
from string_matchers import StringStartsWithMatcher as startswith  # noqa
from string_matchers import StringEndsWithMatcher as endswith  # noqa
from string_matchers import StringRegexMatcher as matches  # noqa

from delegators import same_elements  # noqa
from delegators import has_elements  # noqa

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
