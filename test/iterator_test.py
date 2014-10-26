from equals import any_iterable


def test_containing_passes_on_super_set():
    assert any_iterable.containing(1, 2, 3) == [1, 2, 3, 4, 5]


def test_containing_fails_on_sub_set():
    assert not any_iterable.containing(1, 2, 3) == [2, 3, 4, 5]


def test_not_containing_passes_if_value_is_not_found():
    assert any_iterable.not_containing(1, 2, 3) == [4, 5]


def test_not_containing_fails_if_value_is_found():
    assert not any_iterable.not_containing(1, 2, 3) == [1, 2, 3, 4, 5]


def test_containing_only_passes_on_identical_list():
    assert any_iterable.containing_only(1, 2, 3) == [1, 2, 3]


def test_containing_only_fails_on_super_set():
    assert not any_iterable.containing_only(1, 2, 3) == [1, 2, 3, 4]


def test_containing_only_fails_on_sub_set():
    assert not any_iterable.containing_only(1, 2, 3) == [2, 3]


def test_order_of_test_does_not_matter():
    assert [1, 2, 3, 4, 5] == any_iterable.containing(1, 2, 3)
