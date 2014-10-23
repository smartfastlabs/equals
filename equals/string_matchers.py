import re


class StringMatcher(object):
    def __init__(self, value):
        self.value = value


class StringContainsMatcher(StringMatcher):
    def __eq__(self, value):
        return self.value in value


class StringStartsWithMatcher(StringMatcher):
    def __eq__(self, value):
        return value.startswith(self.value)


class StringEndsWithMatcher(StringMatcher):
    def __eq__(self, value):
        return value.endswith(self.value)


class StringRegexMatcher(StringMatcher):
    def __eq__(self, value):
        return bool(re.search(self.value, value))
