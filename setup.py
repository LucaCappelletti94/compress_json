"""Module providing the installation setup for the compress_json package."""
import os
import re
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()


def read(*parts):
    """Read document at given path."""
    with open(os.path.join(here, *parts), 'r', encoding='utf8') as file:
        return file.read()


def find_version(*file_paths):
    """Returns version code found in provided standard version document."""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("compress_json", "__version__.py")

test_deps =[
    "pytest",
    "pytest-cov",
    "validate_version_code",
    "random_dict",
    "dict_hash"
]

extras = {
    'test': test_deps,
}

setup(
    name='compress_json',
    version=__version__,
    description="The missing Python utility to read and write large compressed JSONs.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/LucaCappelletti94/compress_json",
    author="Luca Cappelletti",
    author_email="cappelletti.luca94@gmail.com",
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    extras_require=extras,
)
