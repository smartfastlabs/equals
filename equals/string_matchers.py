import re

from base_matcher import BaseMatcher


class StringMatcher(BaseMatcher):
    def __init__(self, value):
        self.value = value


class StringContainsMatcher(StringMatcher):
    def _check(self, value):
        return self.value in value


class StringStartsWithMatcher(StringMatcher):
    def _check(self, value):
        return value.startswith(self.value)


class StringEndsWithMatcher(StringMatcher):
    def _check(self, value):
        return value.endswith(self.value)


class StringRegexMatcher(StringMatcher):
    def _check(self, value):
        return bool(re.search(self.value, value))
