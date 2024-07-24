"""Test behaviour on wrong parameters."""

import pytest
import compress_json


def test_wrong_path():
    """In this test we check whether the method correctly rises an exception."""
    with pytest.raises(ValueError):
        compress_json.load({})

    with pytest.raises(ValueError):
        compress_json.dump({}, {})

    with pytest.raises(ValueError):
        compress_json.dump("", {})
