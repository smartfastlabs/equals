fuzzy_matcher
=============

fuzzy_matcher allows you to assert certain equality constraints between python objects during testing.  There are times where we don't want to assert absolute equality, e.g. we need to ensure two lists have the same elements, but don't care about order.

strings:
-------
*   contains
*   startswith
*   endswith
*   matches


numbers:
-------
*   less_than
*   less_than_or_equal
*   greater_than
*   greater_than_or_equal
*   between
*   plus_or_minus

iterators/dictionaries:
-------
*   same_elements
*   includes_elements

objects:
-------
*   anything
*   anything_true
*   anything_false


Examples:
-------
    contains('abc') == '123 abc 456'
    startswith('abc') == 'abcdef'
    matches('^abc$') == 'abc'

    includes_elements(1, 2, 3) == [1, 2, 3, 4, 5]
    same_elements(1, 2, 3) == [2, 3, 1]

    includes_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }

    anything == None
    anything == True
    anything == {1: 1}
    any_instance(dict) == {}


License:
-------

See LICENSE
