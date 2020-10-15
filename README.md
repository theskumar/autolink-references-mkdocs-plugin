# Autolink References (MkDocs Plugin)

This [mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/)
look in each MkDocs article for the presence of a references to tickets from issues
trackers like Jira, Linear, etc and convert them to links that point to respective
platforms:


## Getting started
To install it, using `pip`:

```
pip install autolink-references-mkdocs-plugin
```

Edit your `mkdocs.yml` file and add these few lines of code:

```yaml
plugins:
   - autolink_references:
        autolinks:
            - reference_prefix: AF-
              target_url: https://linear.com/AF-<num>
            - reference_prefix: PROJ-
              target_url: https://jiracloud.com/PROJ-<num>
```

- __reference_prefix__: This prefix appended by a number will generate a link any time it is found in an page.
- __target_url__: The URL must contain `<num>` for the reference number.

### An example

For example, you could edit the `docs/index.md` file and insert the ticket references like this:

````markdown

Changelog:

- AF-100: add new feature.

````

This will generate pre-processed to:

```
Changelog:

- [AF-100](https://linear.com/AF-100): add new feature.

```

## License

MIT

Built with ❤️ by [Saurabh Kumar](https://saurabh-kumar.com?ref=autolink-references-mkdocs-plugin)
