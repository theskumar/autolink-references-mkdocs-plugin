import pytest

from autolink_references.main import replace_autolink_references as autolink

simple_replace = [
    ("TAG-<num>", "http://gh/<num>", "TAG-123", "[TAG-123](http://gh/123)"),
    ("TAG-<num>", "http://gh/<num>", "x TAG-123", "x [TAG-123](http://gh/123)"),
    ("TAG-<num>", "http://gh/<num>", "TAG-123 x", "[TAG-123](http://gh/123) x"),
    ("TAG-<num>", "http://gh/<num>", "x TAG-123 y", "x [TAG-123](http://gh/123) y"),
    ("TAG-<num>", "http://gh/<num>", "x TAG-123 y", "x [TAG-123](http://gh/123) y"),
    ("TAG-<num>", "http://gh/TAG-<num>", "(TAG-123)", "([TAG-123](http://gh/TAG-123))"),
    ("TAG-", "http://forgot-num/<num>", "TAG-543", "[TAG-543](http://forgot-num/543)"),
    (
        "TAG-<num>",
        "http://gh/TAG-<num>",
        "(TAG-12_3-4)",
        "([TAG-12_3-4](http://gh/TAG-12_3-4))",
    ),
    (
        "TAG-<num>",
        "http://gh/<num>",
        "x TAG-123 y TAG-456 z",
        "x [TAG-123](http://gh/123) y [TAG-456](http://gh/456) z",
    ),
    (
        "TAG-<num>",
        "http://gh/TAG-<num>",
        "TAG-Ab123dD",
        "[TAG-Ab123dD](http://gh/TAG-Ab123dD)",
    ),
]

ignore_already_linked = [
    (
        "TAG-<num>",
        "http://gh/<num>",
        "[TAG-789](http://gh/789)",
        "[TAG-789](http://gh/789)",
    ),
    (
        "TAG-<num>",
        "http://gh/TAG-<num>",
        "[TAG-789](http://gh/TAG-789)",
        "[TAG-789](http://gh/TAG-789)",
    ),
]

ignore_ref_links = [
    ("TAG-<num>", "http://gh/<num>", "[TAG-456]", "[TAG-456]"),
    ("TAG-<num>", "http://gh/<num>", "[TAG-456][test456]", "[TAG-456][test456]"),
    ("TAG-<num>", "http://gh/<num>", "[TAG-456] [tag456]", "[TAG-456] [tag456]"),
    (
        "TAG-<num>",
        "http://gh/TAG-<num>",
        "[tag456]: http://gh/TAG-456",
        "[tag456]: http://gh/TAG-456",
    ),
]


@pytest.mark.parametrize(
    "ref_prefix, target_url, test_input, expected",
    simple_replace + ignore_already_linked + ignore_ref_links,
)
def test_parser(ref_prefix, target_url, test_input, expected):
    assert autolink(test_input, ref_prefix, target_url) == expected


def test_with_attr_list():
    text = "## Feature 1 { #F-001 .class-feature }"
    ref_prefix = "F-<num>"
    target_url = "http://gh/<num>"
    assert autolink(text, ref_prefix, target_url) == text
