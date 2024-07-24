"""Test that version code is correct."""

from validate_version_code import validate_version_code
from compress_json.__version__ import __version__


def test_version():
    """Tests whether the version code is correct."""
    assert validate_version_code(__version__)
