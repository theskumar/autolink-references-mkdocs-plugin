import pytest

from autolink_references.main import replace_autolink_references as autolink

markdown_samples = [
    ("#1", "[#1](http://gh/1)"),
    ("hello #1", "hello [#1](http://gh/1)"),
    ("(#2)", "([#2](http://gh/2))"),
    ("x (#2)", "x ([#2](http://gh/2))"),
    ("x (#2) y", "x ([#2](http://gh/2)) y"),
    ("(#2)", "([#2](http://gh/2))"),
]


@pytest.mark.parametrize("test_input,expected", markdown_samples)
def test_parser(test_input, expected):
    ref_prefix = "#<num>"
    target_url = "http://gh/<num>"

    assert autolink(test_input, ref_prefix, target_url, False) == expected
