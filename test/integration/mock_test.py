from mock import Mock
import pytest

from equals import instance_of


def test_mock_assert_called_with_passes():
    test_object = Mock()

    test_object.method({'bob': 'barker'})

    test_object.method.assert_called_with(instance_of(dict))


def test_mock_assert_called_with_can_fail():
    test_object = Mock()

    test_object.method({'bob': 'barker'})

    with pytest.raises(AssertionError):
        test_object.method.assert_called_with(instance_of(list))
