API
===

strings:
--------

::

    from equals import any_string

    any_string.containing('abc') == '123 abc 456'
    any_string.starting_with('abc') == 'abcdef'
    any_string.ending_with('abc') == '123abc'
    any_string.matching('^abc$') == 'abc'

numbers:
--------

::

    from equals import any_number

    any_number.less_than(5) == 4
    any_number.less_than_or_equal_to(5) == 5
    any_number.greater_than(4) == 5
    any_number.greater_than_or_equal_to(5) == 5
    any_number.between(1, 3) == 2

dictionaries:
-------------

::

    from equals import any_dict

    any_dict.containing(1, 2) == {1: 2, 2:3, 4:5}
    any_dict.containing(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }
    any_dict.not_containing(1, foo=5) == {'foo':3, 4:5}

iterators:
----------

::

    from equals import any_iterable

    any_iterable.containing(1, 2, 3) == [1, 2, 3, 4, 5]
    any_iterable.containing_only(1, 2, 3) == [2, 3, 1]
    any_iterable.not_containing(1, 2) == [3, 4]
    any_iterable.with_length(2) == [3, 4]

objects:
--------

::

    from equals import anything

    anything == None
    anything == True
    anything == {1: 1}
    anything_true == 'dd'
    anything_false == ''

    instance_of(dict) == {}
    anything.with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')
    instance_of(Dummy).with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')