from fuzzy_match import has_elements, same_elements


def test_has_elements_passes_on_super_set():
    assert has_elements(1, 2, 3) == [1, 2, 3, 4, 5]


def test_has_elements_fails_on_sub_set():
    assert not has_elements(1, 2, 3) == [2, 3, 4, 5]


def test_same_elements_passes_on_identical_list():
    assert same_elements(1, 2, 3) == [1, 2, 3]


def test_same_elements_fails_on_super_set():
    assert not same_elements(1, 2, 3) == [1, 2, 3, 4]


def test_same_elements_fails_on_sub_set():
    assert not same_elements(1, 2, 3) == [2, 3]
