import re

from equals import any_string


class TestContaining(object):
    test_obj = any_string.containing("abc")

    def test_string_contains_substring(self):
        assert self.test_obj == "123 abc 456"

    def test_string_does_not_contain_substring(self):
        assert not self.test_obj == "123 ac 456"

    def test_representation(self):
        expected = (
            r"Any instance of <(type|class) '(basestring|str)'> " r"containing: abc"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestStartingWith(object):
    test_obj = any_string.starting_with("abc")

    def test_string_startswith_substring(self):
        assert self.test_obj == "abcdef"

    def test_string_does_not_startswith_substring(self):
        assert not self.test_obj == "bcdef"

    def test_representation(self):
        expected = (
            "Any instance of <(type|class) '(basestring|str)'> " "starting with abc"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestEndingWith(object):
    test_obj = any_string.ending_with("abc")

    def test_string_endswith_substring(self):
        assert self.test_obj == "123abc"

    def test_string_does_not_endswith_substring(self):
        assert not self.test_obj == "123ab"

    def test_representation(self):
        expected = (
            "Any instance of <(type|class) '(basestring|str)'> " "ending with abc"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestMatching(object):
    test_obj = any_string.matching("^abc$")

    def test_string_matches_regex(self):
        assert self.test_obj == "abc"

    def test_string_does_not_match_regex(self):
        assert not self.test_obj == "ac"

    def test_representation(self):
        expected = (
            "Any instance of <(type|class) '(basestring|str)'> " "matching \\^abc\\$"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestNoConstraints(object):
    def test_with_no_constraints_pass_case(self):
        assert any_string == "bob barker"

    def test_with_no_constraints_fail_case(self):
        assert not any_string == 1

    def test_representation(self):
        expected = "Any instance of <(type|class) '(basestring|str)'>"
        assert re.match(expected, str(any_string))
        assert re.match("<Equals {}>".format(expected), repr(any_string))


def test_order_of_test_does_not_matter():
    assert "123 abc 456" == any_string.containing("abc")
