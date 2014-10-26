import re

from base_matcher import BaseMatcher


class StringMatcher(BaseMatcher):
    def _handle_args(self, value):
        self.value = value


class StartsWithMatcher(StringMatcher):
    def _check(self, value):
        return value.startswith(self.value)


class EndsWithMatcher(StringMatcher):
    def _check(self, value):
        return value.endswith(self.value)


class RegexMatcher(StringMatcher):
    def _check(self, value):
        return bool(re.search(self.value, value))
