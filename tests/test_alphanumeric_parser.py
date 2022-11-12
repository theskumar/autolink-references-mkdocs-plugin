import pytest

from autolink_references.main import replace_autolink_references as autolink

markdown_samples = [
    ("#A", "[#A](http://example/A)"),
    ("#A-1", "[#A-1](http://example/A-1)"),
    ("hello #B/_-A1", "hello [#B/_-A1](http://example/B/_-A1)"),
    ("(#2)", "([#2](http://example/2))"),
    ("x (#nn02)", "x ([#nn02](http://example/nn02))"),
    ("x (#2) y", "x ([#2](http://example/2)) y"),
    ("(#AA___//2)", "([#AA___//2](http://example/AA___//2))"),
    ("#A-1?????test", "[#A-1](http://example/A-1)?????test"),
]


@pytest.mark.parametrize("test_input,expected", markdown_samples)
def test_alphanumeric_parser(test_input, expected):
    ref_prefix = "#<num>"
    target_url = "http://example/<num>"

    assert autolink(test_input, ref_prefix, target_url, True) == expected
