from equals import any_string


def test_string_contains_substring():
    assert any_string.containing('abc') == '123 abc 456'


def test_string_does_not_contain_substring():
    assert not any_string.containing('ac') == '123 abc 456'


def test_string_startswith_substring():
    assert any_string.starting_with('abc') == 'abcdef'


def test_string_does_not_startswith_substring():
    assert not any_string.starting_with('bc') == 'abcdef'


def test_string_endswith_substring():
    assert any_string.ending_with('abc') == '123abc'


def test_string_does_not_endswith_substring():
    assert not any_string.ending_with('ab') == '123abc'


def test_string_matches_regex():
    assert any_string.matching('^abc$') == 'abc'


def test_string_does_not_match_regex():
    assert not any_string.matching('^bc$') == 'abc'


def test_order_of_test_does_not_matter():
    assert '123 abc 456' == any_string.containing('abc')


def test_with_no_constraints_pass_case():
    assert any_string == 'bob barker'


def test_with_no_constraints_fail_case():
    assert not any_string == 1
