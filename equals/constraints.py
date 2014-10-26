from functools import wraps


def constraint(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        matcher_class = func(self)
        value = matcher_class(
            self,
            *args,
            **kwargs
        )
        return value

    return wrapped


class Constraints(object):
    @constraint
    def containing(self):
        from iter_matchers import Containing
        return Containing

    @constraint
    def not_containing(self):
        from iter_matchers import NotContaining
        return NotContaining

    @constraint
    def matching(self):
        from string_matchers import RegexMatcher
        return RegexMatcher

    @constraint
    def containing_only(self):
        from iter_matchers import ContainingOnly
        return ContainingOnly

    @constraint
    def starting_with(self):
        from string_matchers import StartsWithMatcher
        return StartsWithMatcher

    @constraint
    def ending_with(self):
        from string_matchers import EndsWithMatcher
        return EndsWithMatcher

    @constraint
    def with_attrs(self):
        from object_matchers import HasAttrs
        return HasAttrs

    @constraint
    def greater_than(self):
        from number_matchers import GreaterThan
        return GreaterThan

    @constraint
    def greater_than_or_equal_to(self):
        from number_matchers import GreaterThanOrEqual
        return GreaterThanOrEqual

    @constraint
    def less_than(self):
        from number_matchers import LessThan
        return LessThan

    @constraint
    def less_than_or_equal_to(self):
        from number_matchers import LessThanOrEqual
        return LessThanOrEqual

    @constraint
    def between(self):
        from number_matchers import WithinRange
        return WithinRange

    @constraint
    def plus_or_minus(self):
        from number_matchers import PlusOrMinus
        return PlusOrMinus

    @constraint
    def with_keys(self):
        from dict_matchers import HasKeys
        return HasKeys
