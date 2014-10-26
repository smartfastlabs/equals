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
        from containing import Containing
        return Containing

    @constraint
    def not_containing(self):
        from not_containing import NotContaining
        return NotContaining

    @constraint
    def containing_only(self):
        from containing_only import ContainingOnly
        return ContainingOnly

    @constraint
    def matching(self):
        from strings.regex import Regex
        return Regex

    @constraint
    def starting_with(self):
        from strings.startswith import StartsWith
        return StartsWith

    @constraint
    def ending_with(self):
        from strings.endswith import EndsWith
        return EndsWith

    @constraint
    def with_attrs(self):
        from with_attrs import WithAttrs
        return WithAttrs

    @constraint
    def greater_than(self):
        from numbers.greater_than import GreaterThan
        return GreaterThan

    @constraint
    def greater_than_or_equal_to(self):
        from numbers.greater_than_or_equal import GreaterThanOrEqual
        return GreaterThanOrEqual

    @constraint
    def less_than(self):
        from numbers.less_than import LessThan
        return LessThan

    @constraint
    def less_than_or_equal_to(self):
        from numbers.less_than_or_equal import LessThanOrEqual
        return LessThanOrEqual

    @constraint
    def between(self):
        from numbers.between import Between
        return Between