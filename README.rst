A mock equality tool for testing
================================

.. image:: https://badge.fury.io/py/equals.svg
    :target: https://badge.fury.io/py/equals

.. image:: https://readthedocs.org/projects/equals/badge/?version=latest
    :target: https://equals.readthedocs.io/en/latest/?badge=latest

.. image:: https://coveralls.io/repos/github/smartfastlabs/equals/badge.svg?branch=master
    :target: https://coveralls.io/github/smartfastlabs/equals?branch=master


tl;dr Equals is a stricter version of
`Mock.Any <http://www.voidspace.org.uk/python/mock/helpers.html#any>`__.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order.  This was designed specifically for
usage with `Mock <https://pypi.python.org/pypi/mock>`_ and `dobles <https://github.com/smartfastlabs/dobles>`_.


Usage
=====
**Full Documentation is available at http://equals.readthedocs.org/en/latest/.**

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

**Note:** For more examples please see https://equals.readthedocs.io/en/latest/api.html.


Installation:
-------------

::

    >> pip install equals


Development
-----------

Source code is available at https://github.com/smartfastlabs/equals.

To install the dependencies on a fresh clone of the repository, run ``make bootstrap``.

To run the test suite, run ``make test``.

To build the documentation locally, run ``make docs``.


License
-------

MIT: http://opensource.org/licenses/MIT
