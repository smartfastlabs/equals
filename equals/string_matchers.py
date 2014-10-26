import re

from base_matcher import BaseMatcher


class StringMatcher(BaseMatcher):
    def _handle_args(self, value):
        self.value = value


class StartsWithMatcher(StringMatcher):
    _description = 'starting with {}'

    def _check(self, value):
        return value.startswith(self.value)


class EndsWithMatcher(StringMatcher):
    _description = 'ending with {}'

    def _check(self, value):
        return value.endswith(self.value)


class RegexMatcher(StringMatcher):
    _description = 'matching {}'

    def _check(self, value):
        return bool(re.search(self.value, value))
