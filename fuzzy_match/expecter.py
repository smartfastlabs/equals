from string_matchers import StringContainsMatcher
from string_matchers import StringStartsWithMatcher
from string_matchers import StringEndsWithMatcher
from string_matchers import StringRegexMatcher
from matchers import same_elements
from matchers import includes_elements


class Expecter(object):
    def __init__(self, value):
        self.value = value

    def to_include(self, *args, **kwargs):
        matcher = includes_elements(*args, **kwargs)
        assert matcher == self.value

    def to_have_exactly(self, *args, **kwargs):
        matcher = same_elements(*args, **kwargs)
        assert matcher == self.value

    def to_contain(self, value):
        assert StringContainsMatcher(value) == self.value

    def to_start_with(self, value):
        assert StringStartsWithMatcher(value) == self.value

    def to_end_with(self, value):
        assert StringEndsWithMatcher(value) == self.value

    def to_match(self, regex):
        assert StringRegexMatcher(regex) == self.value
