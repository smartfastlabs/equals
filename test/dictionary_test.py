import fuzzy_match.matchers as matchers


def test_includes_elements_passes_on_super_set():
    assert matchers.includes_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }


def test_includes_elements_fails_on_sub_set():
    assert not matchers.includes_elements(foo='bar') == {'bob': 'barker'}


def test_same_elements_passes_on_identical_dict():
    assert matchers.same_elements(foo='bar') == {'foo': 'bar'}


def test_same_elements_fails_on_super_set():
    assert not matchers.same_elements(foo='bar') == {
        'foo': 'bar',
        'bob': 'barker'
    }


def test_same_elements_fails_on_sub_set():
    assert not matchers.same_elements(foo='bar', bob='bob') == {'foo': 'bar'}
