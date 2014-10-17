from fuzzy_match import anything, anything_true, anything_false, any_instance


def test_anything_matches_none():
    assert anything == None  # noqa


def test_anything_matches_true():
    assert anything == True  # noqa


def test_anything_true_matches_true():
    assert anything_true == True  # noqa


def test_anything_true_matches_a_string():
    assert anything_true == 'test'


def test_anything_true_does_not_match_false():
    assert not anything_true == False  # noqa


def test_anything_false_matches_false():
    assert anything_false == False  # noqa


def test_anything_false_does_not_match_true():
    assert not anything_false == True  # noqa


def test_any_instance_matches():
    assert any_instance(dict) == {}


def test_any_instance_with_multiple_types():
    assert any_instance(dict, tuple) == (1, 2)
