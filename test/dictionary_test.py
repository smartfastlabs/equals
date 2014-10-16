from fuzzy_match import includes_elements, same_elements


def test_includes_elements_passes_on_super_set():
    assert includes_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }


def test_includes_elements_fails_on_sub_set():
    assert not includes_elements(foo='bar') == {'bob': 'barker'}


def test_same_elements_passes_on_identical_dict():
    assert same_elements(foo='bar') == {'foo': 'bar'}


def test_same_elements_fails_on_super_set():
    assert not same_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }


def test_same_elements_fails_on_sub_set():
    assert not same_elements(foo='bar', bob='bob') == {'foo': 'bar'}
