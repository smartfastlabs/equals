from fuzzy_match import has_elements, has_keys


def test_has_elements_passes_on_super_set():
    assert has_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker',
    }


def test_has_elements_fails_on_sub_set():
    assert not has_elements(foo='bar') == {'bob': 'barker'}


def hest_has_keys_passes_on_dict_with_exact_keys():
    assert has_keys('foo', 'bob') == {
        'foo': 'bar',
        'bob': 'barker',
    }


def hest_has_keys_passes_on_dict_with_extra_keys():
    assert has_keys('foo', 'bob') == {
        'foo': 'bar',
        'bob': 'barker',
        'ricky': 'bobby',
    }


def test_has_fails_on_dict_with_missing_keys():
    assert not has_keys('foo', 'bob') == {'bob': 'barker'}
