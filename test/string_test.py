from fuzzy_match import contains, startswith, endswith, matches


def test_string_contains_substring():
    assert contains('abc') == '123 abc 456'


def test_string_does_not_contain_substring():
    assert not contains('ac') == '123 abc 456'


def test_string_startswith_substring():
    assert startswith('abc') == 'abcdef'


def test_string_does_not_startswith_substring():
    assert not startswith('bc') == 'abcdef'


def test_string_endswith_substring():
    assert endswith('abc') == '123abc'


def test_string_does_not_endswith_substring():
    assert not endswith('ab') == '123abc'


def test_string_matches_regex():
    assert matches('^abc$') == 'abc'


def test_string_does_not_match_regex():
    assert not matches('^bc$') == 'abc'
