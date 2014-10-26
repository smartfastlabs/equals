from equals import any_dict


def test_has_elements_passes_on_super_set():
    assert any_dict.containing(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker',
    }


def test_has_elements_fails_on_sub_set():
    assert not any_dict.containing(foo='bar') == {'bob': 'barker'}


def hest_has_keys_passes_on_dict_with_exact_keys():
    assert any_dict.containing('foo', 'bob') == {
        'foo': 'bar',
        'bob': 'barker',
    }


def hest_has_keys_passes_on_dict_with_extra_keys():
    assert any_dict.containing('foo', 'bob') == {
        'foo': 'bar',
        'bob': 'barker',
        'ricky': 'bobby',
    }


def test_has_fails_on_dict_with_missing_keys():
    assert not any_dict.with_keys('foo', 'bob') == {'bob': 'barker'}


def test_order_of_test_does_not_matter():
    assert {'foo': 'bar'} == any_dict.containing(foo='bar')
