import os
from .utils import local_call


def test_local_path():
    target = os.sep.join("/compress_json/tests/object.json".split("/"))
    assert local_call().endswith(target)