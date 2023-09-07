from function import sum_strings
import pytest

def test_empty_strings():
    assert sum_strings("", "") == ""

def test_full_empty_strings():
    str = "test string"
    assert sum_strings(str, "") == str
    assert sum_strings("", str) == str

def test_not_empty_strings():
    assert sum_strings("hello", "world") == "helloworld"

def test_string_and_anouther_types():
    with pytest.raises(TypeError):
        result = sum_strings("hello", 123)

    with pytest.raises(TypeError):
        result = sum_strings("hello", ["world", "!"])

    with pytest.raises(TypeError):
        result = sum_strings("hello", ("world", "!"))

    with pytest.raises(TypeError):
        result = sum_strings("hello", {"world"})

    with pytest.raises(TypeError):
        result = sum_strings("hello", None)


def test_string_with_spaces():
    str = "test string"
    assert sum_strings(str, " 1") == "test string 1"
    assert sum_strings(" 1", str) == " 1test string"
    assert sum_strings(str, "\t1") == "test string\t1"
    assert sum_strings("\t1", str) == "\t1test string"


def test_string_with_specific_simbols():
    str = "test string"
    assert sum_strings(str, " #$%^&*~") == "test string #$%^&*~"


def test_string_with_end_of_line():
    str = "test string\n"
    assert sum_strings(str, "123") == "test string\n123"


def test_on_large_strings():
    str = 'a' * 2000
    assert sum_strings(str, "123") == 'a' * 2000 + "123"


