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
*   has_elements

objects:
-------
*   anything
*   anything_true
*   anything_false
*   instance_of


Examples:
-------
    contains('abc') == '123 abc 456'
    startswith('abc') == 'abcdef'
    matches('^abc$') == 'abc'

    has_elements(1, 2, 3) == [1, 2, 3, 4, 5]
    same_elements(1, 2, 3) == [2, 3, 1]

    has_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }

    anything == None
    anything == True
    anything == {1: 1}
    instance_of(dict) == {}
    anything.with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')
    instance_of(Dummy).with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')

    less_than(5) == 4
    greater_than(4) == 5
    between(1, 3) == 2
    plus_or_minus(10, 1) == 10.5


License:
-------

See LICENSE
