import pytest

from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template('madlib_cli/input1.txt')
    expected = "A {Adjective} and {Adjective} {Noun}."
    assert actual == expected


def test_read_template_bad_path():
    path = 'input1.txt'
    with pytest.raises(FileNotFoundError):
        read_template(path)


def test_parse_template():
    actual_stripped, actual_parts = parse_template( "A {Adjective} and {Adjective} {Noun}.")
    expected_stripped = "A {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")
    assert actual_parts == expected_parts
    assert actual_stripped == expected_stripped


def test_merge():
    actual = merge("A {} and {} {}.", ("dark", "stormy", "night"))
    expected = "A dark and stormy night."
    assert actual == expected


