equals
=============

equals allows you to assert certain equality constraints between python objects during testing.  There are times where we don't want to assert absolute equality, e.g. we need to ensure two lists have the same elements, but don't care about order.

strings:
-------
    contains('abc') == '123 abc 456'
    startswith('abc') == 'abcdef'
    endswith('abc') == '123abc'
    matches('^abc$') == 'abc'


numbers:
-------
    less_than(5) == 4
    less_than_or_equal(5) == 5
    greater_than(4) == 5
    greater_than_or_equal(5) == 5
    between(1, 3) == 2
    plus_or_minus(10, 1) == 10.5

dictionaries:
-------
    has_keys(1, 2) == {1: 2, 2:3, 4:5}
    has_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }

iterators:
-------
    has_elements(1, 2, 3) == [1, 2, 3, 4, 5]
    same_elements(1, 2, 3) == [2, 3, 1]

objects:
-------
    anything == None
    anything == True
    anything == {1: 1}
    anything_true == 'dd'
    anything_false == ''

    instance_of(dict) == {}
    anything.with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')
    instance_of(Dummy).with_attrs(foo='bar', bob='barker') == Dummy('bar', 'barker')


Usage with Mock:
-------
    test_object = Mock()
    test_object.method({'bob': 'barker'})
    test_object.method.assert_called_with(instance_of(dict))

Usage with doubles:
-------
    test_object = TestClass()
    expect(test_object).method.with_args(contains('bob'))

    test_object.method('bob barker')

Installation:
-------
    >> pip install equals


License:
-------

See LICENSE
