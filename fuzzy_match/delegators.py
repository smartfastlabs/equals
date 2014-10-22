from functools import wraps

import iter_matchers
import dict_matchers


def delegater(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return func(
            dict_matchers if kwargs else iter_matchers,
            *args,
            **kwargs
        )

    return wrapped


@delegater
def has_elements(module, *args, **kwargs):
    return module.Includes(*args, **kwargs)


@delegater
def same_elements(module, *args, **kwargs):
    return module.SameElements(*args, **kwargs)
