Usage
=====

With Mock:
----------

::

    from mock import Mock
    from equals import any_dict

    test_object = Mock()
    test_object.method({'bob': 'barker'})
    test_object.method.assert_called_with(any_dict)

dobles:
-------

::

    from dobles import expect
    from equals import any_string


    class TestClass(object):
        def method(self, arg):
            return arg


    test_object = TestClass()
    expect(test_object).method.with_args(any_string.containing('bob'))

    test_object.method('bob barker')