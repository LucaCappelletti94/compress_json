"""Test if the local path feature is working as expected."""

import os
from .utils import local_call


def test_local_path():
    """Test whether the local path feature is working as expected."""
    target = os.sep.join("/compress_json/tests/object.json".split("/"))
    assert local_call().endswith(target)
