import io
from setuptools import setup

from pathlib import Path

readme_path = Path(__file__).parent / "README.md"

with io.open(readme_path, encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='autolink-references-mkdocs-plugin',
    version='0.2.0',
    packages=['autolink_references'],
    url='https://github.com/theskumar/autolink-references-mkdocs-plugin',
    license='MIT',
    author='Saurabh Kumar',
    author_email='noreply@theskumar.github.com',
    description='This plugin allows to configure your own autolink references for non-GitHub URLs.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'autolink_references = autolink_references:AutolinkReference',
        ]
    },
)
