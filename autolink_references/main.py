import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


def replace_autolink_references(markdown, ref_prefix, target_url):
    if "<num>" not in ref_prefix:
        ref_prefix = ref_prefix + "<num>"
    find_regex = re.compile(
        r"(?<![#\[/])" + ref_prefix.replace(r"<num>", r"(?P<num>[-\w]+)")
    )
    linked_ref = rf"[{ref_prefix}](" + target_url + r")"
    replace_text = linked_ref.replace(r"<num>", r"\g<num>")
    markdown = re.sub(find_regex, replace_text, markdown, re.IGNORECASE)
    return markdown


class AutoLinkOption(config_options.OptionallyRequired):
    def run_validation(self, values):
        if not isinstance(values, list):
            raise config_options.ValidationError("Expected a list of autolinks.")

        for autolink in values:
            if "reference_prefix" not in autolink:
                raise config_options.ValidationError(
                    "Expected a 'reference_prefix' in autolinks."
                )
            if "target_url" not in autolink:
                raise config_options.ValidationError(
                    "Expected a 'target_url' in autolinks."
                )
            if "<num>" not in autolink["target_url"]:
                raise config_options.ValidationError("Missing '<num>' in 'target_url'.")

        return values


class AutolinkReference(BasePlugin):

    config_scheme = (("autolinks", AutoLinkOption(required=True)),)

    def on_page_markdown(self, markdown, **kwargs):
        """
        Takes an article written in markdown and looks for the
        presence of a ticket reference and replaces it with autual link
        to the ticket.

        :param markdown: Original article in markdown format
        :param kwargs: Other parameters (won't be used here)
        :return: Modified markdown
        """
        for autolink in self.config["autolinks"]:
            markdown = replace_autolink_references(
                markdown, autolink["reference_prefix"], autolink["target_url"]
            )

        return markdown
