from string_matchers import StringContainsMatcher as contains  # noqa
from string_matchers import StringStartsWithMatcher as startswith  # noqa
from string_matchers import StringEndsWithMatcher as endswith  # noqa
from string_matchers import StringRegexMatcher as matches  # noqa

from delegators import same_elements  # noqa
from delegators import includes_elements  # noqa

from object_matchers import MatchAnything
from object_matchers import MatchAnythingTruthy
from object_matchers import MatchAnythingFalsey
from object_matchers import MatchAnyInstanceOf as any_instance  # noqa

anything = MatchAnything()
anything_false = MatchAnythingFalsey()
anything_true = MatchAnythingTruthy()
