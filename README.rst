A mock equality tool for testing
================================

|Travis Test Status|

tl;dr Equals is a stricter version of
`Mock.Any <http://www.voidspace.org.uk/python/mock/helpers.html#any>`__.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order.

strings:
--------

::

    any_string.containing('abc') == '123 abc 456'
    any_string.starting_with('abc') == 'abcdef'
    any_string.ending_with('abc') == '123abc'
    any_string.matching('^abc$') == 'abc'

numbers:
--------

::

    any_number.less_than(5) == 4
    any_number.less_than_or_equal(5) == 5
    any_number.greater_than(4) == 5
    any_number.greater_than_or_equal(5) == 5
    any_number.between(1, 3) == 2

dictionaries:
-------------

::

    any_dict.containing(1, 2) == {1: 2, 2:3, 4:5}
    any_dict.containing(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }

iterators:
----------

::

    any_iter.containing(1, 2, 3) == [1, 2, 3, 4, 5]
    any_iter.containing_only(1, 2, 3) == [2, 3, 1]

objects:
--------

::

    anything == None
    anything == True
    anything == {1: 1}
    anything_true == 'dd'
    anything_false == ''

    instance_of(dict) == {}
    anything.with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')
    instance_of(Dummy).with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')

Usage with Mock:
----------------

::

    test_object = Mock()
    test_object.method({'bob': 'barker'})
    test_object.method.assert_called_with(any_dict)

Usage with doubles:
-------------------

::

    test_object = TestClass()
    expect(test_object).method.with_args(any_string.containing('bob'))

    test_object.method('bob barker')

Installation:
-------------

::

    >> pip install equals

Development:
------------

::

    >> git clone https://github.com/toddsifleet/equals
    >> cd equals
    >> make bootstrap
    >> make

License:
--------

See LICENSE

.. |Travis Test Status| image:: https://travis-ci.org/toddsifleet/equals.svg?branch=master
   :target: https://travis-ci.org/toddsifleet/equals
