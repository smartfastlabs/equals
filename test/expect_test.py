from fuzzy_match import expect


def test_to_include_passes():
    expect([1, 2, 3]).to_include(1, 2)


def test_to_have_exactly():
    expect([1, 2, 3]).to_have_exactly(1, 2, 3)


def test_to_contain():
    expect('bob barker').to_contain('bar')


def test_to_start_with():
    expect('bob barker').to_start_with('bob')


def test_to_end_with():
    expect('bob barker').to_end_with('barker')


def test_to_match():
    expect('bob barker').to_match('^bob barker$')
