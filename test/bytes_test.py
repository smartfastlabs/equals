from equals import any_bytes


def test_b_string():
    assert any_bytes == b"123 abc 456"


def test_containing():
    assert any_bytes.containing(b"123") == b"123 abc 456"


def test_endswith():
    assert any_bytes.ending_with(b"456") == b"123 abc 456"


def test_string():
    assert any_bytes != "123 abc 456"


def test_bytes_string():
    assert any_bytes == bytes("123 abc 456", encoding="utf-8")


def test_bytearray():
    # Not Sure what wwe want here
    assert any_bytes != bytearray("123 abc 456", encoding="utf-8")
