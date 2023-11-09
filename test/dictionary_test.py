import re

from equals import any_dict


class TestNotContaining(object):
    test_obj = any_dict.not_containing("key1", key2="bar")

    def test_passes_on_dict_not_containing_key_or_value(self):
        assert self.test_obj == {
            "foo": "bar",
            "bob": "barker",
        }

    def test_failes_on_dict_containing_key(self):
        assert not self.test_obj == {"key1": "barker"}

    def test_fails_on_dict_containing_value(self):
        assert not self.test_obj == {"key2": "bar"}

    def test_passes_on_dict_with_key_but_wrong_value(self):
        assert self.test_obj == {"key2": "bob"}

    def test_representation(self):
        expected = (
            "Any instance of <(type|class) 'dict'> not containing: key1 and key2=bar"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestContaining(object):
    test_obj = any_dict.containing(foo="bar")

    def test_passes_on_super_set(self):
        assert self.test_obj == {
            "foo": "bar",
            "bob": "barker",
        }

    def test_fails_on_sub_set(self):
        assert not self.test_obj == {"bob": "barker"}

    def test_representation(self):
        expected = "Any instance of <(type|class) 'dict'> containing: foo=bar"
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestContainingKeys(object):
    test_obj = any_dict.containing("foo", "bob")

    def test_passes_on_dict_with_exact_keys(self):
        assert self.test_obj == {
            "foo": "bar",
            "bob": "barker",
        }

    def test_passes_on_dict_with_extra_keys(self):
        assert self.test_obj == {
            "foo": "bar",
            "bob": "barker",
            "ricky": "bobby",
        }

    def test_fails_on_dict_with_missing_keys(self):
        assert not self.test_obj == {"bob": "barker"}

    def test_representation(self):
        expected = "Any instance of <(type|class) 'dict'> containing: foo, bob"
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


class TestContaingKeysAndItems(object):
    test_obj = any_dict.containing("foo", "bar", bob="barker")

    def test_passes_on_dict_with_keys_and_items(self):
        assert self.test_obj == {
            "foo": "bar",
            "bob": "barker",
            "bar": "bobby",
        }

    def test_fails_on_dict_with_keys_but_not_items(self):
        assert not self.test_obj == {
            "foo": "bar",
            "bar": "bobby",
        }

    def test_fails_on_dict_with_items_but_not_all_keys(self):
        assert not self.test_obj == {
            "foo": "bar",
            "bob": "barker",
        }

    def test_representation(self):
        expected = (
            "Any instance of <(type|class) 'dict'> containing: "
            "foo, bar and bob=barker"
        )
        assert re.match(expected, str(self.test_obj))
        assert re.match("<Equals {}>".format(expected), repr(self.test_obj))


def test_order_of_test_does_not_matter():
    assert {"foo": "bar"} == any_dict.containing(foo="bar")
