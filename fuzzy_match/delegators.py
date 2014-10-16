import iter_matchers
import dict_matchers


def includes_elements(*args, **kwargs):
    if kwargs:
        return dict_matchers.DictIncludes(**kwargs)
    else:
        return iter_matchers.IteratorIncludes(*args)


def same_elements(*args, **kwargs):
    if kwargs:
        return dict_matchers.DictSameElements(**kwargs)
    else:
        return iter_matchers.IteratorSameElements(*args)
